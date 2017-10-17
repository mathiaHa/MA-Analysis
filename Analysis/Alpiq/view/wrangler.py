import pandas as pd
import numpy as np

import storage as st
import normalization as norm

import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import pydocumentdb.errors as errors
import pydocumentdb.http_constants as http_constants

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import types
import itertools

def GetDataFromCosmos(HOST, MASTER_KEY, DATABASE_ID, COLLECTION_ID, proc_id, params, options):
    dodocs = None
    try:
        client = document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY})
        
        coll_link = st.GetCollectionLink(client, DATABASE_ID, COLLECTION_ID)
        
        dodocs = st.ExecuteProcedure( client, coll_link, proc_id, params, options )
    except BaseException as e:
        raise e
    
    return dodocs
    
def MergeCosmosData( dodocs ):
    
    data = []
    
    for key, value in dodocs.iteritems():
        df = pd.DataFrame(value)
        df["resource"] = key
        df["alert"] = "NORMAL"
        df["downgraded"] = "NORMAL"
        data.append(df)
        
    data = norm.FindProbableFloat(data)
    df = pd.concat(data, axis=0)
    
    return df

def MarkInsufficientOffers( df ):
    
    for index, row in df[df.resource == "insufficients_offers"].iterrows():
        if row.type == "DOWNGRADED":
            condition = np.logical_and(df.start_date >= row.start_date, df.start_date < row.end_date)
            df.loc[condition, "downgraded"] = row.nature
        elif row.type == "WARNING":
            condition = np.logical_and(df.start_date >= row.start_date, df.start_date < row.end_date)
            df.loc[condition, "alert"] = row.nature
    
    return df

def NormalizePeakDailyMargins( df ):

    indexs = [] #index of original peak daily margins row
    df3 = pd.DataFrame([]) 
    
    for index, row in df[df.resource == "peak_daily_margins"].iterrows():
        # start/end of margins
        start = pd.date_range(start=row.start_date, end=row.end_date, freq='30T', closed='left')
        end = pd.date_range(start=row.start_date, end=row.end_date, freq='30T', closed='right')
    
        # search current direction of market
        do = df[df.start_date == row.start_date]
        distance = do[do.resource == "accepted_offers"].direction.unique()

        row.direction = distance[0] if len(distance)>0 else "UP_DOWN"

        df2 = pd.concat([row]*len(start), ignore_index=True, axis=1).T

        df2.start_date = start
        df2.end_date = end

        df3 = df3.append(df2)
        indexs.append(index)

    df = df.drop(df.index[[indexs]])
    df = df.append(df3, ignore_index=True)
    
    return df

def GetMarket(cfg, params, options):
    try:
        dodocs = GetDataFromCosmos(cfg["HOST"], cfg["MASTER_KEY"], cfg["DATABASE_ID"], cfg["COLLECTION_ID"], cfg["PROCEDURE_ID"], params, options)
    
        data = []

        df = MergeCosmosData( dodocs )
    
        # Set date columns as normalized datetime columns
        df[["start_date", "end_date"]]= df[["start_date", "end_date"]].astype(np.datetime64)
        df = df[df.start_date < df.end_date]
        
        df = MarkInsufficientOffers( df )

        df = NormalizePeakDailyMargins( df )

        # Drop Rows
        df = df[df.resource != "insufficients_offers"]
        
        valueList = ["available_value","price", "required_value", "value"]
        
        

        divider = getattr(cfg["GROUPS"], "balancing_capacity")
        NumberTypes = (types.IntType, types.LongType, types.FloatType, types.ComplexType)
        if not valueList ==[] :
            table_df = pd.pivot_table(
                        df,
                        values=valueList,
                        index=['start_date','end_date','resource','type','direction','alert','downgraded'],
                        aggfunc= 'first')

            # Go from multi columns to cube
            level = 7
            table_df = table_df.stack(0).reset_index(level)
            table_df = table_df.rename(index=str, columns={"level_"+str(level): "value_type"})

            # Set date columns as normalized datetime columns
            table_df = table_df.reset_index()
            table_df[["start_date", "end_date"]]= table_df[["start_date", "end_date"]].astype(np.datetime64)


            # Set multi index dataframe
            table_df = table_df.set_index(['start_date','end_date','resource','type','direction','alert','downgraded',"value_type"])
            table_df = table_df.rename(index=str, columns={0:"value"})
    except BaseException as e:
        print e
            
    return table_df
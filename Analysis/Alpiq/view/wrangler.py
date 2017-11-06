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

def MergeCosmosData( dodocs ):
    
    data = []
    
    for key, value in dodocs.iteritems():
        df = pd.DataFrame(value)
        df["resource"] = key
        data.append(df)
        
    data = norm.FindProbableFloat(data)
    df = pd.concat(data, axis=0)
    
    return df

def MarkInsufficientOffers( df ):
    
    for index, row in df[df.resource == "insufficients_offers"].iterrows():
        if row.type == "DOWNGRADED":
            condition = np.logical_and(df.start_date >= row.start_date, df.start_date < row.end_date)
            df.loc[condition, "downgraded"] = row["nature"]
        elif row.type == "WARNING":
            condition = np.logical_and(df.start_date >= row.start_date, df.start_date < row.end_date)
            df.loc[condition, "alert"] = row["nature"]
    
    return df

def MarkPPDay( df ):
    for index, row in df[df.type == "PP2"].iterrows():
        if row.value:
            condition = np.logical_and(df.start_date >= row.start_date, df.start_date < row.end_date)
            df.loc[condition, "PP"] = row.type
    for index, row in df[df.type == "PP1"].iterrows():
        if row.value:
            condition = np.logical_and(df.start_date >= row.start_date, df.start_date < row.end_date)
            df.loc[condition, "PP"] = row.type
            
    return df

def Row2Categories ( df, resources ):
    for resource in resources:
        if resource == "insufficients_offers":
            df["alert"] = "NORMAL"
            df["downgraded"] = "NORMAL"
            df = MarkInsufficientOffers( df )
            df = df[df.resource != "insufficients_offers"] # Drop Rows
        
        elif resource == "signals":
            df["PP"] = "NORMAL"
            df = MarkPPDay( df )
            df = df[df.resource != "signals"]
    return df

def update_startend(x, df1, freq):
    if x.name < df1.shape[0]:
        x.end_date = x.start_date + pd.Timedelta(freq)
    else:
        x.start_date = x.end_date - pd.Timedelta(freq)
    return x

def PropagateData( df, resources, freq='30 min' ):
    
    for resource in resources:
        if resource in ["peak_daily_margins"]:
            
            df0 = df[df.resource == resource]

            df1 = df0.set_index("start_date").resample(freq).pad().reset_index()
            df2 = df0.set_index("end_date").resample(freq).bfill().reset_index()
            df3 = pd.concat([df1, df2], ignore_index=True)


            df3 = df3[ df3.start_date < df3.end_date ].apply(lambda x: update_startend(x, df1, freq), axis=1)

            df = df[df.resource != resource]
            df = df.append(df3, ignore_index=True)
    return df

def MergeColumns( df ):
    cols = list(df.columns.values)
    
    if set(["direction", "system_trend"]).issubset(set(cols)):
        df.loc[df.system_trend.isnull() == False, "direction"] = df.loc[df.system_trend.isnull() == False, "system_trend"].map({'HAUSSE': 'UPWARD', 'BAISSE': 'DOWNWARD', 'NULLE': 'UP_DOWN'})
    
    return df

def GetMarket(cfg, params, options):
    try:
        df = st.GetDataFromCosmos(cfg["HOST"], cfg["MASTER_KEY"], cfg["DATABASE_ID"], cfg["COLLECTION_ID"], cfg["PROCEDURE_ID"], params, options)
        
        # Drop Pulicates data
        df.drop_duplicates(keep='first', inplace=True)
        
        # fillna here
        
        df = MergeColumns( df )
        
        if "direction" in df.reset_index().columns:
            df.loc[df.direction.isnull(),"direction"] = "UP_DOWN"
    
        # Set date columns as normalized datetime columns
        df[["start_date", "end_date"]]= df[["start_date", "end_date"]].astype(np.datetime64)
        df = df[df.start_date < df.end_date]
        
        df = PropagateData( df, params["resources"], '30 min' )
        
        df = Row2Categories ( df, params["resources"] )

        valueList = list(df.select_dtypes(include=["int","float","float64","long"]).columns) #["available_value","price", "required_value", "value"]
        
        if not valueList ==[] :
            table_df = pd.pivot_table(
                        df,
                        values=valueList,
                        index=cfg["index"],
                        aggfunc= 'first')
            
            # Go from multi columns to cube
            level = len(cfg["index"])
            table_df = table_df.stack(0).reset_index(level)
            table_df = table_df.rename(index=str, columns={"level_"+str(level): "value_type"})

            # Set date columns as normalized datetime columns
            table_df = table_df.reset_index()
            table_df[["start_date", "end_date"]]= table_df[["start_date", "end_date"]].astype(np.datetime64)


            # Set multi index dataframe
            table_df = table_df.set_index(cfg["index"]+["value_type"])
            table_df = table_df.rename(index=str, columns={0:"value"})
    except BaseException as e:
        print e
            
    return table_df
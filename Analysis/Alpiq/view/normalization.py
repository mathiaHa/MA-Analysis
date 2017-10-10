import pandas as pd

def GetDescription( df, dividers, res_names, index_names ):
    description = GetDescribe( df, dividers, res_names )
    description_df = {}
    for key, value in description.iteritems():
        description_df[key] = GetSingletonStatistic(description[key])
    
    description_df = pd.concat(description_df)
    description_df.index.names = index_names
    return description_df


def GetSingletonStatistic( description ):
    description = description.stack(0).reset_index(1)
    description = description.rename(index=str, columns={"level_1": "Value_Type"})
    index = pd.MultiIndex.from_tuples(GetSubResourceIndexs( description ))
    description = pd.DataFrame(description.values,index,description.columns);
    description= description.drop('Value_Type', axis=1)
    return description

def GetSubResourceIndexs( description ):
    index =[]
    if (type([description.Value_Type[i] for i in description.index][0])  is pd.core.series.Series) :
        index = pd.MultiIndex.from_tuples([(i,s) for i in description.index for s in description.Value_Type[i]])
    else:
        index = pd.MultiIndex.from_tuples([(i,description.Value_Type[i]) for i in description.index])
    
    return index.unique()

def GetDescribe( df, dividers, res_names ):
    description = {}
    
    for res_name in res_names:
    
        if not df[res_name].empty:
            if (dividers[res_name] != None 
                and any(dividers[res_name] in s for s in df[res_name].columns.values)):
                groups = df[res_name].groupby([dividers[res_name]])
                description[res_name] = groups.describe()
            else:
                description[res_name] = df[res_name].describe().T
                description[res_name].columns = pd.MultiIndex.from_tuples([(res_name, c) for c in description[res_name].columns])
    
    return description

def FindProbableFloat( dic ):
    for key, df in dic.iteritems():
        for col in df.columns:
            try:
                dic[key][col] = dic[key][col].astype(float)
            except:
                x = 42
    return dic
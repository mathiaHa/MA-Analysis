import pandas as pd
import numpy as np
import chardet
import pytz

# Read CSV

def ReadCSV(path, seps):
    for separator in seps:

        # Read the file
        with open(path, 'rb') as f:
            result = chardet.detect(f.readline())
        
        docs = pd.read_csv(path, index_col=0, parse_dates=True, sep = separator, encoding=result["encoding"], decimal=".", thousands=',')

        if not docs.shape[1] == 0:
            break
            
    return docs

# Normalize data

def NormalizeCSV(docs, columns, traduction):
    # Change the column titles
    docs.columns = columns
    
    # Normalization of the columns
    docs.type = docs.type.apply(lambda x: traduction[x.encode("utf-8")] if traduction.has_key(x.encode("utf-8")) else x)
    docs.direction = docs.direction.apply(lambda x: traduction[x.encode("utf-8")] if traduction.has_key(x) else x)
    docs.value = docs[[ "value"]].apply(lambda x: [float(v) for v in x])
        
    docs.value = docs[[ "value"]].apply(lambda x: [float(v) for v in x])
    docs.price=docs.price.apply(lambda x : str(x) if not isinstance(x, (str)) else x)
    docs.price=docs.price.apply(lambda x : x.replace(',','.') if not isinstance(x, (float, long, int)) else x)
    docs.price=docs.price.apply(lambda x : None if x=='*' else x)
    docs.price=docs.price.astype(float)
        
    # Add start_date and end_date
    docs["Dates"] = docs.index
    docs[["start_date", "end_date"]] = docs[["Dates", "Heures"]].apply(lambda x: split2StartEnd(x), axis=1)
    
    return docs

def split2StartEnd(x):
    delta = [[int(m) for m in i.split(":")] for i in x[1].split(" - ") ]
    
    return [addHm(x[0], d) for d in delta]

def addHm(x, delta):
    x = x + np.timedelta64(delta[0], 'h')
    x = x + np.timedelta64(delta[1], 'm')
    return x

# Shape data
def CreateDictOfDocument(groups):
    dic = {}
    
    for key, df in groups:
        df = CreateData(df)
        dic[key] = df
    return dic

def CreateData(df):
    zone = pytz.timezone('Europe/Paris')
    df.index = range(df.shape[0])
    df = df.drop(["Dates", "Heures"], axis=1)
    df.start_date = df.start_date.apply(lambda x: str(zone.localize(x)))
    df.end_date = df.end_date.apply(lambda x: str(zone.localize(x)))
    df.price = df.price.apply(lambda x: str(x) if not np.isnan(x) else None)
    values = df.T.to_dict().values()
    return values

def GetStartEnd(groups):
    dic = {}
    zone = pytz.timezone('Europe/Paris')
    for key, df in groups:

        dic[key] = { 
            "start_date" : zone.localize(df.start_date.min()),
            "end_date" : zone.localize(df.end_date.max())
        }
    return dic

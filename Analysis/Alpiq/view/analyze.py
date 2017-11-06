import numpy as np
import scipy
import pandas as pd


def MultipleFilter(df, selection):
    """Filter a dataframe with multiple values. 
    /!\ 0..1 value per index level not more
    
    :Parameters:
        -`df`: pandas.DataFrame
        -`selection`: list
        
    :Returns:
        Multi Index pandas.DataFrame
    """
    index_names = df.index.names
    for item in selection:
        df = df.filter(like=item, axis = 0)
        if df.shape[1] == 0:
            break
    df = df.reset_index().set_index(index_names)
    return df

def kruskal(df, groups ,kurkeys, x, alpha):
    """Apply a kruskal test on a pandas.DataFrame with a classifiaction stored in groups as paur key/list of index. kurkeys contains the list of the possible keys. x is the name of the variable on which we are doing a distribution test. alpha the statistic primary failure.
    
    :Parameters:
        -`df` : pandas.DataFrame
        -`groups`: pandas.groupby
        -`kurkeys`: list
        -`x`: string
        -`alpha`: float
    :Returns:
        dict
    """
    results = {}
    try:
        if groups != None:
            if kurkeys.shape[0] == 2:
                _, p = scipy.stats.kruskal(
                    df.loc[groups[kurkeys[0]],x],
                    df.loc[groups[kurkeys[1]],x])

            elif kurkeys.shape[0] == 3:
                _, p = scipy.stats.kruskal(
                    df.loc[groups[kurkeys[0]],x],
                    df.loc[groups[kurkeys[1]],x],
                    df.loc[groups[kurkeys[2]],x]) 

        if p:
            results = {"kruskal" : p > alpha}
    except Exception as ex:
        if False:
            print ex
    
    return results
          
def mannwhitneyu(df, groups ,kurkeys, x, alpha):
    """Apply a Mann Whitney test on a pandas.DataFrame with a classifiaction stored in groups as paur key/list of index. kurkeys contains the list of the possible keys. x is the name of the variable on which we are doing a distribution test. alpha the statistic primary failure.
    
    :Parameters:
        -`df` : pandas.DataFrame
        -`groups`: pandas.groupby
        -`kurkeys`: list
        -`x`: string
        -`alpha`: float
    :Returns:
        dict
    """
    results = {}
    p = []
    try:
        if groups != None:

            if kurkeys.shape[0] == 2:

                p.append(scipy.stats.mannwhitneyu(
                    df.loc[groups[kurkeys[0]],x],
                    df.loc[groups[kurkeys[1]],x]).pvalue)

            elif kurkeys.shape[0] == 3:
                p.append(scipy.stats.mannwhitneyu(
                    df.loc[groups[kurkeys[0]],x],
                    df.loc[groups[kurkeys[1]],x]).pvalue)
                p.append(scipy.stats.mannwhitneyu(
                    df.loc[groups[kurkeys[0]],x],
                    df.loc[groups[kurkeys[2]],x]).pvalue)
                p.append(scipy.stats.mannwhitneyu(
                    df.loc[groups[kurkeys[1]],x],
                    df.loc[groups[kurkeys[2]],x]).pvalue)

        if p != []:
            results = {"mannwhitneyu" : all(i >= alpha for i in p)}
    except Exception as ex:
        if False:
            print ex
    
    
    return results

def norlmaltest(df, x, alpha, stamp):
    """Apply a normal test on a pandas.DataFrame.  is the name of the variable on which we are doing a distribution test. alpha the statistic primary failure.
    
    :Parameters:
        -`df` : pandas.DataFrame
        -`x`: string
        -`alpha`: float
    :Returns:
        dict
    """
    
    results = {}
    if df.shape[0] > 8:
        results = {"normal_"+stamp : scipy.stats.normaltest(df[x]).pvalue > alpha }
    
    return results

def stats(df, hues, value, alpha):
    """Apply kruskal, Mann Whitney and normal test on a pandas.DataFrame. Hues is a list of classification on which we want to all the tests. Value is the name of the value on which we are doing the test and alpha the statistic primary failure.
    
    :Parameters:
        -`df` : pandas.DataFrame
        -`hues` : list
        -`value`: string
        -`alpha`: float
    :Returns:
        pandas.DataFrame
    """
    results = []
    
    for hue in hues:
        if not df.empty:
            kurkeys = np.asarray(sorted(df[hue].unique()))
            grouped = df.groupby(hue)
            groups = grouped.groups if kurkeys.shape[0] > 1 else None
                        
            if groups != None:
                
                dic = {
                    'hue': hue,
                }
                dic.update(mannwhitneyu(df, groups ,kurkeys, value, alpha))
                dic.update(kruskal(df, groups ,kurkeys, value, alpha))
                dic.update(norlmaltest(df[df[hue] != "NORMAL"], value, alpha, 'tension'))
                dic.update(norlmaltest(df[df[hue] == "NORMAL"], value, alpha, 'normal'))
                dic.update(df.describe().value)
                results.append(dic)
    
    sub_df = pd.DataFrame(results)          
    return sub_df if results != [] else None
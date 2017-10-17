def MultipleFilter(df, selection):
    index_names = df.index.names
    for item in selection:
        df = df.filter(like=item, axis = 0)
        if df.shape[1] == 0:
            break
    df = df.reset_index().set_index(index_names)
    return df


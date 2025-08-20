def get_summary_stats(df,group_col=None):
    if group_col:
        return df.groupby(group_col).mean(numeric_only=True).reset_index()
    else:
        return df.describe()

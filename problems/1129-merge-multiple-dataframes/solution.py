import pandas as pd

def solution(df1, df2, df3):
    merger_df = pd.merge(df1,df2,on='emp_id',how='inner')
    final_df = pd.merge(merger_df,df3,on='emp_id',how='left')
    return final_df.reset_index(drop=True)
    pass
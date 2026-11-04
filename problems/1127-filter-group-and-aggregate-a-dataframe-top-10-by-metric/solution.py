import pandas as pd

def solution(df):
    df = df[df['status']=='completed']
    result = df.groupby('region',as_index=False)['amount'].sum()
    result = result.sort_values(by='amount',ascending=False).head(10)    
    return result
    pass
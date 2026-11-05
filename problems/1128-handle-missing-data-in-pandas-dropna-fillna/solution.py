import pandas as pd

def solution(df):
    col_thresh = df.isna().mean()
    df = df.loc[:,col_thresh<=0.5]

    row_thresh = df.isna().mean(axis=1)
    df = df.loc[row_thresh<=0.5]

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode().iloc[0])

    return df.reset_index(drop=True)
    
    pass
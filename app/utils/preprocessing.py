import pandas as pd

def validate_ecg_dataframe(df: pd.DataFrame):
    if df.shape[1] == 188:
        df = df.iloc[:, :-1]
    if df.shape[1] != 188:
        raise ValueError(
            "Uploaded file must contain exactly 187 features."
        )
    
    return df
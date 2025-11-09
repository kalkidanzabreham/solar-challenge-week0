import pandas as pd
from src.data_cleaning import clean_data

def test_clean_data_removes_nans():
    df = pd.DataFrame({'GHI': [100, None, 300], 'DNI': [200, 400, None]})
    clean_df = clean_data(df)
    assert not clean_df.isna().any().any(), "There should be no NaN values after cleaning"

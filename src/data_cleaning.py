"""
data_cleaning.py
----------------
Module for cleaning and preprocessing solar datasets.
"""

import pandas as pd
from scipy import stats

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataset by handling missing values and removing outliers.

    Args:
        df (pd.DataFrame): Input raw DataFrame.
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Drop or fill missing values
    df = df.fillna(df.median(numeric_only=True))
    
    # Remove extreme outliers for key columns
    for col in ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']:
        df = df[(abs(stats.zscore(df[col], nan_policy='omit')) < 3)]
    
    return df

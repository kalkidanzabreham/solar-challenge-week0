"""
data_loader.py
--------------
Module for loading and profiling solar datasets.
"""

import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV data into a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    df = pd.read_csv(filepath)
    print(f"✅ Loaded {len(df)} rows and {len(df.columns)} columns from {filepath}")
    return df

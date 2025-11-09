"""
run_eda.py
----------
Reproduce cleaning and EDA steps for all countries.
"""

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.eda_visuals import plot_correlation_heatmap
import pandas as pd
import os

COUNTRIES = ["benin", "sierra_leone", "togo"]
DATA_DIR = "data"

os.makedirs(f"{DATA_DIR}/cleaned", exist_ok=True)

for country in COUNTRIES:
    print(f"\n🌍 Processing {country.title()}...")
    raw_path = f"{DATA_DIR}/{country}.csv"
    df = load_data(raw_path)
    clean_df = clean_data(df)
    clean_df.to_csv(f"{DATA_DIR}/cleaned/{country}_clean.csv", index=False)
    print(f"✅ Cleaned file saved to {DATA_DIR}/cleaned/{country}_clean.csv")

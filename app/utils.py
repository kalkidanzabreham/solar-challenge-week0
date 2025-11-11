
from pathlib import Path
import pandas as pd

DATA_DIR = Path("../data/cleaned")

def load_country_csvs(file_map=None):
    """
    Load cleaned CSVs for countries.
    Returns a dictionary: country_name -> DataFrame
    """
    if file_map is None:
        file_map = {
            "Benin": DATA_DIR / "benin_clean.csv",
            "Sierra Leone": DATA_DIR / "sieraleone_clean.csv",
            "Togo": DATA_DIR / "togo_clean.csv"
        }
    dfs = {}
    for name, p in file_map.items():
        if p.exists():
            dfs[name] = pd.read_csv(p, parse_dates=["Timestamp"], infer_datetime_format=True)
        else:
            raise FileNotFoundError(f"{p} not found. Please put the cleaned CSVs in data/cleaned/")
    return dfs

def combine_for_plot(dfs):
    """Combine all country DataFrames into one with a 'country' column."""
    frames = []
    for country, df in dfs.items():
        tmp = df.copy()
        tmp["country"] = country
        frames.append(tmp)
    return pd.concat(frames, ignore_index=True)

def metrics_summary(dfs, metrics=["GHI","DNI","DHI"]):
    """Return a summary DataFrame with mean, median, and std for each metric."""
    rows = []
    for country, df in dfs.items():
        row = {"country": country}
        for m in metrics:
            series = df[m].dropna()
            row[f"{m}_mean"] = series.mean()
            row[f"{m}_median"] = series.median()
            row[f"{m}_std"] = series.std()
        rows.append(row)
    return pd.DataFrame(rows).set_index("country")

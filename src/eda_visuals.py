"""
eda_visuals.py
--------------
EDA visualization utilities for solar datasets.
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df, title="Correlation Heatmap"):
    """Plot heatmap for selected numerical columns."""
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title(title)
    plt.show()

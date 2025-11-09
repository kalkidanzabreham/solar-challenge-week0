# src/eda_visuals.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df, title="Correlation Heatmap"):
    """
    Plots a clean, readable correlation heatmap.
    """
    plt.figure(figsize=(10, 8))
    corr = df.corr(numeric_only=True)

    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="YlOrRd",
        annot_kws={"size": 8},
        cbar_kws={'shrink': 0.7}
    )

    plt.title(title, fontsize=14, pad=20)
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    plt.show()

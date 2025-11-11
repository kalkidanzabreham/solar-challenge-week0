# app/main.py
import streamlit as st
import plotly.express as px
from scipy import stats
import pandas as pd
from utils import load_country_csvs, combine_for_plot, metrics_summary

st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("🌞 Solar Potential Comparison Dashboard")
st.markdown("Analyze and compare **GHI**, **DNI**, and **DHI** across Benin, Sierra Leone, and Togo.")

# Load data
try:
    dfs = load_country_csvs()
except FileNotFoundError as e:
    st.error(str(e))
    st.stop()

countries = list(dfs.keys())

# Sidebar widgets
st.sidebar.header("⚙️ Controls")
selected_countries = st.sidebar.multiselect("Select countries", countries, default=countries)
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI"])
show_stats = st.sidebar.checkbox("Show Summary Table", value=True)
run_stat_test = st.sidebar.checkbox("Run Statistical Test", value=True)

# Filter data
dfs_sel = {c: dfs[c] for c in selected_countries}
if not dfs_sel:
    st.warning("Please select at least one country.")
    st.stop()

combined = combine_for_plot(dfs_sel)

# --- Boxplot ---
fig = px.box(
    combined,
    x="country",
    y=metric,
    color="country",
    points="outliers",
    title=f"{metric} Distribution Across Countries"
)
st.plotly_chart(fig, use_container_width=True)

# --- Summary Table ---
if show_stats:
    st.subheader("📊 Summary Metrics")
    summary = metrics_summary(dfs_sel)
    st.dataframe(summary.round(2))

# --- Mean GHI Ranking ---
if "GHI_mean" in summary.columns:
    st.subheader("🏆 Countries Ranked by Mean GHI")
    mean_rank = summary["GHI_mean"].sort_values(ascending=False)
    rank_fig = px.bar(
        x=mean_rank.values,
        y=mean_rank.index,
        orientation="h",
        labels={"x": "Mean GHI (W/m²)", "y": "Country"},
        color=mean_rank.index
    )
    st.plotly_chart(rank_fig, use_container_width=True)

# --- Statistical Test ---
if run_stat_test and len(dfs_sel) > 1:
    st.subheader("🧮 Kruskal-Wallis Test (for GHI Differences)")
    groups = [df["GHI"].dropna().values for df in dfs_sel.values()]
    h_stat, p_val = stats.kruskal(*groups)
    st.write(f"H = {h_stat:.3f}, p = {p_val:.4g}")
    if p_val < 0.05:
        st.success("Significant differences detected (p < 0.05)")
    else:
        st.info("No significant difference (p ≥ 0.05)")

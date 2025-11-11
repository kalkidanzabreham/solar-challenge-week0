# 🌞 Solar Challenge Week 0 – KIAM 10 Academy

**Author:** Kalkidan Abreham  
**Cohort:** KIAM 10 Academy  
**Repository:** [solar-challenge-week0](https://github.com/kalkidanzabreham/solar-challenge-week0)

---

## 📘 Project Overview

This repository contains my submission for **KIAM 10 Academy – Week 0 Challenge**, focusing on data profiling, cleaning, and exploratory data analysis (EDA) of solar radiation datasets from **Benin**, **Sierra Leone**, and **Togo**.

The project supports **MoonLight Energy Solutions** in identifying high-potential regions for solar installations through quick, data-driven insights into environmental and meteorological variables.

---

## 🧩 Objectives

1. **Task 1 – Git & Environment Setup**
   - Initialize version-controlled environment for reproducible analytics.
   - Implement GitHub Actions workflow to ensure CI.
   - Define a modular folder structure for analysis and reporting.

2. **Task 2 – Data Profiling, Cleaning & EDA**
   - Profile and clean raw solar datasets from Benin, Sierra Leone, and Togo.
   - Generate summary statistics, detect outliers, and explore relationships.
   - Evaluate cleaning effects on module performance.
   - Summarize comparative insights across all regions.


---

## 🏗️ Repository Structure
```bash
solar-challenge-week0/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data
│   └── cleaned/
│       ├── benin_clean.csv
│       ├── sierra_leone_clean.csv
│       └── togo_clean.csv
│
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sieraleone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   └── eda_visuals.py
│
├── app/
│   ├── __init__.py
│   ├── dashboard_screenshots
│   ├── main.py
│   └── utils.py
│
├── scripts/
│   ├── run_eda.py
│   └── README.md
│
├── tests/
│   └── test_cleaning.py
│
├── requirements.txt
├── .gitignore
└── README.md

```
---

## ⚙️ Environment Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/kalkidanzabreham/solar-challenge-week0.git
cd solar-challenge-week0
```

## Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```
## Install dependencies
```bash
pip install -r requirements.txt
To verify the setup, ensure the GitHub Actions workflow (.github/workflows/ci.yml) runs successfully upon each commit.
```

## 🧪 Reproducing the Cleaning Pipeline
Run the following to clean and export datasets automatically:

```bash
python scripts/run_eda.py
```

## 📊 Data Summary & Key Insights
| Metric | Benin | Sierra Leone | Togo |
|--------|--------|---------------|-------|
| Mean GHI (W/m²) | 240.34 | 196.44 | 229.83 |
| Mean DNI (W/m²) | 167.19 | 104.53 | 149.37 |
| Mean DHI (W/m²) | 110.9 | 110.11 | 112.4 |
| Mean Tamb (°C) | 28.18 | 26.32 | 27.75 |
| Corr(GHI,Tamb) | 0.548 | 0.643 | 0.563 |

**Highlights:**
- Benin shows the highest solar potential with consistent irradiance.  
- Sierra Leone has lower irradiance, influenced by humidity.  
- Togo’s strong cleaning effect suggests high maintenance sensitivity.

 ## 🧩 Code Modularity & Documentation

-The project follows a modular structure for better reusability and maintenance.
-Module-level docstrings are included across src/ scripts to explain functionality.
-Notebooks now import reusable functions from:
```bash
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.eda_visuals import plot_correlation_heatmap
```

3. Task 3 – Cross-Country Comparison

This stage focuses on comparing solar potential across Benin, Sierra Leone, and Togo using cleaned datasets.
The analysis highlights key metrics — GHI (Global Horizontal Irradiance), DNI (Direct Normal Irradiance), and DHI (Diffuse Horizontal Irradiance) — to determine which country demonstrates the highest potential for photovoltaic (PV) deployment.

🔍 Objectives
   - Merge and compare cleaned datasets from all three countries.
   - Compute and visualize summary statistics (mean, median, standard deviation).
   - Conduct statistical significance testing using the Kruskal–Wallis test.
   - Identify top-performing countries and discuss variability and potential solar performance risks.

### 📊 Outputs

| **Visualization** | **Description** |
|--------------------|-----------------|
| **Boxplots** | Side-by-side comparison of GHI, DNI, and DHI across countries. |
| **Summary Table** | Displays mean, median, and standard deviation of irradiance metrics for each country. |
| **Bar Chart** | Ranks countries by their average GHI to highlight solar potential. |
| **Statistical Test** | Kruskal–Wallis p-value used to determine whether differences between countries are statistically significant. |

## 💻 Streamlit Dashboard

An interactive dashboard was developed using Streamlit to visualize and explore the dataset dynamically.
It enables users to compare solar irradiance metrics across countries and interactively adjust visualizations.

🌐 Features
   - Country selection via sidebar widgets

   - Interactive boxplots and bar charts

   - Real-time data summary and ranking table

   - Clean and minimal UI design

▶️ Run the Streamlit Dashboard Locally

Activate your environment
```bash
conda activate solar_env
```
or
```bash
venv/Script/activate
```
Navigate to the app directory
```bash
cd app
```

Run Streamlit
```bash
streamlit run main.py
```

Open the link displayed in your terminal (usually http://localhost:8501) in your browser.


## 🤝 Contributing

Contributions are welcome!
If you’d like to improve or extend this project:

 Contributing
1. Clone the repo and create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Run tests before committing:
   ```bash
   pytest
   ```
4. Push your branch and open a Pull Request with a clear description of your changes.

## 🧾 References
- KIAM 10 Academy – Week 0 Challenge (2025)
- MoonLight Energy Solutions – Business Objective Document
- Solar Radiation Data – Aggregated from NOAA and Regional Measurement Systems

  


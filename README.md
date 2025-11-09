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
│ └── workflows/
│ └── ci.yml
│
├── data/
│ ├── benin_clean.csv
│ ├── sierra_leone_clean.csv
│ └── togo_clean.csv
│
├── notebooks/
│ ├── benin_eda.ipynb
│ ├── sierra_leone_eda.ipynb
│ └── togo_eda.ipynb
│
├── src/
│ └── utils/
│ ├── data_cleaning.py
│ └── visualization.py
│
├── scripts/
│ └── run_eda.py
│
├── tests/
│ └── test_cleaning.py
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

# Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```
# Install dependencies
```bash
pip install -r requirements.txt
To verify the setup, ensure the GitHub Actions workflow (.github/workflows/ci.yml) runs successfully upon each commit.
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

## 🧾 References
- KIAM 10 Academy – Week 0 Challenge (2025)
- MoonLight Energy Solutions – Business Objective Document
- Solar Radiation Data – Aggregated from NOAA and Regional Measurement Systems


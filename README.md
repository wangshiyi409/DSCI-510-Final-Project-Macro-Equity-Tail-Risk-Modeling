# DSCI 510 Final Project  
## Equity Tail-Risk Modeling Using Macro-Financial Data (FRED + Yahoo Finance)

### University of Southern California  
### DSCI 510: Principles of Programming for Data Science  
### Fall 2025  

---

## 🧑‍💻 Team Information
**Name:** Shiyi Wang  
**Email:** (your USC email)  
**USC ID:** (your USC ID)  
**GitHub Username:** (your GitHub username)

---

# DSCI 510 Final Project  
## Equity Tail-Risk Modeling Using Macro-Financial Data (FRED + Yahoo Finance)

### University of Southern California  
### DSCI 510: Principles of Programming for Data Science  
### Fall 2025  

---

## 👤 Student Information

**Name:** Shiyi Wang  
**USC Email:** (your USC email)  
**GitHub Username:** (your GitHub username)  

---

# 1. Project Overview

This project studies the relationship between **macroeconomic indicators**, **firm fundamentals**, and **equity tail-risk**, where tail-risk is defined as **maximum drawdown (MDD)** during a given period.

To accomplish this, the project implements an end-to-end data science pipeline:

- ✔ **FRED API** → collect macroeconomic time series  
- ✔ **Yahoo Finance (yfinance)** → collect stock prices & fundamentals  
- ✔ **Python ETL scripts** → clean & merge datasets  
- ✔ **Logistic Regression** → classify high-drawdown stocks  
- ✔ **Visualizations** → macro time series, scatter plots, correlation heatmap  

This project fulfills all DSCI 510 Final Project requirements:
- API/data scraping  
- Data cleaning  
- Exploratory data analysis  
- Machine learning modelling  
- Data visualization  
- Modular Python package structure (src/ folder)

---

# 2. Repository Structure

```text
.
├── README.md
├── requirements.txt
├── project_proposal.pdf
├── data/
│   ├── raw/
│   └── processed/
├── results/
│   ├── analysis_summary.txt
│   ├── macro_timeseries.png
│   ├── drawdown_hist.png
│   ├── roa_vs_drawdown.png
│   ├── profit_margin_vs_drawdown.png
│   ├── debt_to_assets_vs_drawdown.png
│   └── correlation_heatmap.png
└── src/
    ├── get_data.py
    ├── clean_data.py
    ├── run_analysis.py
    ├── visualize_results.py
    └── utils/
        ├── helpers.py
        ├── fred_api.py
        ├── yahoo_api.py
        └── indicators.py

...
```

---

# 3. Setup
Create a Python virtual environment

---

# 4.How to Run
## 4.1 Get Data
python -m src.get_data

This will download macro data from FRED and equity data from Yahoo Finance
and store them in data/raw/.
## 4.2 Clean Data
python -m src.clean_data

This will clean and merge the raw data and save the processed files to
data/processed/.
## 4.3 Run Analysis
python -m src.run_analysis

This will generate plots (PNG files) in the results/ directory.
## 4.4 Visualize Results
python -m src.visualize_results

This will generate plots (PNG files) in the results/ directory.





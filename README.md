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

# 1. Project Overview

This project examines how macroeconomic indicators and firm fundamentals relate to stock tail-risk, defined as maximum drawdown (MDD).  
We use:

- **FRED API** (macroeconomic data)  
- **Yahoo Finance API** (prices + fundamentals)  
- Modular Python scripts for ETL  
- Logistic Regression for classification  
- Visualizations for insights  

This project fulfills all DSCI 510 requirements:
✔ Data collection via web APIs  
✔ Data cleaning  
✔ Analysis  
✔ Visualization  
✔ Organized GitHub repo structure  

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
│   ├── correlation_heatmap.png
│   └── (other plots)
└── src/
    ├── get_data.py
    ├── clean_data.py
    ├── run_analysis.py
    ├── visualize_results.py
    └── utils/
        ├── fred_api.py
        ├── yahoo_api.py
        ├── indicators.py
        └── helpers.py

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





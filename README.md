# DSCI-510-Final-Project-Macro-Equity-Tail-Risk-Modeling
This project collects macroeconomic time series from FRED and firm-level equity data (prices and fundamentals) from Yahoo Finance. It then constructs features to study the relationship between financial indicators and maximum drawdown (tail risk) in U.S. equities.

## 🧑‍💻 Team Information
**Name:** Shiyi Wang  
**Email:** shiyiw@usc.edu
**USC ID:** 9862305589
**GitHub Username:** wangshiyi409

---

# 1. Project Overview

This project analyzes the relationship between **macroeconomic conditions**, **firm fundamentals**, and **equity tail-risk**, defined as **maximum drawdown (MDD)** over a specific quarter.

The project uses:
- **FRED API** – to collect U.S. macroeconomic indicators  
- **Yahoo Finance API** – to collect firm-level fundamentals & historical stock prices  
- **Python data pipeline** – for processing, cleaning, analysis, and visualization  
- **A simple logistic regression model** – to classify “high drawdown” equities  

This project demonstrates end-to-end data science workflow including:
✔ Web/API data collection  
✔ Data cleaning & preprocessing  
✔ Statistical analysis  
✔ Data visualization  
✔ Python modular structure  

---

# 2. Repository Structure

├── README.md
├── requirements.txt
├── project_proposal.pdf
├── data/
│ ├── raw/ # Raw FRED + Yahoo API data
│ └── processed/ # Cleaned & merged data
├── results/
│ ├── analysis_summary.txt
│ ├── macro_timeseries.png
│ ├── drawdown_hist.png
│ ├── correlation_heatmap.png
│ └── (other plots)
└── src/
├── get_data.py # Step 1: Fetch raw data
├── clean_data.py # Step 2: Data cleaning & merging
├── run_analysis.py # Step 3: Statistical analysis + logistic regression
├── visualize_results.py# Step 4: Visualization
└── utils/


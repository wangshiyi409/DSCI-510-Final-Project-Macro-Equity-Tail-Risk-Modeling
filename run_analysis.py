"""
run_analysis.py
Step 3: Statistical Analysis + Logistic Regression

This script:
1. Loads cleaned & merged data
2. Computes descriptive statistics
3. Creates a binary tail-risk label
4. Fits a logistic regression model
5. Saves analysis summary to results/analysis_summary.txt
"""

import pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from utils.helpers import get_data_dir


# ----------------------------------------------------
# Utility: write text data to results folder
# ----------------------------------------------------
def write_results(text: str, filename="analysis_summary.txt"):
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    out_path = results_dir / filename
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"[Saved] Analysis summary → {out_path}")


# ----------------------------------------------------
# Core analysis
# ----------------------------------------------------
def run_analysis():
    """
    Load merged dataset, create labels, run logistic regression,
    and output summary statistics.
    """
    print("\n[Step] Running analysis...")

    data_dir = get_data_dir()
    merged_path = data_dir / "processed" / "merged_panel.csv"

    df = pd.read_csv(merged_path)

    # ---------------------------------------------
    # 1. Tail-risk label (bottom 25% = high risk)
    # ---------------------------------------------
    df["tail_risk"] = (df["q2_max_drawdown"] <= df["q2_max_drawdown"].quantile(0.25)).astype(int)

    # ---------------------------------------------
    # 2. Select features (simple but useful)
    # ---------------------------------------------
    feature_cols = [
        "roa",
        "net_profit_margin",
        "debt_to_assets",
        "GDP",
        "CPIAUCSL",
        "UNRATE"
    ]

    X = df[feature_cols].copy()
    y = df["tail_risk"]

    # Remove rows with missing features
    non_missing = X.notna().all(axis=1)
    X = X[non_missing]
    y = y[non_missing]

    # ---------------------------------------------
    # 3. Logistic Regression Model
    # ---------------------------------------------
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    preds = model.predict(X)

    # ---------------------------------------------
    # 4. Prepare text summary
    # ---------------------------------------------
    text = "=== DSCI 510 Final Project: Analysis Summary ===\n\n"

    text += "Number of samples: {}\n".format(len(df))
    text += "Number after removing NaNs: {}\n\n".format(len(X))

    text += "=== Descriptive Statistics ===\n"
    text += df.describe(include="all").to_string()
    text += "\n\n"

    text += "=== Logistic Regression Report ===\n"
    text += classification_report(y, preds)
    text += "\n"

    coef_table = pd.DataFrame({
        "feature": feature_cols,
        "coefficient": model.coef_[0]
    })
    text += "=== Model Coefficients ===\n"
    text += coef_table.to_string(index=False)
    text += "\n"

    # ---------------------------------------------
    # 5. Save results
    # ---------------------------------------------
    write_results(text)


# ----------------------------------------------------
# Main execution
# ----------------------------------------------------
def main():
    print("\n=== Starting Statistical Analysis ===\n")
    run_analysis()
    print("\n=== Analysis Complete ===\n")


if __name__ == "__main__":
    main()

"""
clean_data.py
Step 2: Clean & Process Raw Data

This script performs:
1. Cleaning macroeconomic data (FRED)
2. Cleaning equity panel data (Yahoo Finance)
3. Merging macro + equity data into one final dataset

Outputs saved to:
    data/processed/macro_clean.csv
    data/processed/equity_clean.csv
    data/processed/merged_panel.csv
"""

import pandas as pd
from utils.helpers import get_data_dir


# ----------------------------------------------------
# 1. Clean Macroeconomic Data
# ----------------------------------------------------
def clean_macro_data():
    """
    Load raw FRED macro data, clean NaNs, resample to monthly,
    and save into data/processed/.
    """
    data_dir = get_data_dir()

    raw_path = data_dir / "raw" / "macro_raw.csv"
    out_path = data_dir / "processed" / "macro_clean.csv"

    print("\n[Step] Cleaning macroeconomic data...")

    macro_df = pd.read_csv(raw_path)

    # Ensure date column exists and parse it
    if "date" in macro_df.columns:
        macro_df["date"] = pd.to_datetime(macro_df["date"])
        macro_df.set_index("date", inplace=True)

    # Resample monthly (if daily) and forward fill
    macro_df = macro_df.resample("M").last().ffill()

    macro_df.to_csv(out_path)
    print(f"[Saved] Clean macro data → {out_path}")


# ----------------------------------------------------
# 2. Clean Equity Panel Data
# ----------------------------------------------------
def clean_equity_data():
    """
    Clean raw equity data downloaded from Yahoo Finance.
    Handle missing values, ensure numeric types, and save.
    """
    data_dir = get_data_dir()

    raw_path = data_dir / "raw" / "equity_raw.csv"
    out_path = data_dir / "processed" / "equity_clean.csv"

    print("\n[Step] Cleaning equity panel data...")

    df = pd.read_csv(raw_path)

    # Standard basic cleaning
    # Remove duplicate symbols if any
    df.drop_duplicates(subset=["symbol"], inplace=True)

    # Convert numeric columns except metadata
    numeric_cols = [
        "total_assets", "total_liabilities", "total_equity",
        "net_income", "total_revenue",
        "roa", "net_profit_margin", "debt_to_assets",
        "q2_return", "q2_max_drawdown"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows with missing drawdown (cannot analyze)
    df = df[df["q2_max_drawdown"].notna()]

    df.to_csv(out_path, index=False)
    print(f"[Saved] Clean equity data → {out_path}")


# ----------------------------------------------------
# 3. Merge Macro + Equity Data
# ----------------------------------------------------
def merge_macro_equity():
    """
    Attach macroeconomic indicators to each stock.

    Strategy:
    - Use the latest macro values (last available date)
    - Broadcast as additional columns to each stock row
    """
    data_dir = get_data_dir()

    macro_path = data_dir / "processed" / "macro_clean.csv"
    equity_path = data_dir / "processed" / "equity_clean.csv"
    out_path = data_dir / "processed" / "merged_panel.csv"

    print("\n[Step] Merging macro + equity data...")

    macro_df = pd.read_csv(macro_path)
    equity_df = pd.read_csv(equity_path)

    # Latest macro row (1 row)
    latest_macro = macro_df.iloc[[-1]].copy()

    # Add macro columns to each stock row
    for col in latest_macro.columns:
        if col != "date":
            equity_df[col] = latest_macro[col].iloc[0]

    equity_df.to_csv(out_path, index=False)
    print(f"[Saved] Final merged panel → {out_path}")


# ----------------------------------------------------
# Main Execution
# ----------------------------------------------------
def main():
    print("\n=== Starting Data Cleaning ===\n")

    clean_macro_data()
    clean_equity_data()
    merge_macro_equity()

    print("\n=== Data Cleaning Complete ===\n")


if __name__ == "__main__":
    main()

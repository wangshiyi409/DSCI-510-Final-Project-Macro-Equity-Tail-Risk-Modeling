"""
get_data.py
Step 1: Collect Raw Data (FRED + Yahoo Finance)

This script downloads:
1. Macroeconomic indicators from FRED
2. Stock price + fundamentals + drawdown metrics from Yahoo Finance

Raw data are saved into:
    data/raw/macro_raw.csv
    data/raw/equity_raw.csv
"""

import pandas as pd
from pathlib import Path

# Local utility imports
from utils.fred_api import FREDClient
from utils.yahoo_api import build_equity_panel
from utils.helpers import get_data_dir


# ------------------------------
# 1. Download Macro Data (FRED)
# ------------------------------
def download_macro_data():
    """
    Fetch macroeconomic indicators from FRED API.
    """
    data_dir = get_data_dir()
    raw_dir = data_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    fred_series = [
        "GDP",
        "CPIAUCSL",
        "UNRATE",
        "DGS3MO",
        "DGS10",
        "RSAFS",
        "HOUST"
    ]

    print("\n[Step] Downloading FRED macroeconomic series...")
    client = FREDClient()

    macro_df = client.fetch_series(
        series_ids=fred_series,
        start_date="2000-01-01",
        end_date="2025-12-31"
    )

    out_path = raw_dir / "macro_raw.csv"
    macro_df.to_csv(out_path)
    print(f"[Saved] FRED macro data → {out_path}")


# ----------------------------------------
# 2. Download Stock Panel (Yahoo Finance)
# ----------------------------------------
def download_equity_data():
    """
    Download firm fundamentals + Q2 price data + drawdowns.
    """

    data_dir = get_data_dir()
    raw_dir = data_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    # TODO: Replace with your full NASDAQ list
    symbols = [
        "AAPL", "MSFT", "GOOGL", "AMZN", "META"
    ]

    print("\n[Step] Downloading Yahoo Finance equity panel...")
    panel_df = build_equity_panel(
        symbols=symbols,
        price_start="2025-04-01",
        price_end="2025-06-30"
    )

    out_path = raw_dir / "equity_raw.csv"
    panel_df.to_csv(out_path, index=False)
    print(f"[Saved] Equity panel → {out_path}")


# ------------------------------
# Main Execution
# ------------------------------
def main():
    print("\n=== Starting Data Collection ===\n")
    download_macro_data()
    download_equity_data()
    print("\n=== Data Collection Complete ===\n")


if __name__ == "__main__":
    main()


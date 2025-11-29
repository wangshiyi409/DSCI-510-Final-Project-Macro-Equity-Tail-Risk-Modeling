"""
yahoo_api.py
Utility functions for downloading stock price data, fundamentals,
and constructing a clean equity panel DataFrame.
"""

import yfinance as yf
import pandas as pd
import numpy as np
from utils.indicators import compute_max_drawdown, compute_return


def fetch_financials(ticker):
    """
    Extract financial metrics from Yahoo Finance.
    """
    try:
        bs = ticker.balance_sheet
        fin = ticker.financials
    except:
        return {}

    result = {}

    def safe_extract(df, row_name):
        try:
            return df.loc[row_name].iloc[0]
        except:
            return np.nan

    result["total_assets"] = safe_extract(bs, "Total Assets")
    result["total_liabilities"] = safe_extract(bs, "Total Liab")
    result["total_equity"] = safe_extract(bs, "Total Stockholder Equity")
    result["net_income"] = safe_extract(fin, "Net Income")
    result["total_revenue"] = safe_extract(fin, "Total Revenue")

    # Derived ratios
    try:
        result["roa"] = result["net_income"] / result["total_assets"]
    except:
        result["roa"] = np.nan

    try:
        result["net_profit_margin"] = result["net_income"] / result["total_revenue"]
    except:
        result["net_profit_margin"] = np.nan

    try:
        result["debt_to_assets"] = result["total_liabilities"] / result["total_assets"]
    except:
        result["debt_to_assets"] = np.nan

    return result


def build_equity_panel(symbols, price_start="2025-04-01", price_end="2025-06-30"):
    """
    Download financial and price data for multiple symbols.
    Compute Q2 return + Q2 max drawdown.
    Output: DataFrame (one row per stock)
    """

    rows = []

    for sym in symbols:
        print(f"[Yahoo] Fetching {sym} ...")

        ticker = yf.Ticker(sym)

        # ---------- Prices ----------
        price_df = ticker.history(start=price_start, end=price_end)

        if price_df.empty:
            print(f"[Warning] No price data for {sym}")
            continue

        price_df = price_df.copy()
        price_df.index = price_df.index.strftime("%Y-%m-%d")

        try:
            start_price = price_df.loc[price_start, "Close"]
            end_price = price_df.loc[price_end, "Close"]
        except:
            start_price = None
            end_price = None

        q2_return = compute_return(start_price, end_price)
        q2_mdd = compute_max_drawdown(price_df["Close"])


        # ---------- Fundamentals ----------
        fin = fetch_financials(ticker)

        # ---------- Metadata ----------
        info = ticker.info or {}

        row = {
            "symbol": sym,
            "company_name": info.get("longName", ""),
            "sector": info.get("sector", ""),
            "industry": info.get("industry", ""),
            "market_cap": info.get("marketCap", None),
            "country": info.get("country", ""),
            "exchange": info.get("exchange", ""),

            # Prices
            "q2_return": q2_return,
            "q2_max_drawdown": q2_mdd,
        }

        row.update(fin)  # add financial metrics
        rows.append(row)

    return pd.DataFrame(rows)

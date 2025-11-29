"""
fred_api.py
Simple wrapper for downloading FRED macroeconomic data.
"""

import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # to read FRED_API_KEY from .env


class FREDClient:
    """
    Minimal FRED API client.
    """

    def __init__(self):
        self.api_key = os.getenv("FRED_API_KEY", "")
        self.url = "https://api.stlouisfed.org/fred/series/observations"

        if not self.api_key:
            print("[Warning] No FRED_API_KEY found in .env. Requests may be rate-limited.")

    def fetch_series(self, series_ids, start_date="2000-01-01", end_date="2025-12-31"):
        """
        Download multiple FRED series and combine into one DataFrame.
        """
        dfs = []

        for series in series_ids:
            print(f"[FRED] Fetching {series} ...")

            params = {
                "series_id": series,
                "api_key": self.api_key,
                "file_type": "json",
                "observation_start": start_date,
                "observation_end": end_date,
            }

            r = requests.get(self.url, params=params)
            data = r.json()

            if "observations" not in data:
                print(f"[Error] Unable to fetch {series}")
                continue

            obs = pd.DataFrame(data["observations"])
            obs["date"] = pd.to_datetime(obs["date"])
            obs[series] = pd.to_numeric(obs["value"], errors="coerce")
            obs = obs[["date", series]]

            dfs.append(obs)

        # merge on date
        if not dfs:
            return pd.DataFrame()

        out = dfs[0]
        for d in dfs[1:]:
            out = out.merge(d, on="date", how="outer")

        out = out.sort_values("date").reset_index(drop=True)
        return out

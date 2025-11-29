"""
indicators.py
Financial indicator helper functions:
- max drawdown
- quarterly return
"""

import pandas as pd
import numpy as np


def compute_max_drawdown(price_series):
    """
    Compute maximum drawdown from a price series.
    MDD = min(price / rolling max - 1).
    """
    if len(price_series) < 2:
        return np.nan

    rolling_max = price_series.cummax()
    drawdown = price_series / rolling_max - 1
    return drawdown.min()


def compute_return(start_price, end_price):
    """
    Simple return: (end - start) / start
    """
    if start_price is None or end_price is None:
        return np.nan
    try:
        return (end_price - start_price) / start_price
    except:
        return np.nan

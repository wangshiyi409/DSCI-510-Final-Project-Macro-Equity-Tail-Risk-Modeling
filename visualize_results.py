"""
visualize_results.py
Step 4: Generate visualizations for the DSCI 510 final project.

This script produces:
1. Macro indicator time series (4×2 subplot)
2. Maximum drawdown histogram
3. Scatter plots:
      - ROA vs Drawdown
      - Net Profit Margin vs Drawdown
      - Debt-to-Assets vs Drawdown
4. Correlation heatmap

All output PNGs are stored in: results/
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from utils.helpers import get_data_dir


# ----------------------------------------------------
# Ensure results directory exists
# ----------------------------------------------------
def ensure_results_dir():
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    return results_dir


# ----------------------------------------------------
# 1. Macro Time Series — 4×2 subplot
# ----------------------------------------------------
def plot_macro_time_series(macro_df, output_dir):
    features = [
        "GDP",
        "CPIAUCSL",
        "UNRATE",
        "DGS3MO",
        "DGS10",
        "RSAFS",
        "HOUST"
    ]

    macro_df = macro_df.set_index("date")
    macro_df.index = pd.to_datetime(macro_df.index)

    fig, axes = plt.subplots(4, 2, figsize=(16, 18))
    axes = axes.flatten()

    for ax, feature in zip(axes, features):
        if feature in macro_df.columns:
            macro_df[feature].plot(ax=ax, linewidth=1.8)
            ax.set_title(feature)
            ax.grid(True)

    # Remove empty last subplot if < 8 plots
    for ax in axes[len(features):]:
        fig.delaxes(ax)

    plt.tight_layout()
    fig.savefig(output_dir / "macro_timeseries.png", dpi=150)
    plt.close(fig)


# ----------------------------------------------------
# 2. Drawdown Histogram
# ----------------------------------------------------
def plot_drawdown_hist(equity_df, output_dir):
    fig = plt.figure(figsize=(8, 6))
    plt.hist(equity_df["q2_max_drawdown"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Distribution of Q2 Maximum Drawdown")
    plt.xlabel("Max Drawdown")
    plt.ylabel("Count")
    plt.grid(True)

    fig.savefig(output_dir / "drawdown_hist.png", dpi=150)
    plt.close(fig)


# ----------------------------------------------------
# 3. Scatter Plots
# ----------------------------------------------------
def scatter_plot(equity_df, x_col, y_col, title, fname, output_dir):
    fig = plt.figure(figsize=(8, 6))
    sns.scatterplot(data=equity_df, x=x_col, y=y_col)
    plt.title(title)
    plt.grid(True)

    fig.savefig(output_dir / fname, dpi=150)
    plt.close(fig)


# ----------------------------------------------------
# 4. Correlation Heatmap
# ----------------------------------------------------
def plot_correlation_heatmap(df, output_dir):
    corr_df = df[[
        "roa",
        "net_profit_margin",
        "debt_to_assets",
        "q2_max_drawdown"
    ]].dropna()

    fig = plt.figure(figsize=(8, 6))
    sns.heatmap(corr_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")

    fig.savefig(output_dir / "correlation_heatmap.png", dpi=150)
    plt.close(fig)


# ----------------------------------------------------
# Main Visualization Pipeline
# ----------------------------------------------------
def main():
    print("\n=== Starting Visualization ===\n")

    data_dir = get_data_dir()
    results_dir = ensure_results_dir()

    macro_df = pd.read_csv(data_dir / "processed" / "macro_clean.csv")
    equity_df = pd.read_csv(data_dir / "processed" / "equity_clean.csv")

    # 1. Macro time series
    print("[Plot] Macro Time Series")
    plot_macro_time_series(macro_df, results_dir)

    # 2. Drawdown histogram
    print("[Plot] Drawdown Histogram")
    plot_drawdown_hist(equity_df, results_dir)

    # 3. Scatter plots
    print("[Plot] Scatter: ROA vs Drawdown")
    scatter_plot(
        equity_df, "roa", "q2_max_drawdown",
        "ROA vs Maximum Drawdown",
        "roa_vs_drawdown.png", results_dir
    )

    print("[Plot] Scatter: Net Profit Margin vs Drawdown")
    scatter_plot(
        equity_df, "net_profit_margin", "q2_max_drawdown",
        "Net Profit Margin vs Maximum Drawdown",
        "profit_margin_vs_drawdown.png", results_dir
    )

    print("[Plot] Scatter: Debt-to-Assets vs Drawdown")
    scatter_plot(
        equity_df, "debt_to_assets", "q2_max_drawdown",
        "Debt-to-Assets vs Maximum Drawdown",
        "debt_to_assets_vs_drawdown.png", results_dir
    )

    # 4. Correlation heatmap
    print("[Plot] Correlation Heatmap")
    plot_correlation_heatmap(equity_df, results_dir)

    print("\n=== Visualization Complete ===\n")


if __name__ == "__main__":
    main()

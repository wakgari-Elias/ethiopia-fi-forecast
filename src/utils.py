# src/utils.py
import pandas as pd
import os
import matplotlib.pyplot as plt

# Absolute paths based on project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENRICHED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "ethiopia_fi_unified_data_enriched.xlsx")
FORECAST_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "ethiopia_fi_unified_data_enriched.xlsx")  # replace with your forecast file

def load_enriched_data():
    """Load enriched dataset"""
    if not os.path.exists(ENRICHED_DATA_PATH):
        raise FileNotFoundError(f"Enriched dataset not found at {ENRICHED_DATA_PATH}")
    return pd.read_excel(ENRICHED_DATA_PATH, sheet_name="Sheet1")

def load_forecast_data():
    """Load forecast dataset"""
    if not os.path.exists(FORECAST_DATA_PATH):
        raise FileNotFoundError(f"Forecast dataset not found at {FORECAST_DATA_PATH}")
    return pd.read_excel(FORECAST_DATA_PATH)

def plot_indicator_trend(df, indicator_code, title):
    """Return a matplotlib figure of the indicator trend"""
    fig, ax = plt.subplots(figsize=(10, 5))
    df_indicator = df[df['indicator_code'] == indicator_code].sort_values("year")
    ax.plot(df_indicator['year'], df_indicator['value_numeric'], marker='o')
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel("Value")
    ax.grid(True)
    return fig

def compute_crossover_ratio(df):
    """Compute P2P/ATM crossover ratio"""
    df = df.copy()
    df['crossover_ratio'] = df['USG_P2P_VALUE'] / df['USG_ATM_VALUE']
    return df[['year', 'crossover_ratio']]

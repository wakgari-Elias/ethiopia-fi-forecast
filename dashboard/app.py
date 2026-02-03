# dashboard/app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ===========================
# CONFIG
# ===========================
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide"
)

st.title("🇪🇹 Ethiopia Financial Inclusion Dashboard")

# ===========================
# DATA LOADING (ROBUST)
# ===========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "ethiopia_fi_unified_data_enriched.xlsx"
)

if not os.path.exists(DATA_PATH):
    st.error(f"Dataset not found at:\n{DATA_PATH}")
    st.stop()

df = pd.read_excel(DATA_PATH, sheet_name="Sheet1")

# ===========================
# BASIC CLEANING
# ===========================
df["observation_date"] = pd.to_datetime(df["observation_date"], errors="coerce")

if "year" not in df.columns:
    df["year"] = df["observation_date"].dt.year

obs = df[df["record_type"] == "observation"].copy()

# ===========================
# SIDEBAR
# ===========================
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Trends", "Forecasts", "Inclusion Projections"]
)

# ===========================
# OVERVIEW PAGE
# ===========================
if page == "Overview":

    st.header("Overview")

    col1, col2, col3 = st.columns(3)

    # ---- Account Ownership ----
    acc_latest = (
        obs[obs["indicator_code"] == "ACC_OWNERSHIP"]
        .sort_values("year")
        .tail(1)
    )

    with col1:
        if acc_latest.empty:
            st.metric("Account Ownership (Latest)", "N/A")
        else:
            st.metric(
                "Account Ownership (Latest)",
                f"{acc_latest['value_numeric'].iloc[0]}%",
                f"Year {int(acc_latest['year'].iloc[0])}"
            )

    # ---- Digital Payment Usage ----
    usg_latest = (
        obs[obs["indicator_code"] == "USG_DIGITAL_PAYMENT"]
        .sort_values("year")
        .tail(1)
    )

    with col2:
        if usg_latest.empty:
            st.metric("Digital Payment Usage (Latest)", "N/A")
        else:
            st.metric(
                "Digital Payment Usage (Latest)",
                f"{usg_latest['value_numeric'].iloc[0]}%",
                f"Year {int(usg_latest['year'].iloc[0])}"
            )

    # ---- P2P / ATM Crossover ----
    crossover = obs[obs["indicator_code"] == "USG_CROSSOVER"]

    with col3:
        if crossover.empty:
            st.metric("P2P > ATM Crossover", "N/A")
        else:
            st.metric(
                "P2P > ATM Crossover",
                int(crossover.sort_values("year")["year"].iloc[-1])
            )

    st.subheader("Dataset Summary")
    st.dataframe(
        df.groupby(["record_type", "pillar"])
        .size()
        .reset_index(name="count")
    )

# ===========================
# TRENDS PAGE
# ===========================
elif page == "Trends":

    st.header("Indicator Trends")

    indicator = st.selectbox(
        "Select Indicator",
        sorted(obs["indicator_code"].unique())
    )

    trend_data = (
        obs[obs["indicator_code"] == indicator]
        .groupby("year")["value_numeric"]
        .mean()
    )

    if trend_data.empty:
        st.warning("No data available for this indicator.")
    else:
        fig, ax = plt.subplots()
        trend_data.plot(marker="o", ax=ax)
        ax.set_xlabel("Year")
        ax.set_ylabel("Value")
        ax.set_title(indicator)
        st.pyplot(fig)

# ===========================
# FORECASTS PAGE
# ===========================
elif page == "Forecasts":

    st.header("Simple Forecasts (Trend-Based)")

    target = st.selectbox(
        "Select Target",
        ["ACC_OWNERSHIP", "USG_DIGITAL_PAYMENT"]
    )

    hist = (
        obs[obs["indicator_code"] == target]
        .groupby("year")["value_numeric"]
        .mean()
        .reset_index()
    )

    if hist.shape[0] < 3:
        st.warning("Not enough historical data to generate a forecast.")
    else:
        x = hist["year"].values
        y = hist["value_numeric"].values

        coef = np.polyfit(x, y, 1)
        trend = np.poly1d(coef)

        future_years = np.array([2025, 2026, 2027])
        forecast = trend(future_years)

        fig, ax = plt.subplots()
        ax.plot(x, y, marker="o", label="Historical")
        ax.plot(future_years, forecast, marker="o", linestyle="--", label="Forecast")
        ax.set_xlabel("Year")
        ax.set_ylabel("Percentage")
        ax.set_title(f"{target} Forecast")
        ax.legend()
        st.pyplot(fig)

        st.subheader("Forecast Table")
        st.dataframe(
            pd.DataFrame({
                "Year": future_years,
                "Forecast (%)": np.round(forecast, 2)
            })
        )

# ===========================
# INCLUSION PROJECTIONS PAGE
# ===========================
elif page == "Inclusion Projections":

    st.header("Progress Toward 60% Financial Inclusion Target")

    acc_series = (
        obs[obs["indicator_code"] == "ACC_OWNERSHIP"]
        .groupby("year")["value_numeric"]
        .mean()
    )

    if acc_series.empty:
        st.warning("No Account Ownership data available.")
    else:
        latest_value = acc_series.iloc[-1]
        gap = max(0, 60 - latest_value)

        st.metric("Current Inclusion Rate", f"{latest_value}%")
        st.metric("Gap to 60% Target", f"{gap}%")

        fig, ax = plt.subplots()
        acc_series.plot(marker="o", ax=ax)
        ax.axhline(60, linestyle="--", color="red", label="60% Target")
        ax.set_title("Account Ownership vs Target")
        ax.set_xlabel("Year")
        ax.set_ylabel("Percentage")
        ax.legend()
        st.pyplot(fig)

# ===========================
# FOOTER
# ===========================
st.caption("Task 5 — Interactive Dashboard for Ethiopia Financial Inclusion")

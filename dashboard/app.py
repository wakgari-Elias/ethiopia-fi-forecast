# dashboard/app.py
import streamlit as st
import pandas as pd
from src.utils import load_enriched_data, load_forecast_data, plot_indicator_trend, compute_crossover_ratio
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

st.set_page_config(page_title="Ethiopia Financial Inclusion Dashboard", layout="wide")

st.title("📊 Ethiopia Financial Inclusion Dashboard (Access & Usage)")

# --- Load Data ---
try:
    enriched_data = load_enriched_data()
    forecast_data = load_forecast_data()
except FileNotFoundError as e:
    st.error(str(e))
    st.stop()

# --- Overview Page ---
st.header("Overview Metrics")
access_latest = enriched_data[enriched_data['indicator_code']=="ACC_OWNERSHIP"]['value_numeric'].iloc[-1]
usage_latest = enriched_data[enriched_data['indicator_code']=="USG_DIGITAL_PAYMENT"]['value_numeric'].iloc[-1]
st.metric(label="Account Ownership (Access)", value=f"{access_latest:.2f}%")
st.metric(label="Digital Payment Usage (Usage)", value=f"{usage_latest:.2f}%")

# Compute P2P/ATM Crossover Ratio
if 'USG_P2P_VALUE' in enriched_data.columns and 'USG_ATM_VALUE' in enriched_data.columns:
    crossover_df = compute_crossover_ratio(enriched_data)
    st.subheader("📈 P2P/ATM Crossover Ratio")
    st.line_chart(crossover_df.set_index('year')['crossover_ratio'])

# --- Trends Page ---
st.header("Indicator Trends")
selected_indicator = st.selectbox("Select indicator to view trend", enriched_data['indicator_code'].unique())
fig = plot_indicator_trend(enriched_data, selected_indicator, f"{selected_indicator} Trend")
st.pyplot(fig)

# --- Forecasts Page ---
st.header("Forecasts (2025-2027)")
st.dataframe(forecast_data)  # show full forecast table
st.line_chart(forecast_data.set_index('year')[['ACC_OWNERSHIP', 'USG_DIGITAL_PAYMENT']])

# --- Download data button ---
st.download_button(
    label="Download Enriched Data",
    data=enriched_data.to_csv(index=False).encode('utf-8'),
    file_name='ethiopia_fi_enriched.csv',
    mime='text/csv'
)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Energy Consumption Monitor",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ICON MAPPING (Industrial Look) ---
ICONS = {
    "Voltage": "https://openmoji.org/data/color/svg/26A1.svg",      # Bolt
    "Consumption": "https://openmoji.org/data/color/svg/1F3D2.svg", # Factory
    "Solar": "https://openmoji.org/data/color/svg/2600.svg",       # Sun
    "Alert": "https://openmoji.org/data/color/svg/26A0.svg"        # Warning
}

# --- SIDEBAR (Project Details) ---
st.sidebar.image(ICONS["Voltage"], width=80)
st.sidebar.title("System Control")
st.sidebar.info("Graduation Project: Energy Consumption Analysis")

# Simulation toggle (since we don't have the live DB connected yet)
data_source = st.sidebar.selectbox("Data Source", ["Simulation Mode", "Live Database (Disconnected)"])

# --- DASHBOARD HEADER ---
st.title("⚡ Energy Monitoring System Dashboard")
st.write(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# --- TOP METRICS ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image(ICONS["Consumption"], width=40)
    st.metric("Total Load", "145.8 kWh", delta="+4.2%")

with col2:
    st.image(ICONS["Voltage"], width=40)
    st.metric("Phase Voltage", "231V", delta="Stable", delta_color="normal")

with col3:
    st.image(ICONS["Solar"], width=40)
    st.metric("Renewable Input", "12.5 kW", delta="-1.5%")

with col4:
    st.image(ICONS["Alert"], width=40)
    st.metric("Active Alerts", "0", delta="Normal")

st.write("---")

# --- MAIN CHARTS ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📈 Real-time Load Profile")
    # Mock data for the chart
    chart_data = pd.DataFrame({
        'Time': pd.date_range(start='2026-05-07', periods=24, freq='H'),
        'Usage (kWh)': np.random.randint(80, 160, size=24)
    })
    fig = px.area(chart_data, x='Time', y='Usage (kWh)', color_discrete_sequence=['#00CC96'])
    fig.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("📊 Consumption by Sector")
    sector_data = pd.DataFrame({
        'Sector': ['Industrial', 'Residential', 'Commercial', 'Public'],
        'Value': [45, 25, 20, 10]
    })
    fig_pie = px.pie(sector_data, values='Value', names='Sector', hole=0.4,
                     color_discrete_sequence=px.colors.sequential.Greens_r)
    fig_pie.update_layout(template="plotly_dark", showlegend=False)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- SYSTEM LOGS ---
st.write("---")
st.subheader("📋 System Event Logs")
logs = [
    {"Time": "02:10:05", "Event": "Database Handshake Initiated", "Status": "Success"},
    {"Time": "02:05:12", "Event": "Peak Load Threshold Adjusted", "Status": "Updated"},
    {"Time": "01:55:00", "Event": "Sensor Node 4 Connectivity", "Status": "Stable"}
]
st.table(logs)
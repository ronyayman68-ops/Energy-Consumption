import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# --- SETTINGS & THEME ---
st.set_page_config(page_title="Industrial Energy Monitor", layout="wide")

# Industrial Icon Assets
ICONS = {
    "Main": "https://openmoji.org/data/color/svg/26A1.svg",
    "Factory": "https://openmoji.org/data/color/svg/1F3ED.svg",
    "Analytics": "https://openmoji.org/data/color/svg/1F4C8.svg",
    "Control": "https://openmoji.org/data/color/svg/1F39B.svg"
}

# --- HEADER ---
st.title("⚡ Energy Management System (EMS)")
st.subheader("Real-time Industrial Consumption Analytics")
st.write(f"**System Status:** Running | **Last Sync:** {datetime.now().strftime('%H:%M:%S')}")

# --- TOP KPI DASHBOARD ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Active Load", "420.5 kW", "12%")
c2.metric("Daily Avg", "380.2 kW", "-2%")
c3.metric("Peak Demand", "510.0 kW", "Normal", delta_color="off")
c4.metric("Cost Est.", "$1,240", "$45")

st.divider()

# --- MAIN ANALYTICS SECTION ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📈 Load Profile (24h Window)")
    # Simulating data flow
    data = pd.DataFrame({
        'Time': pd.date_range(start=datetime.now(), periods=24, freq='H'),
        'Usage': np.random.randint(300, 500, size=24)
    })
    fig = px.line(data, x='Time', y='Usage', markers=True, template="plotly_dark")
    fig.update_traces(line_color='#00ffcc')
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("🎮 Control Center")
    st.write("Simulate Hardware Control:")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🔴 Stop Turbines", use_container_width=True):
            st.error("Turbines Halted")
    with col_b:
        if st.button("🟢 Start Solar Array", use_container_width=True):
            st.success("Solar Grid Active")
            
    st.write("---")
    st.write("**Alert Thresholds**")
    st.slider("Set Max Load Alert (kW)", 100, 1000, 600)

# --- DATABASE LOGS MOCKUP ---
st.subheader("📋 Recent Database Logs")
logs = pd.DataFrame([
    ["02:14:01", "Sensor_A1", "Voltage Spike Detected", "Warning"],
    ["02:10:45", "System", "Auto-Backup Successful", "Normal"],
    ["01:55:22", "Sensor_B4", "Database Connection Established", "Success"]
], columns=["Timestamp", "Node", "Message", "Level"])
st.table(logs)
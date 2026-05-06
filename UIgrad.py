import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="Energy Intelligence Dashboard", layout="wide")

# --- HEADER & STATUS ---
st.title("🔋 Smart Energy Analytics Platform")
st.write("Graduation Project | Technical Demo Phase")

with st.container():
    c1, c2, c3 = st.columns([1, 1, 1])
    c1.info("📡 **Gateway:** Connected")
    c2.success("🗄️ **Database:** Handshake Active")
    c3.warning("⚡ **Grid Load:** High Demand")

st.divider()

# --- REAL-TIME METRICS ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Consumption", "1,245 kWh", "4.5%")
m2.metric("Peak Power", "85.2 kW", "-2.1%")
m3.metric("Cost Accrued", "$452.10", "$12.05")
m4.metric("Co2 Footprint", "0.85 Tons", "Stable")

# --- DATA VISUALIZATION (Using Native Streamlit Charts) ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📈 Consumption Profile (Native Line Chart)")
    # Simulating data flow
    chart_data = pd.DataFrame(
        np.random.randn(24, 1) / [5] + [0.5],
        columns=['kWh Usage']
    )
    # This chart is built-in to Streamlit! No Plotly needed.
    st.line_chart(chart_data)

with right_col:
    st.subheader("⚙️ Control Panel")
    st.write("Adjust Simulation Parameters:")
    sim_speed = st.select_slider("Data Refresh Frequency", options=["Slow", "Normal", "Real-time"])
    
    st.write("---")
    if st.button("🚨 Emergency Load Shedding", use_container_width=True):
        st.error("Protocol Initiated: Reducing non-essential consumption.")
    
    if st.toggle("Enable AI Forecasting"):
        st.info("✨ AI Model is analyzing trends...")

# --- DATA TABLES & LOGS ---
st.write("---")
st.subheader("📜 Recent Activity Logs")
log_data = pd.DataFrame({
    'Timestamp': [datetime.now().strftime("%H:%M:%S") for _ in range(3)],
    'Module': ['Sensor_Node_04', 'Cloud_Sync', 'Auth_System'],
    'Message': ['Voltage anomaly detected', 'Data packet transmitted', 'User admin logged in'],
    'Priority': ['High', 'Normal', 'Low']
})
st.dataframe(log_data, use_container_width=True, hide_index=True)
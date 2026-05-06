import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="Energy Intelligence Dashboard", layout="wide")

# Styling for a modern "Dark Industrial" look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

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
m1.metric("Total Consumption", "1,245 kWh", "4.5%", help="Aggregated load across all sensors")
m2.metric("Peak Power", "85.2 kW", "-2.1%", delta_color="inverse")
m3.metric("Cost Accrued", "$452.10", "$12.05")
m4.metric("Co2 Footprint", "0.85 Tons", "Stable")

# --- DATA VISUALIZATION AREA ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📊 Consumption Profile (Last 24 Hours)")
    # Simulating a dynamic data stream
    df = pd.DataFrame({
        'Time': pd.date_range(start=datetime.now(), periods=24, freq='H'),
        'Value': np.random.randint(40, 100, size=24)
    })
    fig = px.area(df, x='Time', y='Value', template="plotly_dark", color_discrete_sequence=['#00f2ff'])
    fig.update_layout(xaxis_title=None, yaxis_title="kW/h")
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("⚙️ Control Panel")
    st.write("Adjust Simulation Parameters:")
    sim_speed = st.select_slider("Data Refresh Frequency", options=["Slow", "Normal", "Real-time"])
    
    st.write("---")
    st.write("Manual Overrides:")
    if st.button("🚨 Emergency Load Shedding", use_container_width=True):
        st.error("Protocol Initiated: Reducing non-essential consumption.")
    
    if st.toggle("Enable AI Forecasting"):
        st.write("✨ AI Model is analyzing historical trends...")

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
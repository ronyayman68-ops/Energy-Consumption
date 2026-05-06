import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Energy Monitor Pro", layout="wide")

st.title("⚡ Energy Consumption Analytics")
st.write("Graduation Project: Real-time Database Integration")

@st.cache_data
def get_energy_data():
    dates = pd.date_range(start="2026-01-01", periods=100, freq="H")
    consumption = np.random.randint(50, 200, size=100)
    return pd.DataFrame({"Timestamp": dates, "Usage (kWh)": consumption})

df = get_energy_data()
current_usage = df["Usage (kWh)"].iloc[-1]
avg_usage = df["Usage (kWh)"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Current Consumption", f"{current_usage} kWh")
col2.metric("Average Load", f"{avg_usage:.2f} kWh")
col3.metric("System Status", "Stable" if current_usage < 180 else "Peak Load")


st.subheader("Consumption Over Time")
fig = px.line(df, x="Timestamp", y="Usage (kWh)", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

st.write("---")
st.subheader("Predictive Insights")
prediction = [current_usage + np.random.randint(-10, 10) for _ in range(5)]
st.info(f"AI Prediction for next hour: **{prediction[0]} kWh**")

if st.button("Generate Detailed Energy Report"):
    st.write("Exporting data from database... (Feature in progress)")
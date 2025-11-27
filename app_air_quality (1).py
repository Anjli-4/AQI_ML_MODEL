import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import random

# ---------------------------
# 🎨 App Header
# ---------------------------
st.set_page_config(page_title="Air Quality Prediction", page_icon="🌤️", layout="centered")
st.header("🌤️ Air Quality Prediction Using Machine Learning")

st.markdown("""
### 🧠 Project Overview
Air pollution has become one of the major global concerns affecting human health and the environment.
This interactive tool uses a **Machine Learning model** to predict the **Air Quality Index (AQI)** based on
various air pollutants like PM2.5, PM10, NO, NO₂, CO, SO₂, and O₃.

The app helps you understand how changes in pollution levels affect overall air quality.
""")

st.image("https://www.shutterstock.com/image-vector/air-quality-index-aqi-measurement-600nw-2418628893.jpg")

# ---------------------------
# 🧩 Load Trained Model
# ---------------------------
try:
    with open('air_quality_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("⚠️ Model file 'air_quality_model.pkl' not found. Please upload or save the trained model first.")
    st.stop()

# ---------------------------
# 🧮 Sidebar Inputs
# ---------------------------
st.sidebar.image("https://png.pngtree.com/png-vector/20220609/ourlarge/pngtree-colorcoded-air-quality-index-poster-design-female-hazardous-global-warming-vector-png-image_37156516.jpg")
st.sidebar.header(" Enter Air Pollutant Levels")
st.sidebar.markdown("Adjust the sliders below to simulate different air conditions.")

pollutants = {
    "PM2.5": st.sidebar.slider("PM2.5 (μg/m³)", 0, 500, 60),
    "PM10": st.sidebar.slider("PM10 (μg/m³)", 0, 600, 80),
    "NO": st.sidebar.slider("NO (μg/m³)", 0, 200, 25),
    "NO2": st.sidebar.slider("NO₂ (μg/m³)", 0, 200, 40),
    "CO": st.sidebar.slider("CO (mg/m³)", 0.0, 10.0, 2.0),
    "SO2": st.sidebar.slider("SO₂ (μg/m³)", 0, 200, 15),
    "O3": st.sidebar.slider("O₃ (μg/m³)", 0, 200, 30),
}

input_values = np.array([[v for v in pollutants.values()]])

# ---------------------------
# 🔍 Prediction Button
# ---------------------------
if st.button("🔎 Predict Air Quality"):
    placeholder = st.empty()
    placeholder.subheader("Analyzing Air Data... 🌬️")

    with st.spinner("Processing your input..."):
        for i in range(50):
            time.sleep(0.03)

    predicted_aqi = model.predict(input_values)[0]
    placeholder.empty()

    # ---------------------------
    # 🎨 AQI Category
    # ---------------------------
    if predicted_aqi <= 50:
        category, color, emoji = "Good", "🟢", "😊"
    elif predicted_aqi <= 100:
        category, color, emoji = "Moderate", "🟡", "😐"
    elif predicted_aqi <= 200:
        category, color, emoji = "Poor", "🟠", "😷"
    elif predicted_aqi <= 300:
        category, color, emoji = "Very Poor", "🔴", "🤢"
    else:
        category, color, emoji = "Severe", "🟣", "😵‍💫"

    st.success(f"### {emoji} Predicted AQI: {predicted_aqi:.2f}")
    st.markdown(f"### {color} Air Quality Category: **{category}**")

    st.progress(min(int(predicted_aqi/5), 100))

    st.markdown("""
    | AQI Range | Category | Color |
    |------------|-----------|--------|
    | 0-50 | Good | 🟢 |
    | 51-100 | Moderate | 🟡 |
    | 101-200 | Poor | 🟠 |
    | 201-300 | Very Poor | 🔴 |
    | 301+ | Severe | 🟣 |
    """)

st.markdown("---")
st.markdown("👩‍💻 Designed by **Anjali 🌸**")

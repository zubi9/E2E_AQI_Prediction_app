import streamlit as st
import joblib
import pandas as pd
import hopsworks

# Load Model from Hopsworks
project = hopsworks.login()
mr = project.get_model_registry()
model = joblib.load(mr.get_model("AQI_Predictor", version=1).download())

# Streamlit UI
st.title("🌍 AQI Prediction Webapp")

# User Inputs
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50)
wind_speed = st.number_input("Wind Speed (m/s)", min_value=0, max_value=30, value=5)

# Predict
if st.button("Predict AQI"):
    df = pd.DataFrame([[temperature, humidity, wind_speed]], columns=["temperature", "humidity", "wind_speed"])
    prediction = model.predict(df)
    st.success(f"Predicted AQI: {prediction[0]:.2f}")

import streamlit as st
import joblib
import os
import hopsworks
import pandas as pd

# Connect to Hopsworks
project = hopsworks.login()
mr = project.get_model_registry()

# Get Model Directory
model_dir = mr.get_model("AQI_Predictor", version=1).download()

# Find Model File inside the Directory
model_path = os.path.join(model_dir, "aqi_model.pkl")  # Update if the filename is different

# Load Model
model = joblib.load(model_path)

# Streamlit UI
st.title("🌍 AQI Prediction Webapp")

st.markdown("""
### About the Air Quality Levels

| AQI Range  | Air Pollution Level               | Health Implications                                      | Cautionary Statement (for PM2.5) |
|------------|----------------------------------|--------------------------------------------------------|----------------------------------|
| 0 - 50    | **Good**                         | Air quality is considered satisfactory, and air pollution poses little or no risk. | None |
| 51 - 100  | **Moderate**                     | Air quality is acceptable; however, for some pollutants, there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution. | Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion. |
| 101 - 150 | **Unhealthy for Sensitive Groups** | Members of sensitive groups may experience health effects. The general public is not likely to be affected. | Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion. |
| 151 - 200 | **Unhealthy**                     | Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects. | Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion. |
| 201 - 300 | **Very Unhealthy**                | Health warnings of emergency conditions. The entire population is more likely to be affected. | Active children and adults, and people with respiratory disease, such as asthma, should avoid all outdoor exertion; everyone else, especially children, should limit outdoor exertion. |
| 300+      | **Hazardous**                     | Health alert: everyone may experience more serious health effects. | Everyone should avoid all outdoor exertion. |
""")

# User Inputs
st.header("Enter Environmental Conditions")
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=50)
wind_speed = st.number_input("Wind Speed (m/s)", min_value=0, max_value=30, value=5)

# Predict
if st.button("Predict AQI"):
    df = pd.DataFrame([[temperature, humidity, wind_speed]], columns=["temperature", "humidity", "wind_speed"])
    prediction = model.predict(df)
    st.success(f"Predicted AQI: {prediction[0]:.2f}")

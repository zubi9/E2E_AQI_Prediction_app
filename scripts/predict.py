import joblib
import pandas as pd

# Load the trained model
model = joblib.load("../models/aqi_model.pkl")

# Example input data for prediction
# Replace these values with actual input data
input_data = {
    "temperature": [25.0],  # Example temperature in Celsius
    "humidity": [60.0],     # Example humidity in percentage
    "wind_speed": [5.0]     # Example wind speed in m/s
}

# Convert input data to a DataFrame
input_df = pd.DataFrame(input_data)

# Predict using the loaded model
predicted_aqi = model.predict(input_df)

# Output the prediction
print(f"Predicted AQI: {predicted_aqi[0]}")
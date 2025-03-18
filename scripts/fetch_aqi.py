import requests
import pandas as pd
import hopsworks
from datetime import datetime

# API key for AQICN (Replace with your own)
API_KEY = "6242a9709ab7ff7d351d47ec21ff27a1833f2508"
CITY = "hamburg"
API_URL = f"https://api.waqi.info/feed/{CITY}/?token={API_KEY}"

def fetch_data():
    """Fetch AQI and weather data from API."""
    response = requests.get(API_URL)
    data = response.json()
    
    if "data" not in data:
        raise Exception("API response error:", data)

    aqi = data["data"]["aqi"]
    weather = data["data"]["iaqi"]
    
    return {
        "timestamp": datetime.now().isoformat(),
        "aqi": aqi,
        "temperature": weather.get("t", {}).get("v", None),
        "humidity": weather.get("h", {}).get("v", None),
        "wind_speed": weather.get("w", {}).get("v", None)
    }

# Fetch Data
data = fetch_data()
df = pd.DataFrame([data])

# Print Preview
print(df.head())


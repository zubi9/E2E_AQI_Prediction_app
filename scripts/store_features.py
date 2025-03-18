import hopsworks
import pandas as pd

project = hopsworks.login()
fs = project.get_feature_store()

# Load features
df = pd.read_csv("../data/historical_aqi.csv")  # Assume `fetch_aqi.py` saves a file

# Define Feature Group
feature_group = fs.get_or_create_feature_group(
    name="aqi_features",
    version=1,
    description="Features for AQI prediction",
    primary_key=["timestamp"],
    online_enabled=True
)

# Store Data
feature_group.insert(df)

print("Data stored in Feature Store successfully!")

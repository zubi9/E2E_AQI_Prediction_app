import hopsworks
import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

# Connect to Hopsworks
project = hopsworks.login()
fs = project.get_feature_store()

# Load historical features
feature_group = fs.get_feature_group("aqi_features", version=1)
df = feature_group.read()

# Prepare Data
X = df[["temperature", "humidity", "wind_speed"]]
y = df["aqi"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Model MAE: {mae}")

# Save Model
joblib.dump(model, "../models/aqi_model.pkl")

# Store Model in Hopsworks
mr = project.get_model_registry()
aqi_model = mr.sklearn.create_model(name="AQI_Predictor", metrics={"mae": mae})
aqi_model.save("../models/aqi_model.pkl")

print("Model saved in Hopsworks!")

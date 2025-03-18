import pandas as pd
from datetime import datetime, timedelta
from fetch_aqi import fetch_data

start_date = datetime.now() - timedelta(days=180)  # 6 months
dates = [start_date + timedelta(days=i) for i in range(180)]

historical_data = []
for date in dates:
    data = fetch_data()
    data["timestamp"] = date.isoformat()
    historical_data.append(data)

df = pd.DataFrame(historical_data)
df.to_csv("../data/historical_aqi.csv", index=False)

print("Historical data saved!")

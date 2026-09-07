"""
CampusAI EnergyWise - prototype.
The supplied CSV is synthetic demonstration data, not real campus data.
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("sample_campus_energy_data.csv")
df["day_of_week"] = pd.to_datetime(df["date"]).dt.dayofweek
df["building_code"] = df["building"].astype("category").cat.codes

features = ["building_code", "occupancy_pct", "temperature_c", "day_of_week"]
X, y = df[features], df["energy_kwh"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model = RandomForestRegressor(n_estimators=150, max_depth=8, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("MAE:", round(mean_absolute_error(y_test, pred), 2), "kWh")
print("R2 :", round(r2_score(y_test, pred), 3))

def recommend(row):
    actions=[]
    if row["occupancy_pct"] < 35:
        actions.append("Review non-essential lighting/HVAC schedules.")
    if row["temperature_c"] > 30:
        actions.append("Review cooling schedules and set-points.")
    if row["building"] == "Laboratory Block":
        actions.append("Review laboratory equipment standby/shutdown procedures.")
    actions.append("Validate any action with facility policy and human review.")
    return actions

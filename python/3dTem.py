import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. আপনার লোকেশন সেট করুন (উদাহরণ: ঢাকা, বাংলাদেশ)
latitude = 23.8103
longitude = 90.4125

# -------------------------------
# 2. Open-Meteo API থেকে এই বছরের ডেটা আনা
url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={latitude}&longitude={longitude}"
    f"&start_date=2025-01-01&end_date=2025-09-01"
    f"&hourly=temperature_2m"
)
response = requests.get(url)
data = response.json()

# -------------------------------
# 3. DataFrame এ কনভার্ট
times = pd.to_datetime(data["hourly"]["time"])
temps = data["hourly"]["temperature_2m"]

df = pd.DataFrame({"time": times, "temp": temps})

# -------------------------------
# 4. সময়কে Z-axis হিসেবে encode করা
# (normalize করে 0..1 রেঞ্জে আনা যাতে cube এর ভেতরে যায়)
df["z"] = (df["time"] - df["time"].min()) / (
    df["time"].max() - df["time"].min()
)

# X, Y: আমরা location fix করেছি, তাই random jitter দিয়ে box এর ভেতরে ছড়িয়ে দেব
np.random.seed(0)
df["x"] = np.random.rand(len(df))
df["y"] = np.random.rand(len(df))

# -------------------------------
# 5. 3D Visualization
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

sc = ax.scatter(
    df["x"], df["y"], df["z"],
    c=df["temp"], cmap="coolwarm", s=10
)

# cube edges আঁকা
r = [0, 1]
cube_edges = [
    ([0,1],[0,0],[0,0]), ([0,1],[1,1],[0,0]), ([0,0],[0,1],[0,0]), ([1,1],[0,1],[0,0]),
    ([0,1],[0,0],[1,1]), ([0,1],[1,1],[1,1]), ([0,0],[0,1],[1,1]), ([1,1],[0,1],[1,1]),
    ([0,0],[0,0],[0,1]), ([0,0],[1,1],[0,1]), ([1,1],[0,0],[0,1]), ([1,1],[1,1],[0,1])
]
for ex, ey, ez in cube_edges:
    ax.plot(ex, ey, ez, linewidth=1, linestyle='--')

ax.set_xlabel("X (random spread)")
ax.set_ylabel("Y (random spread)")
ax.set_zlabel("Time (normalized)")
cbar = fig.colorbar(sc, ax=ax, shrink=0.6, pad=0.1)
cbar.set_label("Temperature (°C)")
ax.set_title("3D Temperature inside a Box (Dhaka, 2025)")
plt.show()

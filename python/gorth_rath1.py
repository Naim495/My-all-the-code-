import requests
import pandas as pd
import matplotlib.pyplot as plt

# --- Parameters ---
country = "BD"  # Bangladesh
indicators = {
    "population_total": "SP.POP.TOTL",   # total population
    "pop_growth_pct": "SP.POP.GROW"     # annual growth %
}
start_year, end_year = 1971, 2025

# --- Helper function to fetch World Bank data ---
def fetch(indicator):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start_year}:{end_year}&format=json&per_page=1000"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    return data[1]

def records_to_df(records):
    rows = []
    for rec in records:
        year = int(rec.get("date"))
        val = rec.get("value")
        if val is not None:
            rows.append({"year": year, "value": val})
    return pd.DataFrame(rows).sort_values("year")

# --- Fetch data ---
df_pop = records_to_df(fetch(indicators["population_total"]))
df_growth = records_to_df(fetch(indicators["pop_growth_pct"]))

# --- Merge datasets ---
df = pd.merge(df_pop, df_growth, on="year", how="outer", suffixes=("_pop", "_growth")).sort_values("year")

# --- Plot ---
fig, ax1 = plt.subplots(figsize=(12,6))

# Population (left axis)
ax1.plot(df["year"], df["value_pop"], color="blue", marker="o", label="Population")
ax1.set_xlabel("Year")
ax1.set_ylabel("Population (Total)", color="blue")
ax1.ticklabel_format(axis='y', style='plain')

# Growth rate (right axis)
ax2 = ax1.twinx()
ax2.plot(df["year"], df["value_growth"], color="red", marker="s", linestyle="--", label="Growth Rate (%)")
ax2.set_ylabel("Population Growth (%)", color="red")

plt.title("Bangladesh Population and Growth Rate (1971–2025)")
fig.tight_layout()
plt.show()

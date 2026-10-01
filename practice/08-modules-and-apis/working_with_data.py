# working_with_data.py
# Process tabular data with the built-in csv module, then optionally with pandas.

import csv
import io
from collections import defaultdict
from statistics import mean

# Sample weather data (in a real project this comes from a file or API)
CSV_TEXT = """date,max_temp,min_temp
2025-08-01,24.1,15.2
2025-08-02,26.3,16.0
2025-08-03,22.8,14.1
2025-08-04,19.5,12.9
2025-08-05,27.0,17.4
2025-08-06,28.2,18.1
2025-08-07,25.6,16.7
"""

# csv.DictReader turns each row into a dictionary
rows = list(csv.DictReader(io.StringIO(CSV_TEXT)))
print("First row:", rows[0])

# Values are strings, so convert them
max_temps = [float(row["max_temp"]) for row in rows]
print("Average max:", round(mean(max_temps), 1))
print("Hottest day:", max(rows, key=lambda r: float(r["max_temp"]))["date"])

# Filtering
warm_days = [row["date"] for row in rows if float(row["max_temp"]) > 25]
print("Warm days:", warm_days)

# Grouping
sales = [("Laptop", 2), ("Mouse", 5), ("Laptop", 1), ("Keyboard", 3), ("Mouse", 2)]
totals = defaultdict(int)
for product, quantity in sales:
    totals[product] += quantity
print("Units per product:", dict(totals))

# The same analysis with pandas (pip install pandas)
try:
    import pandas as pd

    df = pd.read_csv(io.StringIO(CSV_TEXT))
    df["range"] = df["max_temp"] - df["min_temp"]
    print(df.describe().round(1))
except ImportError:
    print("pandas is not installed. Install it with: pip install pandas")

# Try it:
# 1. Calculate the average min_temp.
# 2. Find the day with the biggest difference between max and min.

# working_with_files.py
# Read and write text, CSV and JSON files.

import csv
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR / "data" / "sales.csv"
OUTPUT_DIR = SCRIPT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)  # create the folder if it doesn't exist

# Writing a text file. `with` closes the file automatically.
notes_file = OUTPUT_DIR / "notes.txt"
with open(notes_file, "w", encoding="utf-8") as f:
    f.write("Line one\n")
    f.write("Line two\n")

# Appending
with open(notes_file, "a", encoding="utf-8") as f:
    f.write("Line three\n")

# Reading the whole file or line by line
print(notes_file.read_text(encoding="utf-8"))
with open(notes_file, encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(number, line.strip())

# Reading a CSV file
with open(DATA_FILE, newline="", encoding="utf-8") as f:
    sales = list(csv.DictReader(f))
print(f"Loaded {len(sales)} sales rows")

# Calculate revenue per product
revenue = {}
for row in sales:
    amount = int(row["quantity"]) * float(row["price"])
    revenue[row["product"]] = revenue.get(row["product"], 0) + amount
revenue = {product: round(total, 2) for product, total in revenue.items()}
print("Revenue:", revenue)

# Writing a CSV file
summary_csv = OUTPUT_DIR / "revenue.csv"
with open(summary_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "revenue"])
    for product, total in sorted(revenue.items(), key=lambda item: -item[1]):
        writer.writerow([product, total])
print("Wrote", summary_csv.name)

# Writing and reading JSON
summary_json = OUTPUT_DIR / "revenue.json"
with open(summary_json, "w", encoding="utf-8") as f:
    json.dump(revenue, f, indent=2)
with open(summary_json, encoding="utf-8") as f:
    loaded = json.load(f)
print("Top product from JSON:", max(loaded, key=loaded.get))

# Try it:
# 1. Add a new row to data/sales.csv and run the script again.
# 2. Write the total units sold per product to output/units.json.

# sales_report.py
# Practice: files, paths, CSV, functions, error handling and formatting.
# Reads ../09-practical-python/data/sales.csv and writes a report.

import csv
import json
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "09-practical-python" / "data" / "sales.csv"
OUTPUT_FILE = BASE_DIR / "output" / "sales_report.json"


def load_sales(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Data file not found: {path}")
        return []

    sales = []
    for line_number, row in enumerate(rows, start=2):
        try:
            sales.append({
                "date": row["date"],
                "product": row["product"],
                "quantity": int(row["quantity"]),
                "price": float(row["price"]),
            })
        except (KeyError, ValueError) as error:
            print(f"Skipping line {line_number}: {error}")
    return sales


def build_report(sales):
    by_product = defaultdict(float)
    by_date = defaultdict(float)
    for sale in sales:
        revenue = sale["quantity"] * sale["price"]
        by_product[sale["product"]] += revenue
        by_date[sale["date"]] += revenue
    total = sum(by_product.values())
    return {
        "total_revenue": round(total, 2),
        "orders": len(sales),
        "best_product": max(by_product, key=by_product.get),
        "best_day": max(by_date, key=by_date.get),
        "revenue_by_product": {k: round(v, 2) for k, v in sorted(by_product.items())},
    }


def main():
    sales = load_sales(DATA_FILE)
    if not sales:
        return
    report = build_report(sales)

    print(f"Total revenue: ${report['total_revenue']:,.2f}")
    print(f"Orders: {report['orders']}")
    print(f"Best product: {report['best_product']}")
    print(f"Best day: {report['best_day']}")
    for product, revenue in report["revenue_by_product"].items():
        share = revenue / report["total_revenue"] * 100
        print(f"  {product:<12} ${revenue:>9,.2f}  {share:5.1f}%")

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("Saved report to", OUTPUT_FILE.relative_to(BASE_DIR))


if __name__ == "__main__":
    main()

# Try it:
# 1. Add a row with a bad quantity like "two" to the CSV and see it get skipped.
# 2. Add the average order value to the report.

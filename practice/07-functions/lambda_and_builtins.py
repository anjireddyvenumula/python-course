# lambda_and_builtins.py
# Small anonymous functions and built-ins that take functions as input.

# A lambda is a one-line function without a name
double = lambda x: x * 2  # noqa: E731 (shown for learning; prefer def)
print("double(5):", double(5))

# Most useful with sorted(), min(), max()
products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 29.99},
    {"name": "Monitor", "price": 249.50},
]
by_price = sorted(products, key=lambda p: p["price"])
print("Cheapest first:", [p["name"] for p in by_price])
print("Most expensive:", max(products, key=lambda p: p["price"])["name"])

# map() applies a function to every item
prices = [p["price"] for p in products]
with_tax = list(map(lambda price: round(price * 1.21, 2), prices))
print("With tax:", with_tax)

# filter() keeps items where the function returns True
affordable = list(filter(lambda p: p["price"] < 300, products))
print("Affordable:", [p["name"] for p in affordable])

# Comprehensions often read better than map/filter
affordable_names = [p["name"] for p in products if p["price"] < 300]
print("Same with a comprehension:", affordable_names)

# any() and all()
print("Any over 500:", any(p["price"] > 500 for p in products))
print("All over 10:", all(p["price"] > 10 for p in products))

# Try it:
# 1. Sort a list of words by their length.
# 2. Use filter() to keep only the words that start with a vowel.

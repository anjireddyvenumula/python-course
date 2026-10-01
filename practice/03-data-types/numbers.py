# numbers.py
# Python has two main number types: int (whole numbers) and float (decimals).

age = 30          # int
price = 19.99     # float
print(type(age), type(price))

# Basic math
print("Add:", 10 + 3)
print("Subtract:", 10 - 3)
print("Multiply:", 10 * 3)
print("Divide:", 10 / 3)         # always returns a float
print("Floor divide:", 10 // 3)  # drops the decimal part
print("Remainder:", 10 % 3)      # modulo
print("Power:", 2 ** 10)

# Integer vs float division
print("10 / 2 =", 10 / 2)    # 5.0 (float)
print("10 // 2 =", 10 // 2)  # 5 (int)

# Floats are approximations
print("0.1 + 0.2 =", 0.1 + 0.2)
print("Rounded:", round(0.1 + 0.2, 2))

# Useful built-in functions
print("abs(-7) =", abs(-7))
print("max(3, 9, 4) =", max(3, 9, 4))
print("min(3, 9, 4) =", min(3, 9, 4))
print("round(3.14159, 2) =", round(3.14159, 2))

# Converting between types
print("int(3.9) =", int(3.9))      # cuts off, doesn't round
print("float(5) =", float(5))
print("int('42') + 1 =", int("42") + 1)

# Underscores make big numbers readable
tokens_per_month = 1_000_000
cost_per_token = 0.000002
print("Monthly cost: $", tokens_per_month * cost_per_token)

# Try it:
# 1. Calculate how many full weeks are in 100 days and how many days remain.
# 2. Convert 72 degrees Fahrenheit to Celsius: (F - 32) * 5 / 9

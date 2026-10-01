# operators.py
# Arithmetic, comparison, logical and assignment operators.

a, b = 17, 5

# Arithmetic
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** 2 = {a ** 2}")

# Order of operations: brackets, powers, * /, + -
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

# Comparison
print("a == b:", a == b)
print("a > b:", a > b)
print("Chained 1 < b < 10:", 1 < b < 10)

# Logical operators and their truth table
print("\nA      B      and    or")
for x in (True, False):
    for y in (True, False):
        print(f"{x!s:<6} {y!s:<6} {x and y!s:<6} {x or y!s:<6}")

# Assignment shortcuts
total = 100
total += 10   # 110
total -= 5    # 105
total *= 2    # 210
total /= 3    # 70.0
print("\nTotal after shortcuts:", total)

# Membership and identity
fruits = ["apple", "banana"]
print("'apple' in fruits:", "apple" in fruits)
result = None
print("result is None:", result is None)

# Try it:
# 1. Check if a number is even using %.
# 2. Write one expression that is True only if age is between 13 and 19.

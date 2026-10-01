# booleans.py
# Booleans are True or False. They power every decision in your code.

is_logged_in = True
has_api_key = False
print(is_logged_in, has_api_key, type(is_logged_in))

# Comparisons produce booleans
print("5 > 3:", 5 > 3)
print("5 == 5:", 5 == 5)
print("'a' != 'b':", "a" != "b")
print("10 <= 9:", 10 <= 9)

# Combine with and, or, not
age = 25
has_ticket = True
print("Can enter:", age >= 18 and has_ticket)
print("Free entry:", age < 12 or age > 65)
print("Not logged in:", not is_logged_in)

# Truthy and falsy values
# These count as False: 0, 0.0, "", [], {}, None
for value in [0, 1, "", "text", [], [1], None]:
    print(f"bool({value!r}) = {bool(value)}")

# Common mistake: = assigns, == compares
x = 10
print("x == 10:", x == 10)

# Try it:
# 1. Write a check that is True when a password is at least 8 characters long.
# 2. Predict bool(" ") before running it. Was a space truthy or falsy?

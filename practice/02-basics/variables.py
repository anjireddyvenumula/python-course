# variables.py
# Variables are names that point to values.

# Creating variables
model_name = "gpt-4"
max_tokens = 500
temperature = 0.7
is_streaming = False

print("Model:", model_name)
print("Max tokens:", max_tokens)
print("Temperature:", temperature)
print("Streaming:", is_streaming)

# Changing a variable: the name now points to a new value
max_tokens = 1000
print("Updated max tokens:", max_tokens)

# Using a variable to update itself
counter = 0
counter = counter + 1
counter += 1  # shortcut for counter = counter + 1
print("Counter:", counter)

# Assign several variables at once
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# Swap two variables
a, b = "first", "second"
a, b = b, a
print("After swap:", a, b)

# Naming rules
# - Use snake_case: user_name, total_price
# - Start with a letter or underscore, never a number
# - No spaces or dashes
# - Avoid built-in names like list, str, print
user_name = "Anji"
total_price = 19.99
print(f"{user_name} paid {total_price}")

# Constants are written in UPPER_CASE by convention
MAX_RETRIES = 3
print("Max retries:", MAX_RETRIES)

# Try it:
# 1. Create variables for your name, age and city and print them in one sentence.
# 2. Try naming a variable 2nd_place and read the error.

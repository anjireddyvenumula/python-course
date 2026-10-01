# type_conversion.py
# Check types with type() and convert with int(), float(), str(), bool().

values = [42, 3.14, "hello", True, None, [1, 2], {"a": 1}]
for value in values:
    print(f"{value!r:>12} is {type(value).__name__}")

# isinstance() checks if a value is a certain type
print("isinstance(42, int):", isinstance(42, int))
print("isinstance(3.14, (int, float)):", isinstance(3.14, (int, float)))

# Input from users and files always arrives as text
user_input = "7"
print("Text math:", user_input * 3)            # "777"
print("Number math:", int(user_input) * 3)     # 21

# Converting numbers to text
temperature = 21.5
print("Temperature: " + str(temperature) + "C")

# Converting strings to booleans needs care
print("bool('False') =", bool("False"))  # True, because the string is not empty
answer = "False"
print("Proper check:", answer.lower() == "true")

# Try it:
# 1. Convert "3.99" to a float and multiply it by 3.
# 2. What happens with int("3.99")? Fix it with int(float("3.99")).

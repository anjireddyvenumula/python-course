# strings.py
# Strings hold text. Use single or double quotes.

greeting = "Hello"
name = 'Ada'
quote = "She said 'Python is fun'"
print(greeting, name)
print(quote)

# Multi-line strings use triple quotes
prompt = """You are a helpful assistant.
Answer in one short sentence."""
print(prompt)

# Combining strings
full = greeting + ", " + name + "!"
print(full)

# f-strings: the easiest way to put values inside text
age = 36
print(f"{name} is {age} years old")
print(f"Next year {name} will be {age + 1}")
print(f"Pi rounded: {3.14159:.2f}")

# Length and indexing
word = "Python"
print("Length:", len(word))
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Slice 0-3:", word[0:3])
print("Reversed:", word[::-1])

# Converting to string
score = 95
print("Score: " + str(score))

# Special characters
print("Line one\nLine two")
print("Tab\tseparated")

# Strings are immutable: methods return a new string
original = "python"
upper = original.upper()
print(original, upper)

# Try it:
# 1. Store your first and last name in two variables and print your initials.
# 2. Print a receipt line with an f-string: "Coffee .......... $3.50"

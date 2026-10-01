# dictionaries.py
# Dictionaries store key-value pairs. API responses and configs look like this.

user = {
    "name": "Ada",
    "age": 36,
    "skills": ["python", "math"],
}
print(user)

# Accessing values
print("Name:", user["name"])
print("Email (with default):", user.get("email", "not set"))

# Changing dictionaries
user["age"] = 37            # update
user["email"] = "ada@example.com"  # add
del user["skills"]          # remove
print("Updated:", user)

# Looping
for key in user:
    print("Key:", key)
for key, value in user.items():
    print(f"{key} -> {value}")

print("Keys:", list(user.keys()))
print("Values:", list(user.values()))
print("'name' in user:", "name" in user)

# Nested dictionaries (like a JSON API response)
response = {
    "model": "example-model",
    "usage": {"input_tokens": 12, "output_tokens": 30},
    "choices": [{"message": {"role": "assistant", "content": "Hello!"}}],
}
print("Output tokens:", response["usage"]["output_tokens"])
print("Reply:", response["choices"][0]["message"]["content"])

# Counting with a dictionary
text = "the cat and the hat and the bat"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print("Word counts:", counts)

# Dictionary comprehension
squares = {n: n ** 2 for n in range(1, 6)}
print("Squares:", squares)

# Merging dictionaries
defaults = {"temperature": 0.7, "max_tokens": 256}
overrides = {"max_tokens": 1024}
settings = {**defaults, **overrides}
print("Settings:", settings)

# Try it:
# 1. Make a dictionary of 3 countries and their capitals, then loop over it.
# 2. Access a missing key with [] and then with .get(). Compare the results.

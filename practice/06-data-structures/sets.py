# sets.py
# Sets store unique items with no order. Great for removing duplicates.

tags = {"python", "ai", "data", "python"}
print(tags)  # "python" only appears once

# Remove duplicates from a list
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique_emails = set(emails)
print("Unique:", unique_emails, "| Count:", len(unique_emails))

# Adding and removing
tags.add("ml")
tags.discard("data")   # no error if missing
print("Tags:", sorted(tags))

# Set operations
python_devs = {"Ana", "Ben", "Cara", "Dev"}
ai_devs = {"Cara", "Dev", "Eli"}
print("Both:", python_devs & ai_devs)
print("Either:", python_devs | ai_devs)
print("Only Python:", python_devs - ai_devs)
print("Exactly one:", python_devs ^ ai_devs)

# Fast membership testing
blocked_words = {"spam", "scam", "phishing"}
message = "this is not spam I promise"
found = [word for word in message.split() if word in blocked_words]
print("Blocked words found:", found)

# Common mistake: {} is an empty dictionary, not an empty set
empty_set = set()
print(type({}), type(empty_set))

# Try it:
# 1. Find the letters two words have in common: set("python") & set("typhoon")
# 2. Count the unique words in a sentence.

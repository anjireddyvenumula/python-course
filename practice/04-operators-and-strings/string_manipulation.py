# string_manipulation.py
# Clean, transform and search text. Very common when preparing data for AI.

raw = "   Hello, Python World!   "

# Cleaning
print(repr(raw.strip()))
print(repr(raw.lstrip()))
print(repr(raw.rstrip()))

text = raw.strip()

# Changing case
print(text.upper())
print(text.lower())
print(text.title())
print("hello world".capitalize())

# Finding and replacing
print("Find 'Python':", text.find("Python"))
print("Count 'o':", text.count("o"))
print("Replace:", text.replace("World", "AI"))
print("Starts with Hello:", text.startswith("Hello"))
print("Ends with !:", text.endswith("!"))

# Splitting and joining
sentence = "python is great for ai"
words = sentence.split()
print("Words:", words)
print("Joined with -:", "-".join(words))

csv_line = "Laptop,2,999.99"
product, quantity, price = csv_line.split(",")
print(f"Product={product}, quantity={quantity}, price={price}")

# Concatenation and repetition
print("=" * 30)
print("ab" + "cd")

# Checking content
print("'123'.isdigit():", "123".isdigit())
print("'abc'.isalpha():", "abc".isalpha())

# A small cleaning pipeline
messy_emails = ["  Alice@Example.COM ", "bob@example.com", " CAROL@example.com"]
clean_emails = [email.strip().lower() for email in messy_emails]
print("Clean emails:", clean_emails)

# Try it:
# 1. Count how many words are in a paragraph of your choice.
# 2. Turn "machine learning basics" into "Machine_Learning_Basics".

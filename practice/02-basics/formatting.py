# formatting.py
# Code formatting: clean spacing makes code easier to read.
# Use Ruff (https://docs.astral.sh/ruff/) to format automatically: ruff format .

# Hard to read
x=5;y=10;total=x+y*2

# Easy to read: one statement per line, spaces around operators
x = 5
y = 10
total = x + y * 2
print("Total:", total)

# Spaces after commas
scores = [90, 85, 77]
print("Scores:", scores)

# Long lines can be split inside brackets
message = (
    "This is a long message that is split over "
    "several lines to keep each line short and readable."
)
print(message)


# Two blank lines before and after top-level functions (PEP 8)
def average(numbers):
    return sum(numbers) / len(numbers)


print("Average score:", average(scores))

# Try it:
# 1. Install Ruff with `pip install ruff` and run `ruff format formatting.py`.
# 2. Compare the file before and after formatting.

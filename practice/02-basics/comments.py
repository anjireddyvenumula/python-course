# comments.py
# Comments explain your code. Python ignores everything after a #.

# Single-line comment above the code it explains
price = 100

discount = 0.2  # Inline comment: 20% discount

"""
Multi-line text in triple quotes is often used as a block comment.
Technically it's a string that Python creates and throws away.
"""

final_price = price * (1 - discount)
print("Final price:", final_price)


def calculate_tax(amount):
    """Return the 21% tax for an amount.

    The first string inside a function is a docstring.
    It shows up when you call help(calculate_tax).
    """
    return amount * 0.21


print("Tax:", calculate_tax(final_price))
print("Docstring:", calculate_tax.__doc__.splitlines()[0])

# Good comments explain WHY, not WHAT
# Bad:  x = x + 1  # add 1 to x
# Good: retries += 1  # the API sometimes fails on the first call

# Temporarily disable code by commenting it out
# print("This line does not run")

# Try it:
# 1. Add a docstring to a new function and print it with help().
# 2. Comment out the final print and run the file again.

# math_helpers.py
# Small, reusable math functions.


def average(numbers):
    """Return the average of a list of numbers, or 0 for an empty list."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def percentage(part, whole):
    """Return part as a percentage of whole, rounded to one decimal."""
    return round(part / whole * 100, 1)

# reading_errors.py
# Errors are normal. This file triggers common errors safely and shows how to read them.

import traceback


def show_error(description, code):
    """Run a small piece of code and print the error it raises."""
    print(f"--- {description} ---")
    try:
        exec(code)
    except Exception:
        # The last line of a traceback tells you the error type and message
        last_line = traceback.format_exc().strip().splitlines()[-1]
        print("Error:", last_line)
    print()


show_error("Using a variable that doesn't exist", "print(username)")
show_error("Adding text and a number", "'Age: ' + 25")
show_error("Dividing by zero", "10 / 0")
show_error("Index out of range", "[1, 2, 3][5]")
show_error("Converting invalid text to a number", "int('hello')")

# How to read a traceback:
# 1. Start at the bottom: the error type and message.
# 2. Look at the line number above it to find where it happened.
# 3. Read upward to see which function calls led there.

print("Full traceback example:")
try:
    result = int("not a number")
except ValueError:
    traceback.print_exc()

# Try it:
# 1. Write your own broken line, run it, and explain the error in your own words.
# 2. Paste an error into an AI assistant and ask it to explain the cause.

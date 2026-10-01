# if_statements.py
# Make decisions with if, elif and else.

score = 82

# Basic if
if score >= 50:
    print("You passed")

# if-else
if score >= 90:
    print("Excellent")
else:
    print("Keep going")

# if-elif-else chain: Python stops at the first True condition
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)

# Multiple conditions
age = 20
has_id = True
if age >= 18 and has_id:
    print("Access granted")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend")

# Nested if statements
is_member = True
cart_total = 120
if is_member:
    if cart_total > 100:
        print("Member discount: 20%")
    else:
        print("Member discount: 10%")
else:
    print("No discount")

# Conditional expression (one-line if)
status = "adult" if age >= 18 else "minor"
print("Status:", status)

# match statement (Python 3.10+) for many fixed options
command = "stop"
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")

# Try it:
# 1. Write a FizzBuzz check for a single number.
# 2. Classify a temperature as cold (<10), mild (10-24) or hot (25+).

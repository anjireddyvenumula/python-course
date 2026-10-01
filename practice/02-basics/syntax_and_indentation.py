# syntax_and_indentation.py
# Python uses indentation (4 spaces) to group code into blocks.

temperature = 25

# The indented lines belong to the if block
if temperature > 20:
    print("It's warm outside")
    print("This line is also inside the if block")

# This line is not indented, so it always runs
print("This line always runs")

# Blocks can be nested. Each level adds 4 more spaces.
for hour in range(3):
    print("Hour", hour)
    if hour == 1:
        print("    It's hour one")

# Common syntax rules
# - Statements like if, for, def end with a colon (:)
# - Strings need matching quotes: "text" or 'text'
# - Python is case sensitive: Name and name are different variables
name = "Ada"
Name = "Grace"
print(name, Name)

# Try it:
# 1. Remove the indentation from line 9 and run the file. Read the IndentationError.
# 2. Remove the colon after `if temperature > 20` and read the SyntaxError.

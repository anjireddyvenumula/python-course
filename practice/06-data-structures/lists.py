# lists.py
# Lists store ordered collections that you can change.

fruits = ["apple", "banana", "cherry"]
numbers = [3, 1, 4, 1, 5, 9]
mixed = ["text", 42, 3.14, True]
empty = []
print(fruits, numbers, mixed, empty)

# Accessing items
print("First:", fruits[0])
print("Last:", fruits[-1])
print("First two:", fruits[:2])

# Changing lists
fruits[1] = "blueberry"
fruits.append("date")
fruits.insert(0, "avocado")
print("After changes:", fruits)

fruits.remove("cherry")
last = fruits.pop()
print("Popped:", last, "| Remaining:", fruits)

# Useful methods and functions
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Count of 1:", numbers.count(1))
print("Index of 4:", numbers.index(4))
print("Sorted copy:", sorted(numbers))

numbers.sort(reverse=True)
print("Sorted in place (desc):", numbers)

# Checking lists
print("'apple' in fruits:", "apple" in fruits)
if not empty:
    print("The empty list is falsy")

# Combining lists
combined = [1, 2] + [3, 4]
combined.extend([5, 6])
print("Combined:", combined)

# Lists of lists (like a table)
matrix = [[1, 2, 3], [4, 5, 6]]
print("Row 2, column 3:", matrix[1][2])

# Common mistake: copying a list
original = [1, 2, 3]
alias = original          # same list, two names
copy = original.copy()    # a real copy
original.append(4)
print("alias:", alias, "| copy:", copy)

# Try it:
# 1. Build a list of your 5 favorite movies and print them sorted.
# 2. Remove duplicates from [1, 2, 2, 3, 3, 3] while keeping the order.

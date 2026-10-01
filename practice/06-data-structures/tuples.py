# tuples.py
# Tuples are ordered like lists but cannot be changed (immutable).

point = (4, 7)
rgb = (255, 128, 0)
single = (42,)  # a one-item tuple needs a trailing comma
print(point, rgb, single, type(single))

# Accessing items
print("x:", point[0], "y:", point[1])

# Tuple unpacking
x, y = point
print(f"x={x}, y={y}")

red, green, blue = rgb
print(f"Red={red}, Green={green}, Blue={blue}")


# Functions often return tuples
def min_max(values):
    return min(values), max(values)


low, high = min_max([3, 9, 1, 7])
print("Low:", low, "High:", high)

# Tuples cannot be changed
try:
    point[0] = 10
except TypeError as error:
    print("Error:", error)

# Tuples can be dictionary keys (lists cannot)
distances = {("Paris", "London"): 344, ("Paris", "Berlin"): 878}
print("Paris to Berlin:", distances[("Paris", "Berlin")], "km")

# Use * to collect the rest
first, *rest = (1, 2, 3, 4)
print("First:", first, "Rest:", rest)

# Try it:
# 1. Store a date as (year, month, day) and unpack it into three variables.
# 2. Loop over a list of (name, score) tuples and print each one.

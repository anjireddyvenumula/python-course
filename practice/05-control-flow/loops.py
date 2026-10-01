# loops.py
# Repeat code with for loops and while loops.

# Repeat a specific number of times
for i in range(3):
    print("Iteration", i)

# Different starting points and steps
print("Count 1 to 5:", list(range(1, 6)))
print("Even numbers:", list(range(0, 11, 2)))
print("Countdown:", list(range(5, 0, -1)))

# Loop through text
for letter in "AI":
    print("Letter:", letter)

# Loop through a list
models = ["gpt", "claude", "llama"]
for model in models:
    print("Model:", model)

# enumerate gives you the index and the item
for index, model in enumerate(models, start=1):
    print(f"{index}. {model}")

# zip loops over two lists together
prices = [0.01, 0.015, 0.0]
for model, price in zip(models, prices):
    print(f"{model} costs {price}")

# While loop: repeats while the condition is True
attempts = 0
while attempts < 3:
    attempts += 1
    print("Attempt", attempts)

# break stops the loop, continue skips to the next item
for number in range(1, 10):
    if number == 7:
        print("Found 7, stopping")
        break
    if number % 2 == 0:
        continue
    print("Odd number:", number)

# Accumulating a result
total = 0
for number in [4, 8, 15, 16, 23, 42]:
    total += number
print("Sum:", total)

# List comprehension: a compact loop that builds a list
squares = [n ** 2 for n in range(1, 6)]
evens = [n for n in range(10) if n % 2 == 0]
print("Squares:", squares)
print("Evens:", evens)

# FizzBuzz, the classic loop exercise
for n in range(1, 16):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# Try it:
# 1. Print the multiplication table for 7.
# 2. Use a while loop to double a number until it is above 1000.

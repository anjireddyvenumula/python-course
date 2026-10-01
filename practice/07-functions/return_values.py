# return_values.py
# return sends a value back so you can use it later.


def square(number):
    return number * number


result = square(6)
print("Square:", result)
print("Used in math:", square(3) + square(4))


# Return vs print
def add_print(a, b):
    print(a + b)  # shows the value, returns None


def add_return(a, b):
    return a + b  # gives the value back


value1 = add_print(2, 3)
value2 = add_return(2, 3)
print("add_print returned:", value1)
print("add_return returned:", value2)


# Returning multiple values (as a tuple)
def analyze(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


low, high, avg = analyze([10, 20, 30, 40])
print(f"Low={low}, High={high}, Average={avg}")


# return ends the function immediately
def find_first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n
    return None


print("First negative:", find_first_negative([5, 3, -2, -8]))
print("No negative:", find_first_negative([1, 2, 3]))


# Functions working together
def clean_text(text):
    return text.strip().lower()


def count_words(text):
    return len(clean_text(text).split())


print("Word count:", count_words("  Python Is Great For AI  "))


# Returning a dictionary is common for structured results
def summarize_order(item, quantity, unit_price):
    return {
        "item": item,
        "quantity": quantity,
        "total": round(quantity * unit_price, 2),
    }


print(summarize_order("Mouse", 3, 29.99))

# Try it:
# 1. Write is_even(n) that returns True or False and use it in an if statement.
# 2. Write a function that returns both the word count and character count of a text.

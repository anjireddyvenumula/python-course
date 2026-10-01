# parameters.py
# Parameters let you pass information into functions.


# Basic parameter
def greet(name):
    print(f"Hello, {name}!")


greet("Ada")


# Multiple parameters: order matters
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")


describe_pet("dog", "Rex")


# Default values
def ask_model(prompt, model="small-model", temperature=0.7):
    print(f"[{model} @ {temperature}] {prompt}")


ask_model("What is Python?")
ask_model("Write a poem", temperature=1.0)

# Keyword arguments: order doesn't matter when you name them
describe_pet(name="Whiskers", animal="cat")


# *args collects any number of positional arguments into a tuple
def total(*numbers):
    return sum(numbers)


print("Total:", total(1, 2, 3, 4))


# **kwargs collects any number of keyword arguments into a dictionary
def build_request(**options):
    for key, value in options.items():
        print(f"  {key} = {value}")


print("Request options:")
build_request(model="demo", max_tokens=100, stream=False)


# Type hints document what you expect (Python doesn't enforce them)
def repeat(text: str, times: int = 2) -> str:
    return text * times


print(repeat("ha", 3))


# Common mistake: mutable default values
def add_item_bad(item, items=[]):
    items.append(item)
    return items


def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print("Bad:", add_item_bad("a"), add_item_bad("b"))    # shares one list!
print("Good:", add_item_good("a"), add_item_good("b"))

# Try it:
# 1. Write calculate_price(price, tax_rate=0.21, discount=0) and call it three ways.
# 2. Write a function that accepts any number of names and greets each one.

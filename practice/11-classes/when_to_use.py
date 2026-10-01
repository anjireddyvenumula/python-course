# when_to_use.py
# Functions for simple transformations, classes when data and behavior belong together.
# Also shows dataclasses, a shortcut for classes that mostly hold data.

from dataclasses import dataclass, field


# A plain function is enough here: input in, output out, no state
def word_count(text):
    return len(text.split())


print("Function result:", word_count("classes are not always needed"))


# A class makes sense when you keep state between calls
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, item, price, quantity=1):
        current = self.items.get(item, (price, 0))
        self.items[item] = (price, current[1] + quantity)

    def total(self):
        return round(sum(price * qty for price, qty in self.items.values()), 2)


cart = ShoppingCart()
cart.add("Notebook", 3.50, 2)
cart.add("Pen", 1.20, 5)
cart.add("Notebook", 3.50)
print("Cart:", cart.items)
print("Total:", cart.total())


# dataclass writes __init__ and __repr__ for you
@dataclass
class Document:
    title: str
    content: str
    tags: list = field(default_factory=list)

    def preview(self, length=20):
        return self.content[:length] + "..."


doc = Document("Intro", "Python is a great language for AI work", ["python"])
print(doc)
print("Preview:", doc.preview())

# Try it:
# 1. Turn ShoppingCart's items into a list of dataclass CartItem objects.
# 2. Decide: would you use a class or a function for converting Celsius to Fahrenheit?

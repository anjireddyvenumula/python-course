# first_class.py
# A class is a blueprint. Objects (instances) are built from it.


class Dog:
    # __init__ runs when you create a new object
    def __init__(self, name, age):
        self.name = name  # self refers to this specific object
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


rex = Dog("Rex", 3)
bella = Dog("Bella", 5)
print(rex.bark())
print(bella.bark())
print(f"{rex.name} is {rex.age}, {bella.name} is {bella.age}")


# Real-world example: configuration for an AI call
class ModelConfig:
    def __init__(self, model="small-model", temperature=0.7, max_tokens=256):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def to_dict(self):
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }


default_config = ModelConfig()
creative_config = ModelConfig(temperature=1.2, max_tokens=1000)
print(default_config.to_dict())
print(creative_config.to_dict())


# Class attributes are shared, instance attributes belong to one object
class Counter:
    instances_created = 0  # class attribute

    def __init__(self):
        Counter.instances_created += 1
        self.count = 0  # instance attribute


a, b = Counter(), Counter()
a.count += 5
print("a.count:", a.count, "| b.count:", b.count)
print("Counters created:", Counter.instances_created)

# Try it:
# 1. Create a Book class with title, author and pages, plus a describe() method.
# 2. Create two books and print their descriptions.

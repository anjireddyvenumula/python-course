# inheritance.py
# A child class reuses and extends a parent class.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def describe(self):
        return f"I am {self.name}"


# Dog inherits everything from Animal and overrides speak()
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"


# Cat adds a new attribute. super() calls the parent's __init__.
class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name)
        self.indoor = indoor

    def speak(self):
        return f"{self.name} meows"


for animal in [Animal("Generic"), Dog("Rex"), Cat("Luna", indoor=False)]:
    print(animal.speak(), "|", animal.describe())

print("Is a Dog an Animal?", isinstance(Dog("Max"), Animal))


# Real-world use case: different AI providers with one shared interface
class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate(self, prompt):
        raise NotImplementedError("Child classes must implement generate()")

    def run(self, prompt):
        print(f"[{self.model_name}] prompt: {prompt}")
        return self.generate(prompt)


class EchoModel(BaseModel):
    def generate(self, prompt):
        return prompt


class ShoutModel(BaseModel):
    def generate(self, prompt):
        return prompt.upper() + "!"


for model in [EchoModel("echo-1"), ShoutModel("shout-1")]:
    print("  ->", model.run("hello python"))

try:
    BaseModel("base").run("test")
except NotImplementedError as error:
    print("Error:", error)

# Try it:
# 1. Add a Bird class that overrides speak() and adds a can_fly attribute.
# 2. Add a ReverseModel that returns the prompt reversed.

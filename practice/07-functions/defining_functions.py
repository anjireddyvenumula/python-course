# defining_functions.py
# Functions package code so you can reuse it.


# Define a function with def, a name, brackets and a colon
def greet():
    print("Hello from a function!")


# Call it by name with brackets
greet()
greet()


# Functions can contain any logic
def check_temperature(celsius):
    if celsius > 30:
        print(f"{celsius}C: hot")
    elif celsius > 15:
        print(f"{celsius}C: pleasant")
    else:
        print(f"{celsius}C: cold")


for temp in [35, 20, 5]:
    check_temperature(temp)

# Variable scope: local vs global
app_name = "Course App"  # global variable


def show_scope():
    message = "I only exist inside this function"  # local variable
    print(message)
    print("Can read global:", app_name)


show_scope()
# print(message)  # would raise NameError: message is local

# Modifying a global variable (works, but prefer parameters and returns)
counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()
print("Counter:", counter)


# Best practice: pass values in, return values out
def add_one(value):
    return value + 1


counter = add_one(counter)
print("Counter with return:", counter)

# Try it:
# 1. Write a function that prints a box of * with a given width.
# 2. Call print(message) outside show_scope() and read the error.

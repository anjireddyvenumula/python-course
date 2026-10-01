# try_except.py
# Handle errors so your program keeps running.

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero")
    result = None
print("Result:", result)


# Catching specific errors and reading the message
def to_number(text):
    try:
        return float(text)
    except ValueError as error:
        print(f"Could not convert {text!r}: {error}")
        return None


print(to_number("3.14"))
print(to_number("three"))

# Handling multiple error types
data = {"scores": [90, 85]}
for key, index in [("scores", 0), ("scores", 5), ("names", 0)]:
    try:
        print("Value:", data[key][index])
    except KeyError:
        print(f"Missing key: {key}")
    except IndexError:
        print(f"No item at index {index}")

# else runs when no error happened, finally always runs
for value in ["42", "oops"]:
    try:
        number = int(value)
    except ValueError:
        print(f"{value!r} is not a whole number")
    else:
        print(f"Converted {value!r} to {number}")
    finally:
        print("Done checking", repr(value))


# Raising your own errors
def set_temperature(value):
    if not 0 <= value <= 2:
        raise ValueError(f"temperature must be between 0 and 2, got {value}")
    return value


try:
    set_temperature(5)
except ValueError as error:
    print("Caught:", error)


# Retrying a flaky operation
attempt_results = iter([False, False, True])  # pretend the first two calls fail


def flaky_api_call():
    if not next(attempt_results):
        raise ConnectionError("network hiccup")
    return "success"


for attempt in range(1, 4):
    try:
        print(f"Attempt {attempt}:", flaky_api_call())
        break
    except ConnectionError as error:
        print(f"Attempt {attempt} failed: {error}")

# Common mistake: a bare `except:` hides every error, including typos.
# Always catch the specific error you expect.

# Try it:
# 1. Write safe_divide(a, b) that returns None instead of crashing on b == 0.
# 2. Open a file that doesn't exist and handle the FileNotFoundError.

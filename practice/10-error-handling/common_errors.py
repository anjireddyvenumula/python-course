# common_errors.py
# The errors you will meet most often, what causes them and how to fix them.

examples = [
    ("FileNotFoundError", lambda: open("does_not_exist.txt"),
     "Check the path. Build it from Path(__file__).parent."),
    ("ValueError", lambda: int("12abc"),
     "The type is right but the value is wrong. Validate input first."),
    ("KeyError", lambda: {"name": "Ada"}["email"],
     "The key is missing. Use dict.get('email') or check with 'in'."),
    ("IndexError", lambda: [1, 2, 3][3],
     "Lists start at 0. The last item is at len(items) - 1."),
    ("TypeError", lambda: "Total: " + 10,
     "Mixed types. Convert with str() or use an f-string."),
    ("AttributeError", lambda: [1, 2, 3].push(4),
     "That method doesn't exist. Lists use append(). Check with dir()."),
    ("NameError", lambda: undefined_variable,  # noqa: F821
     "Typo or variable not defined yet."),
    ("ZeroDivisionError", lambda: 1 / 0,
     "Check the divisor before dividing."),
]

for expected, action, fix in examples:
    try:
        action()
    except Exception as error:
        print(f"{type(error).__name__}: {error}")
        print(f"  Fix: {fix}\n")

# Try it:
# 1. Trigger a ModuleNotFoundError with `import not_a_real_module`.
# 2. Write a try-except that handles both KeyError and IndexError for nested data.

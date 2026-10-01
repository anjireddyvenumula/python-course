# importing_modules.py
# Use code that others wrote. Python ships with many built-in modules.

# Import a whole module
import math
import random
from datetime import datetime, timedelta
from pathlib import Path
import json as js  # import with a shorter alias

print("Square root of 16:", math.sqrt(16))
print("Pi:", round(math.pi, 4))

# Import specific names
print("Today:", datetime.now().strftime("%Y-%m-%d"))
print("In 7 days:", (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"))

# random is useful for sampling data
random.seed(42)  # makes the result repeatable
print("Random number 1-10:", random.randint(1, 10))
print("Random choice:", random.choice(["red", "green", "blue"]))

print("This file is called:", Path(__file__).name)
print("JSON via alias:", js.dumps({"ok": True}))

# External packages are installed with pip (or uv) before importing.
# This checks whether `requests` is available without crashing.
try:
    import requests  # noqa: F401

    print("requests is installed")
except ImportError:
    print("requests is not installed. Install it with: pip install requests")

# Save your project's packages so others can install them:
#   pip freeze > requirements.txt
#   pip install -r requirements.txt

# Try it:
# 1. Use math.ceil() and math.floor() on 4.3.
# 2. Print the day of the week for today with datetime.now().strftime("%A").

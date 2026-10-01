# working_with_json.py
# JSON is the format most APIs use. Python turns it into dicts and lists.

import json

# A JSON string, like one you would get from an API
raw = """
{
    "city": "Paris",
    "current": {"temperature": 21.5, "unit": "C"},
    "forecast": [19.0, 22.5, 24.1]
}
"""

# json.loads: JSON text -> Python objects
data = json.loads(raw)
print(type(data))
print("City:", data["city"])
print("Now:", data["current"]["temperature"], data["current"]["unit"])
print("Max forecast:", max(data["forecast"]))

# json.dumps: Python objects -> JSON text
report = {"city": data["city"], "average": round(sum(data["forecast"]) / 3, 1)}
print(json.dumps(report))
print(json.dumps(report, indent=2))

# Python and JSON types
# dict <-> object, list <-> array, str <-> string,
# int/float <-> number, True/False <-> true/false, None <-> null
print(json.dumps({"active": True, "missing": None}))

# Invalid JSON raises an error you can catch
try:
    json.loads("{'single': 'quotes are not valid JSON'}")
except json.JSONDecodeError as error:
    print("Invalid JSON:", error)

# Try it:
# 1. Add a "country" key to data and print it as formatted JSON.
# 2. Calculate the average of data["forecast"] yourself.

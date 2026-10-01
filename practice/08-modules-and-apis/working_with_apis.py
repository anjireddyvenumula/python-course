# working_with_apis.py
# Call a free weather API (no account needed) and extract what you need.
# Uses the built-in urllib so it runs without installing anything.
# The course itself uses `requests`, shown at the bottom.

import json
from urllib.error import URLError
from urllib.request import urlopen

latitude = 48.85   # Paris
longitude = 2.35

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}&current=temperature_2m"
)

# Sample response used when you are offline
SAMPLE_RESPONSE = {
    "latitude": 48.84,
    "longitude": 2.36,
    "current_units": {"temperature_2m": "°C"},
    "current": {"time": "2025-08-01T08:30", "temperature_2m": 20.0},
}

try:
    with urlopen(url, timeout=5) as response:
        data = json.loads(response.read())
    print("Live data received")
except (URLError, TimeoutError, OSError) as error:
    print(f"Could not reach the API ({error}). Using sample data instead.")
    data = SAMPLE_RESPONSE

# Extract what you need from the nested dictionary
temperature = data["current"]["temperature_2m"]
unit = data["current_units"]["temperature_2m"]
time = data["current"]["time"]
print(f"Temperature in Paris at {time}: {temperature}{unit}")

# The same call with requests (pip install requests):
#
#   import requests
#   response = requests.get(url, timeout=5)
#   response.raise_for_status()   # raises an error for 4xx/5xx status codes
#   data = response.json()
#
# Calling AI APIs follows the same pattern, plus an API key in the headers:
#
#   headers = {"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}
#   requests.post(api_url, headers=headers, json=payload)

# Try it:
# 1. Change the coordinates to your own city.
# 2. Add &daily=temperature_2m_max&timezone=auto to the URL and print the daily maximums.

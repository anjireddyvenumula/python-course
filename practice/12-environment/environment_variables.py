# environment_variables.py
# Keep secrets like API keys out of your code. Read them from the environment.
#
# Set a variable before running:
#   macOS/Linux:  export OPENAI_API_KEY="sk-..."
#   Windows (PowerShell):  $env:OPENAI_API_KEY="sk-..."

import os

# Read with a default so the program doesn't crash
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    # Never print a full key. Show only the start.
    print("API key found:", api_key[:5] + "...")
else:
    print("OPENAI_API_KEY is not set")

debug = os.getenv("DEBUG", "false").lower() == "true"
max_retries = int(os.getenv("MAX_RETRIES", "3"))
print("Debug mode:", debug)
print("Max retries:", max_retries)

# os.environ works like a dictionary
print("HOME/USERPROFILE:", os.environ.get("HOME") or os.environ.get("USERPROFILE"))

# You can set variables for the current process (useful in tests)
os.environ["APP_MODE"] = "practice"
print("APP_MODE:", os.environ["APP_MODE"])

# os.environ["MISSING"] raises KeyError. Use it only for required settings:
try:
    os.environ["SOME_REQUIRED_SETTING"]
except KeyError:
    print("SOME_REQUIRED_SETTING is required but missing")

# Try it:
# 1. Set DEBUG=true in your terminal and run this file again.
# 2. Set MAX_RETRIES=abc and handle the ValueError it causes.

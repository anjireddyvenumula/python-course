# dotenv_example.py
# Load settings from a .env file.
#
# Setup:
#   1. pip install python-dotenv
#   2. Copy .env.example to .env and fill in your values
#   3. Make sure .env is listed in your .gitignore

import os
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parent / ".env"
EXAMPLE_FILE = Path(__file__).resolve().parent / ".env.example"


def load_env_manually(path):
    """A tiny .env reader, so you can see what python-dotenv does for you."""
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"'))


env_path = ENV_FILE if ENV_FILE.exists() else EXAMPLE_FILE
print("Loading settings from:", env_path.name)

try:
    from dotenv import load_dotenv

    load_dotenv(env_path)
    print("Loaded with python-dotenv")
except ImportError:
    load_env_manually(env_path)
    print("python-dotenv not installed, used the manual loader")

key = os.getenv("OPENAI_API_KEY", "")
print("OPENAI_API_KEY:", key[:5] + "..." if key else "not set")
print("DEBUG:", os.getenv("DEBUG"))
print("MAX_RETRIES:", os.getenv("MAX_RETRIES"))

# Try it:
# 1. Create your own .env file with a new variable and print it.
# 2. Run `git status` and confirm .env is not listed (it is ignored).

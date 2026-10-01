# python_paths.py
# Relative paths depend on where you run Python from. Build paths from the
# script's own location instead, and they work from anywhere.

import os
from pathlib import Path

print("Current working directory:", Path.cwd())

# The folder this script lives in, no matter where you run it from
SCRIPT_DIR = Path(__file__).resolve().parent
print("Script folder:", SCRIPT_DIR)

# Build paths with / (works on Windows, macOS and Linux)
data_file = SCRIPT_DIR / "data" / "sales.csv"
print("Data file:", data_file)
print("Exists:", data_file.exists())
print("Name:", data_file.name, "| Stem:", data_file.stem, "| Suffix:", data_file.suffix)

# Relative vs absolute
relative = Path("data/sales.csv")
print("Relative path:", relative, "| absolute?", relative.is_absolute())
print("Relative exists from current folder:", relative.exists())

# List files in a folder
for path in sorted((SCRIPT_DIR / "data").glob("*.csv")):
    print("Found CSV:", path.name)

# The older os.path module does the same job
print("os.path.join:", os.path.join("data", "sales.csv"))

# Try it:
# 1. Run this script from the practice/ folder and from inside 09-practical-python/.
#    Which "exists" checks change?
# 2. Print the parent of the parent of SCRIPT_DIR.

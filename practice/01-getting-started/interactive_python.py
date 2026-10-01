# interactive_python.py
# Shows what you would normally type in the interactive Python shell (REPL).
# Start the shell with: python   (exit with exit() or Ctrl+D)

import sys

# In the shell, typing an expression shows its value automatically.
# In a script, you need print() to see results.
print(2 + 3)
print("ai" * 3)
print(len("Python"))

# Which Python is running this file?
print("Python version:", sys.version.split()[0])
print("Python executable:", sys.executable)

# help() and dir() are great for exploring in the shell
print("String methods (first 10):", [name for name in dir(str) if not name.startswith("_")][:10])

# Try it:
# 1. Open a terminal, type `python`, and run the same lines one by one.
# 2. Run help(str.upper) in the shell to read its documentation.

# Practice programs

Runnable example programs for every topic in the Learn Python for AI course. Each folder matches a section of the course, in the same order. Every file is heavily commented and ends with a short "Try it" list of exercises.

All programs use only the Python standard library, so they run without installing anything. Where the course uses an external package (`requests`, `pandas`, `python-dotenv`), the program shows that version too and falls back gracefully when it's not installed.

## How to run

You need Python 3.10 or newer.

```bash
cd practice

# Run a single program
python 05-control-flow/loops.py

# Run every program and check they all work
python run_all.py

# Run only some sections
python run_all.py 06 07
```


Read a file top to bottom, run it, then change something and run it again. That loop is the fastest way to learn.

## Topics

| Folder | Course section | Programs |
| --- | --- | --- |
| `01-getting-started` | Getting started | `hello.py`, `interactive_python.py` |
| `02-basics` | Python basics | `syntax_and_indentation.py`, `variables.py`, `comments.py`, `reading_errors.py`, `formatting.py` |
| `03-data-types` | Data types | `numbers.py`, `strings.py`, `booleans.py`, `type_conversion.py` |
| `04-operators-and-strings` | Working with data | `operators.py`, `string_manipulation.py` |
| `05-control-flow` | Control flow | `if_statements.py`, `loops.py` (includes list comprehensions) |
| `06-data-structures` | Data structures | `lists.py`, `dictionaries.py`, `tuples.py`, `sets.py` |
| `07-functions` | Functions | `defining_functions.py`, `parameters.py`, `return_values.py`, `lambda_and_builtins.py` |
| `08-modules-and-apis` | External tools | `importing_modules.py`, `working_with_json.py`, `working_with_apis.py`, `working_with_data.py` |
| `09-practical-python` | Practical Python | `python_paths.py`, `working_with_files.py`, `organizing-code/main.py` (imports from `utils/`) |
| `10-error-handling` | Error handling | `try_except.py`, `common_errors.py` |
| `11-classes` | Classes | `first_class.py`, `methods_attributes.py`, `inheritance.py`, `when_to_use.py` (includes dataclasses) |
| `12-environment` | Environment and secrets | `environment_variables.py`, `dotenv_example.py`, `.env.example` |
| `13-mini-projects` | Putting it together | `number_guessing.py`, `todo_manager.py`, `text_analyzer.py`, `sales_report.py`, `prompt_builder.py` |

## Notes

- `working_with_apis.py` calls the free [Open-Meteo](https://open-meteo.com/) weather API. Offline, it uses a sample response instead.
- Programs that write files put them in an `output/` folder next to the script. These folders are ignored by Git.
- `number_guessing.py --play` lets you play yourself, and `todo_manager.py add "task"` keeps a real to-do list.
- Copy `12-environment/.env.example` to `.env` to practice with environment files. `.env` is ignored by Git.

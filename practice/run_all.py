# run_all.py
# Run every practice program in order and report which ones pass.
#
# python run_all.py              -> run everything
# python run_all.py 05 06        -> run only folders starting with 05 or 06

import subprocess
import sys
from pathlib import Path

PRACTICE_DIR = Path(__file__).resolve().parent

# Helper modules that are imported by other files, not run on their own
SKIP_FOLDERS = {"utils"}


def find_programs(prefixes):
    programs = []
    for path in sorted(PRACTICE_DIR.glob("[0-9][0-9]-*/**/*.py")):
        if SKIP_FOLDERS & set(path.parts):
            continue
        folder = path.relative_to(PRACTICE_DIR).parts[0]
        if prefixes and not folder.startswith(tuple(prefixes)):
            continue
        programs.append(path)
    return programs


def main():
    programs = find_programs(sys.argv[1:])
    failed = []
    for path in programs:
        name = path.relative_to(PRACTICE_DIR)
        result = subprocess.run(
            [sys.executable, path.name],
            cwd=path.parent,
            capture_output=True,
            text=True,
            timeout=60,
        )
        status = "ok" if result.returncode == 0 else "FAILED"
        print(f"{status:<7} {name}")
        if result.returncode != 0:
            failed.append(name)
            print(result.stderr)

    print(f"\n{len(programs) - len(failed)}/{len(programs)} programs ran successfully")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

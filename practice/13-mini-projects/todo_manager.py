# todo_manager.py
# Practice: classes, lists of dictionaries, JSON files and error handling.
#
# Commands:
#   python todo_manager.py add "Learn loops"
#   python todo_manager.py done 1
#   python todo_manager.py list
#   python todo_manager.py demo     (default: runs a short demo)

import json
import sys
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent / "output"


class TodoList:
    def __init__(self, path):
        self.path = path
        self.tasks = self.load()

    def load(self):
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Warning: todo file was corrupted, starting fresh")
            return []

    def save(self):
        self.path.parent.mkdir(exist_ok=True)
        self.path.write_text(json.dumps(self.tasks, indent=2), encoding="utf-8")

    def add(self, title):
        self.tasks.append({"id": len(self.tasks) + 1, "title": title, "done": False})
        self.save()

    def complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self.save()
                return True
        return False

    def show(self):
        if not self.tasks:
            print("No tasks yet")
        for task in self.tasks:
            mark = "x" if task["done"] else " "
            print(f"[{mark}] {task['id']}. {task['title']}")


def demo():
    todos = TodoList(OUTPUT_DIR / "demo_todos.json")
    todos.tasks = []
    for title in ["Install Python", "Learn variables", "Write a function"]:
        todos.add(title)
    todos.complete(1)
    todos.complete(2)
    todos.show()
    done = sum(task["done"] for task in todos.tasks)
    print(f"Progress: {done}/{len(todos.tasks)} done")


def main(args):
    if not args or args[0] == "demo":
        demo()
        return
    todos = TodoList(OUTPUT_DIR / "todos.json")
    command = args[0]
    if command == "add" and len(args) > 1:
        todos.add(" ".join(args[1:]))
    elif command == "done" and len(args) > 1:
        if not todos.complete(int(args[1])):
            print("No task with id", args[1])
    elif command != "list":
        print("Unknown command. Use add, done, list or demo.")
        return
    todos.show()


if __name__ == "__main__":
    main(sys.argv[1:])

# Try it:
# 1. Add a `remove` command.
# 2. Add a due date to each task and show overdue tasks first.

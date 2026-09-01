<<<<<<< HEAD
# DecodeLabs Python Internship — Project 1: The To-Do List

**Batch:** 2026 | **Track:** Python Programming — Industrial Training Kit

## Overview

A command-line To-Do List app built as the Week 1 milestone for the DecodeLabs
Python internship. The project focuses on the foundation of data management:
storing multiple items in a single variable (a list), and building simple
CRUD-style operations around it.

## Features

- **Add** tasks to an in-memory list (`my_tasks.append(...)`)
- **View** tasks using a `for` loop with `enumerate()` for clean indexing
- **Mark tasks done**
- **Remove** tasks
- **Persistence**: tasks are saved to `tasks.json` on disk, so your list
  survives between runs (RAM → Disk, as covered in the "Engineering Requires
  Persistence" section of the training deck)

## Architecture

The project follows a simple **Model / View** split, matching the
"Decoupling the Architecture" concept from the training material:

| File         | Role  | Responsibility                                   |
|--------------|-------|---------------------------------------------------|
| `tasks.py`   | Model | Data logic — load/save/add/remove/mark done       |
| `main.py`    | View  | Command-line menu and user interaction            |

## How to Run

```bash
python3 main.py
```

You'll see a menu:

```
==============================
   DECODELABS TO-DO LIST
==============================
1. Add a task
2. View all tasks
3. Mark a task as done
4. Remove a task
5. Exit
==============================
```

## Key Concepts Practiced

- Lists as dynamic, growable containers (`my_tasks = []`)
- `list.append()` — O(1) amortized insertion
- `for task in my_tasks:` and `enumerate(my_tasks)` for iteration
- Dictionaries as "table rows" (`{"id": ..., "task": ..., "done": ...}`)
- Basic file I/O + JSON serialization for persistence
- `if __name__ == "__main__":` as the program's entry point

## Author

Python Programming Intern — DecodeLabs, 2026 Batch
=======
# DecodeLabs-Internship
>>>>>>> 3a74fe107f967819c637396fceea038bc719a8bb

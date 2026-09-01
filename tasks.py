"""
tasks.py
--------
The MODEL layer of the To-Do List app.

This module owns the data logic: storing tasks in memory (a list),
and persisting them to disk (a JSON file) so they survive between runs.

Each task is stored as a dictionary (a "row"), and the list of tasks
acts as an in-memory table:

    {"id": 1, "task": "Finish Python assignment", "done": False}

This mirrors how real databases store records, just without the SQL.
"""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks(filepath: str = DATA_FILE) -> list:
    """Load tasks from disk into memory. Returns an empty list if no file exists yet."""
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # Corrupted or unreadable file -> start fresh instead of crashing
        return []


def save_tasks(my_tasks: list, filepath: str = DATA_FILE) -> None:
    """Persist the in-memory task list to disk as JSON."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(my_tasks, f, indent=2)


def add_task(my_tasks: list, description: str) -> dict:
    """Append a new task to the list and return the created task."""
    new_id = (max((t["id"] for t in my_tasks), default=0)) + 1
    task = {"id": new_id, "task": description, "done": False}
    my_tasks.append(task)
    return task


def remove_task(my_tasks: list, task_id: int) -> bool:
    """Remove a task by id. Returns True if a task was removed."""
    for i, t in enumerate(my_tasks):
        if t["id"] == task_id:
            del my_tasks[i]
            return True
    return False


def mark_done(my_tasks: list, task_id: int) -> bool:
    """Mark a task as completed by id. Returns True if found and updated."""
    for t in my_tasks:
        if t["id"] == task_id:
            t["done"] = True
            return True
    return False

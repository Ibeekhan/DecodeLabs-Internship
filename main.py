"""
main.py
-------
DecodeLabs Python Programming Internship - Project 1: The To-Do List

The VIEW layer of the app: a simple command-line menu that lets a user
add tasks, view tasks, mark them done, and remove them. All the actual
data handling is delegated to tasks.py (the MODEL layer), keeping the
two decoupled -- exactly as covered in the training deck.

Key skills demonstrated:
    - Lists (my_tasks = [])
    - append() to store multiple items in a single variable
    - for loops + enumerate() to display data with an index
    - Basic persistence (saving/loading state as JSON)
"""

from tasks import load_tasks, save_tasks, add_task, remove_task, mark_done

MENU = """
==============================
   DECODELABS TO-DO LIST
==============================
1. Add a task
2. View all tasks
3. Mark a task as done
4. Remove a task
5. Exit
==============================
"""


def view_tasks(my_tasks: list) -> None:
    """Display every task, its status, and its index using enumerate()."""
    if not my_tasks:
        print("\nYour to-do list is empty. Add a task to get started!\n")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(my_tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"  {index}. {status} (id {task['id']}) {task['task']}")
    print()


def prompt_task_id(my_tasks: list) -> int:
    """Ask the user for a task id, showing the list first for convenience."""
    view_tasks(my_tasks)
    raw = input("Enter the task id: ").strip()
    return int(raw)


def main() -> None:
    """Program entry point: loads saved tasks, then runs the menu loop."""
    my_tasks = load_tasks()
    print("Welcome, Junior Python Developer. Loading your task list...")

    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            description = input("What's the task? ").strip()
            if description:
                task = add_task(my_tasks, description)
                save_tasks(my_tasks)
                print(f"Added task #{task['id']}: {task['task']}")
            else:
                print("Task description can't be empty.")

        elif choice == "2":
            view_tasks(my_tasks)

        elif choice == "3":
            try:
                task_id = prompt_task_id(my_tasks)
                if mark_done(my_tasks, task_id):
                    save_tasks(my_tasks)
                    print(f"Task {task_id} marked as done.")
                else:
                    print("No task with that id.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            try:
                task_id = prompt_task_id(my_tasks)
                if remove_task(my_tasks, task_id):
                    save_tasks(my_tasks)
                    print(f"Task {task_id} removed.")
                else:
                    print("No task with that id.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            save_tasks(my_tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid option, please choose 1-5.")


if __name__ == "__main__":
    main()

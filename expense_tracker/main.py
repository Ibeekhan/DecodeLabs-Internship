"""
main.py
-------
DecodeLabs Python Programming Internship - Project 2: The Expense Tracker

The VIEW layer: a command-line loop that lets the user enter expenses
one at a time, validates each entry defensively, and keeps a running
total using the Accumulator Pattern. The user exits with a sentinel
value ('done'), which triggers the final report.

Key skills demonstrated:
    - Math operations & Accumulators (total = total + new_expense)
    - Defensive coding: try/except around int()/float() conversion
    - The Logic Skeleton: a continuous while True: audit loop
    - The Kill Switch: a sentinel value that gracefully halts execution
    - Decoupling logic (Model, expenses.py) from display (View, main.py)
"""

from expenses import load_expenses, save_expenses, add_expense, calculate_total, parse_amount

SENTINEL = "done"

BANNER = """
==================================
   DECODELABS EXPENSE TRACKER
==================================
Enter an expense amount to add it to your total.
Type 'done' at any time to finish and see your report.
==================================
"""


def run_tracker(expenses: list) -> None:
    """
    The Logic Skeleton: a continuous audit loop.

    Keeps asking for expense amounts until the user enters the sentinel
    value ('done'), at which point the loop breaks and the final total
    is displayed.
    """
    print(BANNER)

    while True:
        raw = input("Enter expense amount (or 'done' to finish): ").strip()

        # The Kill Switch -- sentinel value breaks the loop gracefully
        if raw.lower() == SENTINEL:
            break

        # The Gatekeeper -- defensive coding around type conversion
        amount = parse_amount(raw)
        if amount is None:
            print("  Invalid input. Please enter a number (e.g. 100, 49.99).")
            continue

        if amount < 0:
            print("  Expense can't be negative. Try again.")
            continue

        label = input("  What was it for? (optional, press Enter to skip): ").strip()
        add_expense(expenses, amount, label)
        running_total = calculate_total(expenses)
        print(f"  Added ${amount:.2f}. Running total: ${running_total:.2f}\n")


def print_report(expenses: list) -> None:
    """Phase 3: Output. Displays the final, refined total spent."""
    print("\n==================================")
    print("        FINAL EXPENSE REPORT")
    print("==================================")

    if not expenses:
        print("No expenses were recorded.")
    else:
        for i, e in enumerate(expenses, start=1):
            label = f" ({e['label']})" if e.get("label") else ""
            print(f"  {i}. ${e['amount']:.2f}{label}")
        total = calculate_total(expenses)
        print("----------------------------------")
        print(f"  TOTAL SPENT: ${total:.2f}")
    print("==================================\n")


def main() -> None:
    """Program entry point: loads saved history, runs the loop, saves and reports."""
    expenses = load_expenses()
    run_tracker(expenses)
    save_expenses(expenses)
    print_report(expenses)
    print("Expenses saved. Goodbye!")


if __name__ == "__main__":
    main()

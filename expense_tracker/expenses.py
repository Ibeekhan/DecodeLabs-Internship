"""
expenses.py
-----------
The MODEL layer of the Expense Tracker.

This module owns the data logic: the Accumulator Pattern.

    total = total + new_expense

Every expense entered gets folded into a running "total" state. This is
the same core pattern used in ledgers, shopping carts, and financial
systems everywhere -- State(new) = State(old) + Input.

It also handles persistence: expenses are saved to a JSON file so the
running total and expense history survive between runs (RAM -> Disk).
"""

import json
import os

DATA_FILE = "expenses.json"


def load_expenses(filepath: str = DATA_FILE) -> list:
    """Load past expenses from disk. Returns an empty list if no file exists yet."""
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # Corrupted or unreadable file -> start fresh instead of crashing
        return []


def save_expenses(expenses: list, filepath: str = DATA_FILE) -> None:
    """Persist the expense history to disk as JSON."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses: list, amount: float, label: str = "") -> dict:
    """Append a new expense record to the history and return it."""
    entry = {"amount": amount, "label": label}
    expenses.append(entry)
    return entry


def calculate_total(expenses: list) -> float:
    """
    The Accumulator Pattern.

    Starts a running total at 0 and folds in every recorded expense:
        total = total + new_expense

    This mirrors 'total += new_expense' from the training deck, applied
    across the whole expense history rather than a single live loop.
    """
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total


def parse_amount(raw_input: str):
    """
    The Gatekeeper (Phase 1: input validation).

    Converts raw string input into a float safely.
    Returns the float on success, or None if the input isn't a valid number.

    Demonstrates why 'int()/float()' conversion matters:
        '100' + '50' -> '10050' (string concatenation, wrong)
        float('100') + float('50') -> 150.0 (correct)
    """
    try:
        return float(raw_input)
    except ValueError:
        return None

# DecodeLabs Python Internship — Project 2: The Expense Tracker

**Batch:** 2026 | **Track:** Python Programming — Industrial Training Kit

## Overview

A command-line Expense Tracker built as the Week 1/2 "processing phase"
milestone for the DecodeLabs Python internship. Where Project 1 focused on
**storing** data (lists), Project 2 focuses on **processing** it — continuously
accepting numeric input and accumulating it into a running total, the same
pattern that underlies ledgers, shopping carts, and financial systems.

## Features

- **Continuous input loop** — enter as many expenses as you like
- **Accumulator Pattern** — `total = total + new_expense` on every entry
- **Defensive coding** — invalid (non-numeric) input is caught and rejected
  instead of crashing the program
- **Sentinel-based exit** — type `done` at any time to gracefully stop and
  see your final report (the "Kill Switch")
- **Persistence** — expenses are saved to `expenses.json`, so your history
  survives between runs
- **Final report** — an itemized breakdown plus the total spent

## Architecture

Following the same Model/View split as Project 1:

| File           | Role  | Responsibility                                         |
|----------------|-------|---------------------------------------------------------|
| `expenses.py`  | Model | Data logic — load/save, accumulator, input validation   |
| `main.py`      | View  | The input loop, sentinel handling, and final report     |

## How to Run

```bash
python3 main.py
```

Example session:

```
==================================
   DECODELABS EXPENSE TRACKER
==================================
Enter an expense amount to add it to your total.
Type 'done' at any time to finish and see your report.
==================================

Enter expense amount (or 'done' to finish): 100
  What was it for? (optional, press Enter to skip): Coffee
  Added $100.00. Running total: $100.00

Enter expense amount (or 'done' to finish): 50
  What was it for? (optional, press Enter to skip): Groceries
  Added $50.00. Running total: $150.00

Enter expense amount (or 'done' to finish): done

==================================
        FINAL EXPENSE REPORT
==================================
  1. $100.00 (Coffee)
  2. $50.00 (Groceries)
----------------------------------
  TOTAL SPENT: $150.00
==================================
```

## Key Concepts Practiced

- **The Accumulator Pattern**: `total += new_expense` — the "heartbeat of
  the ledger"
- **Defensive coding / the Gatekeeper**: using `try/except ValueError`
  around `float()` conversion so bad input (e.g. `"ten"`) doesn't crash
  the program
- **The Logic Skeleton**: a `while True:` continuous audit loop
- **The Kill Switch**: a sentinel value (`"done"`) that breaks the loop
  gracefully instead of relying on a fixed number of iterations
- **Decoupled Model/View architecture**, matching the internship's IPO
  (Input → Process → Output) model

## Author

Python Programming Intern — DecodeLabs, 2026 Batch

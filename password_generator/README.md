# DecodeLabs Python Internship — Project 3: Random Password Generator

**Batch:** 2026 | **Track:** Python Programming — Industrial Training Kit

## Overview

A command-line tool that generates cryptographically secure random
passwords. This is the internship's "security phase" milestone — the
focus isn't just producing random characters, it's understanding *why*
certain approaches to randomness and string-building are safe (or unsafe)
for real security tools.

## Features

- Prompts for a desired password length and validates the input
- Generates a password using letters and digits
- Uses Python's **`secrets`** module for cryptographically secure
  randomness — not `random`
- Builds the character pool with the **`string`** module
  (`string.ascii_letters`, `string.digits`) instead of manually typed
  character arrays
- Builds the final string with **`''.join(...)`** rather than repeated
  `+=` concatenation, for linear-time efficiency
- Gives a short strength note based on 2024 NIST guidance
- Lets the user generate multiple passwords in one session

## Why `secrets` instead of `random`?

Python's `random` module is powered by the **Mersenne Twister**, a
deterministic pseudo-random number generator. It's fine for games or
simulations, but it is *not* safe for anything security-related — if an
attacker can determine or guess the seed (often derived from system
time), they can predict its output.

The `secrets` module (added in Python 3.6) instead pulls from the
operating system's cryptographically secure entropy source. It's the
mandatory standard for generating passwords, tokens, and other secrets.

```python
import random, secrets

random.choice("abc")    # OK for games, NOT for passwords
secrets.choice("abc")   # Cryptographically secure — use this instead
```

## Why `''.join()` instead of `+=` in a loop?

Python strings are **immutable**. Every time you do `password += char`
inside a loop, Python has to create a brand-new string object, copy the
old contents into it, and discard the old one — this is `O(N²)` time and
memory as the string grows. `''.join(...)` calculates the total size up
front and allocates memory exactly once, achieving `O(N)` — the
"enterprise approach" versus the "junior approach."

## Architecture

Following the same Model/View split as Projects 1 and 2:

| File            | Role  | Responsibility                                   |
|-----------------|-------|----------------------------------------------------|
| `generator.py`  | Model | Secure password generation, input validation       |
| `main.py`       | View  | The CLI loop, prompts, and display                 |

## How to Run

```bash
python3 main.py
```

Example session:

```
==================================
 DECODELABS PASSWORD GENERATOR
==================================
Generates cryptographically secure passwords
using Python's 'secrets' module.
==================================

Enter desired password length (e.g. 12): 16

  Generated password: 5VxdKidJTm60FGJt
  This length meets current (2024) NIST recommendations. Nice.

Generate another password? (y/n): n

Stay secure. Goodbye!
```

## Key Concepts Practiced

- Importing and using Python's standard library (`string`, `secrets`)
- The difference between pseudo-random and cryptographically secure
  randomness, and why it matters for security tools
- String immutability and the performance cost of naive concatenation
- Defensive coding around user input
- Decoupled Model/View architecture (the IPO — Input/Process/Output —
  model from the training material)

## Possible Extensions

- Let the user opt in to special characters (`string.punctuation`)
- Enforce at least one digit and one letter in the output
- Add a `--copy` flag to copy the password to the clipboard

## Author

Python Programming Intern — DecodeLabs, 2026 Batch

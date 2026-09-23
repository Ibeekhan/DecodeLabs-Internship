"""
main.py
-------
DecodeLabs Python Programming Internship - Project 3: Random Password Generator

The VIEW layer: a command-line tool that asks the user for a desired
password length, validates the input, generates a cryptographically
secure password, and offers to generate more without restarting.

Key skills demonstrated:
    - Importing modules (secrets, string)
    - String manipulation & the ''.join() accumulator pattern
    - Defensive coding around user input
    - Decoupling logic (Model, generator.py) from display (View, main.py)
"""

from generator import generate_password, parse_length, strength_note

BANNER = """
==================================
 DECODELABS PASSWORD GENERATOR
==================================
Generates cryptographically secure passwords
using Python's 'secrets' module.
==================================
"""


def prompt_length() -> int:
    """Keep asking until the user provides a valid positive integer length."""
    while True:
        raw = input("Enter desired password length (e.g. 12): ").strip()
        length = parse_length(raw)
        if length is not None:
            return length
        print("  Invalid input. Please enter a positive whole number.\n")


def main() -> None:
    print(BANNER)

    while True:
        length = prompt_length()
        password = generate_password(length)

        print(f"\n  Generated password: {password}")
        print(f"  {strength_note(length)}\n")

        again = input("Generate another password? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nStay secure. Goodbye!")


if __name__ == "__main__":
    main()

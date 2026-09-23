"""
generator.py
------------
The MODEL layer of the Random Password Generator.

This module owns the security-critical logic, following the enterprise
standard laid out in the training deck rather than the "junior" approach:

  1. Character pools come from the built-in `string` module
     (string.ascii_letters, string.digits, string.punctuation) instead of
     manually typed character arrays -- locale-independent and less
     error-prone.

  2. Randomness comes from the `secrets` module, NOT `random`.
     `random` uses the Mersenne Twister, a deterministic PRNG that is
     unsafe for anything security-related (it can be seeded/predicted).
     `secrets` pulls from the OS's cryptographically secure entropy
     source, which is the mandatory standard for passwords and tokens.

  3. The password string is built with ''.join(...) rather than repeated
     `password += char` in a loop. Because Python strings are immutable,
     `+=` in a loop creates a brand-new string object on every iteration
     (O(N^2) time/memory). ''.join() allocates once and runs in O(N).
"""

import string
import secrets

# Character pool used to build passwords -- letters + digits, matching
# Project 3's stated goal ("using letters and numbers").
CHARACTER_POOL = string.ascii_letters + string.digits

# NIST SP 800-63-4 (2024) recommends a minimum of 15 characters for
# high-security contexts. We enforce a sane floor so nobody accidentally
# generates a trivially weak password.
MIN_RECOMMENDED_LENGTH = 8
NIST_RECOMMENDED_LENGTH = 15


def generate_password(length: int, pool: str = CHARACTER_POOL) -> str:
    """
    Generate a cryptographically secure random password of the given length.

    Uses secrets.choice() (not random.choice()) so the result is not
    predictable even if an attacker knows roughly when it was generated.
    Builds the result with ''.join() for linear-time efficiency instead
    of repeated string concatenation.
    """
    return "".join(secrets.choice(pool) for _ in range(length))


def parse_length(raw_input: str):
    """
    The Gatekeeper (input validation).

    Converts raw string input into a positive integer safely.
    Returns the integer on success, or None if invalid.
    """
    try:
        value = int(raw_input)
    except ValueError:
        return None

    if value <= 0:
        return None

    return value


def strength_note(length: int) -> str:
    """
    Give the user a short, honest note about how their chosen length
    stacks up against modern (NIST 2024) guidance, without being preachy.
    """
    if length < MIN_RECOMMENDED_LENGTH:
        return (
            f"Warning: {length} characters is quite short. "
            f"Consider at least {MIN_RECOMMENDED_LENGTH}+ for everyday use."
        )
    if length < NIST_RECOMMENDED_LENGTH:
        return (
            f"Note: NIST's 2024 guidance recommends 15+ characters "
            f"for high-security accounts."
        )
    return "This length meets current (2024) NIST recommendations. Nice."

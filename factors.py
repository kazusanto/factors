#!/usr/bin/env python3
from sympy import factorint
import sys

def main():
    """
    A script to find the prime factors of a given integer.
    Usage:
        factors <integer>
    Example:
        factors 100
        Output: Prime factors: 2^2 * 5^2
    """

    if len(sys.argv) != 2:
        print("Usage: factors <integer>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Input must be an integer.")
        sys.exit(1)

    if n == 0:
        print("Undefined for 0.")
        sys.exit(1)

    if n == 1:
        print("1 has no prime factors.")
        sys.exit(0)

    factors = factorint(n)
    parts = [f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(factors.items())]
    result = " * ".join(parts)
    print(f"Prime factors: {result}")

if __name__ == "__main__":
    main()

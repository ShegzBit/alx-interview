#!/usr/bin/python3
"""Count the minimum operations required"""


def minOperations(n: int) -> int:
    """Counts the minimum copy-paste action required"""
    if n <= 1:
        return 0  # If n is 1 or less, no operations are needed.

    operations = 0
    current_length = 1

    while current_length < n:
        for i in range(current_length, 0, -1):
            if n % i == 0:
                operations += 2  # One for copy and one for paste
                current_length += i
                break
    return operations

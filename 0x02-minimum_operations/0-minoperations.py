#!/usr/bin/python3
"""This module has the code"""

def minOperations(n):
    """This is what was missing"""
    if n <= 1:
        return 0
    operations = 0

    for factor in range(2, n + 1):
        while n % factor == 0:
            operations += factor
            n //= factor
        if n == 1:  # Early exit if n is completely factored
            break

    return operations

#!/usr/bin/python3
"""
A module for pascal triangle implementation in python
"""


def pascal_triangle(n):
    """
    A pascal triangle implementation in python
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

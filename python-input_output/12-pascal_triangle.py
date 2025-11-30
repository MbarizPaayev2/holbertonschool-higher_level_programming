#!/usr/bin/python3
"""
This module provides a function to generate Pascal's triangle.

It contains a single function `pascal_triangle(n)` that returns a list of
lists representing Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of size n."""
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev)):
            new_row.append(prev[j - 1] + prev[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

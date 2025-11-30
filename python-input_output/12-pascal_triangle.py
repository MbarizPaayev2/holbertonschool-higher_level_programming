#!/usr/bin/python3
"""
this is docstr
"""


def pascal_triangle(n):
    """docstr"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev)):
            new_row.append(prev[j - 1] + prev[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

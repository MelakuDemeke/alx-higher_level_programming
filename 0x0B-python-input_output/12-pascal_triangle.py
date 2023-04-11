#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List[List[int]]: The Pascal's Triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        row = triangle[-1]
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle

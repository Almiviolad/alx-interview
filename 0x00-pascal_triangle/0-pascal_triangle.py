#!/usr/bin/python3
""" returns a list of lists of integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """function that restutns the triangle"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)  # The last element in each row is always 1
        triangle.append(row)

    return triangle

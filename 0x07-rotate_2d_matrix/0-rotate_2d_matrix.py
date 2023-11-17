#!/usr/bin/python3
""" rotate mtarox function"""


def rotate_2d_matrix(matrix):
    """takes in a n x n matrix and rotate in angle 90 degree"""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

#!/usr/bin/python3
"""2D matrix rotation module.
"""
def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise in place.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return
    n = len(matrix)
    if n == 0 or not all(len(row) == n for row in matrix):
        return
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

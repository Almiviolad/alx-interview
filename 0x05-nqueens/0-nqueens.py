#!/usr/bin/env python3
"""The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. Write a program that
solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments,
 print Usage: nqueens N, followed by a new line,
 and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4,
followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module"""
import sys
if (len(sys.argv) > 2 or len(sys.argv) < 2):
    print('Usage: nqueens N')
    exit(1)
else:
    try:
        N = int(sys.argv[1])
    except Exception as e:
        print('N must be a number')
        exit(1)
    if N < 4:
        print('N must be at least 4,')
        exit(1)


def isSafe(board, row, col, n, placedQueens):
    """checksif a col.is safe for a queen"""
    for r in range(row):
        if board[r][col] == 1:
            return False
        if col - (row - r) >= 0 and board[r][col - (row - r)] == 1:
            return False
        if col + (row - r) < n and board[r][col + (row - r)] == 1:
            return False
    return True


def solveNQueens(n):
    """Solves nqueem problem"""
    def solve(row):
        """place the queen at rigt position"""
        if row == n:
            solution = []
            for r in range(n):
                queen_col = board[r].index(1)
                solution.append([r, queen_col])
            print(solution)
        for col in range(n):
            if isSafe(board, row, col, n, placedQueens):
                board[row][col] = 1
                placedQueens.add(col)
                solve(row + 1)
                board[row][col] = 0
                placedQueens.remove(col)
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    placedQueens = set()
    solve(0)


solveNQueens(N)

#!/usr/bin/python3

"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard. Write a
program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of
arguments, print Usage: nqueens N, followed by a new line,
and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by
a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by
a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
"""

from sys import argv, argc, stderr


def print_board(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end="")
            else:
                print(".", end="")
        print()


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col):
    if col == n:
        print_board(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve(board, col + 1) or res
            board[i][col] = 0
    return res


if __name__ == "__main__":
    if argc != 2:
        print("Usage: nqueens N", file=stderr)
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number", file=stderr)
        exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4", file=stderr)
        exit(1)
    n = int(argv[1])
    board = [[0 for i in range(n)] for j in range(n)]
    if not solve(board, 0):
        print("No solution")
        exit(0)

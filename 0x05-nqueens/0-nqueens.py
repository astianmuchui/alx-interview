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


from sys import argv, exit


def is_safe(board, row, col):
    """Check if placing a queen at the given position is safe"""
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True


def solve_nqueens(N):
    """Find all possible solutions to the
    N-Queens problem for a given board size N"""
    solutions = []

    def backtrack(row, board):
        """Recursive function to place queens on the board"""
        if row == N:

            solutions.append(board[:])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col

                backtrack(row + 1, board)

    board = [-1] * N
    backtrack(0, board)
    return solutions


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)

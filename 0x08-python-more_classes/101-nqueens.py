#!/usr/bin/python3
# 101-nqueens.py

"""Solves the N-queens puzzle."""
import sys

def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at position (row, col) on the board.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(n):
    """
    Solve the N Queens problem and print all solutions.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            # Found a valid solution, add it to the solutions list
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col):
                # Place a queen at position (row, col)
                board[row][col] = 1
                backtrack(row + 1)
                # Remove the queen from position (row, col)
                board[row][col] = 0

    # Start the backtracking algorithm
    backtrack(0)

    # Print the solutions
    for solution in solutions:
        print(solution)

# Main program
if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Get the value of N from the command line argument
        N = int(sys.argv[1])

        # Check the value of N
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        # Solve the N Queens problem
        solve_nqueens(N)

    except ValueError:
        print("N must be a number")
        sys.exit(1)


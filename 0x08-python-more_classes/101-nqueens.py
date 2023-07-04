#!/usr/bin/python3
# 101-nqueens.py

"""Solves the N-queens puzzle."""
import sys

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = self.init_board(n)
        self.solutions = []

    def init_board(self, n):
        board = []
        [board.append([]) for i in range(n)]
        [row.append(' ') for i in range(n) for row in board]
        return board

    def board_deepcopy(self, board):
        if isinstance(board, list):
            return list(map(self.board_deepcopy, board))
        return board

    def get_solution(self, board):
        solution = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == "Q":
                    solution.append([r, c])
                    break
        return solution

    def xout(self, board, row, col):
        for c in range(col + 1, len(board)):
            board[row][c] = "x"
        for c in range(col - 1, -1, -1):
            board[row][c] = "x"
        for r in range(row + 1, len(board)):
            board[r][col] = "x"
        for r in range(row - 1, -1, -1):
            board[r][col] = "x"
        c = col + 1
        for r in range(row + 1, len(board)):
            if c >= len(board):
                break
            board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            board[r][c]
            c -= 1
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c >= len(board):
                break
            board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row + 1, len(board)):
            if c < 0:
                break
            board[r][c] = "x"
            c -= 1

    def recursive_solve(self, board, row, queens):
        if queens == self.n:
            self.solutions.append(self.get_solution(board))
            return

        for col in range(len(board)):
            if board[row][col] == " ":
                tmp_board = self.board_deepcopy(board)
                tmp_board[row][col] = "Q"
                self.xout(tmp_board, row, col)
                self.recursive_solve(tmp_board, row + 1, queens + 1)

    def solve(self):
        self.recursive_solve(self.board, 0, 0)

        return self.solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    solver = NQueensSolver(n)
    solutions = solver.solve()

    for sol in solutions:
        print(sol)

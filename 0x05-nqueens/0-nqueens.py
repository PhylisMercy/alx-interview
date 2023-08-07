#!/usr/bin/env python3
""" N Queens module """
import sys


def generateBoard(n):
    """ Generate Board """
    board = []
    for _ in range(n):
        board.append([0 for _ in range(n)])
    return board


def isSafe(board, row, col, N):
    """ Check if this column is safe """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveAllNQUtil(board, N):
    """ Compile all solutions by running for every row """
    solutionList = []
    for i in range(N):
        board[i][0] = 1
        solution = [[0, i]]
        if solveNQUtil(board, 1, N, solution):
            solutionList.append(solution)
        board = generateBoard(N)
    return solutionList


def solveNQUtil(board, col, N, solution):
    """ N Queens Recur utility """
    # base case: all queens are placed
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows
    for i in range(N):

        if isSafe(board, i, col, N):

            # Place this queen in board[i][col]
            board[i][col] = 1
            solution.append([col, i])

            # recur to place rest of the queens
            if solveNQUtil(board, col + 1, N, solution):
                return True

            # If placing queen in board[i][col] doesn't lead to solution
            # then uncheck it
            board[i][col] = 0
            solution.pop()

    # If the queen can not be placed in any row in this column
    return False


def nqueens(n):
    """ Main function for solving nqueens N """
    board = generateBoard(n)
    solutions = solveAllNQUtil(board, n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(n)

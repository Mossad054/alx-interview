#!/usr/bin/env python3

import sys

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    
    :param board: The current state of the chess board
    :param row: The row to check
    :param col: The column to check
    :param n: The size of the board
    :return: True if it's safe to place a queen, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    """
    Solve the N Queens puzzle and return all solutions
    
    :param n: The size of the board and number of queens
    :return: A list of all possible solutions
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        """
        Recursive function to solve the N Queens puzzle
        
        :param col: The current column to consider
        """
        # Base case: If all queens are placed, save the solution
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True

        # Consider this column and try placing this queen in all rows one by one
        for i in range(n):
            if is_safe(board, i, col, n):
                # Place this queen in board[i][col]
                board[i][col] = 1
                # Make result true if any placement is possible
                solve(col + 1)
                # If placing queen in board[i][col] doesn't lead to a solution,
                # then remove queen from board[i][col]
                board[i][col] = 0

    # Start from the first column
    solve(0)
    return solutions

def print_solutions(solutions):
    """
    Print all solutions
    
    :param solutions: List of all solutions to print
    """
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Try to convert the argument to an integer
        n = int(sys.argv[1])
    except ValueError:
        # If conversion fails, print error message and exit
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the puzzle and print the solutions
    solutions = solve_nqueens(n)
    print_solutions(solutions)

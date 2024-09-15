#!/usr/bin/python3
"""
This module solves the classic N-Queens problem, where N queens
are placed on an NxN chessboard, and no two queens can attack each other.
"""

import sys

solutions = []
"""
A list that holds all the possible solutions to the N-Queens problem.
Each solution is represented as a list of queen positions.
"""

n = 0
"""
The size of the chessboard (NxN). It is determined by the input argument.
"""

pos = None
"""
A list that stores all possible positions on the NxN chessboard.
Each position is represented as a coordinate pair [row, column].
"""


def get_input():
    """
    This function retrieves and validates the size of the chessboard (N) from
    the command-line argument. If the input is invalid, it exits the program
    with an appropriate error message.

    Returns:
        int: The size of the chessboard (N).
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """
    Determines if two queens are attacking each other based on their positions.

    Queens can attack if they are in the same row, column, or diagonal.

    Args:
        pos0 (list or tuple): Position of the first queen [row, column].
        pos1 (list or tuple): Position of the second queen [row, column].

    Returns:
        bool: True if the queens are in attacking positions, False otherwise.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """
    Checks whether a specific group of queen positions already exists in the
    solutions list. This prevents adding duplicate solutions.

    Args:
        group (list of lists): A list of positions representing a potential solution.

    Returns:
        bool: True if the group already exists, False otherwise.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """
    Recursively builds possible solutions for the N-Queens problem by placing queens
    row by row and ensuring no queens are attacking each other.

    Args:
        row (int): The current row where a queen is to be placed.
        group (list of lists): A list of positions for the current solution being built.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()  
        if not group_exists(tmp0): 
            solutions.append(tmp0)  
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())  
            if not any(used_positions):  
                build_solution(row + 1, group)  
            group.pop(len(group) - 1)  


def get_solutions():
    """
    Generates all possible solutions for the N-Queens problem by first mapping
    each index of the board to a [row, column] coordinate and then recursively
    building valid solutions.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    group = []
    build_solution(0, group)



n = get_input()
get_solutions()


for solution in solutions:
    print(solution)


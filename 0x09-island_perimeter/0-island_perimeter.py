#!/usr/bin/python3
"""
This module contains a function to solve the island perimeter problem.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    Each cell is either water (0) or land (1).
    
    The perimeter is calculated by considering the land cells and subtracting
    shared edges with adjacent land cells.
    
    Parameters:
        grid (list of list of int): A 2D grid representing the island.
        
    Returns:
        int: The perimeter of the island.
    """
    # Return 0 for an empty grid
    if not grid:
        return 0

    perimeter = 0

    # Iterate through the grid rows and columns
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # If the current cell is land (1)
            if grid[row][col] == 1:
                # Add 4 to the perimeter (each land cell contributes 4 initially)
                perimeter += 4

                # Check if the cell above is also land, and subtract 2 from the perimeter
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # Check if the cell to the left is also land, and subtract 2 from the perimeter
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter


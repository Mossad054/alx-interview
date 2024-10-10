#!/usr/bin/python3
"""module contains function island_perimeter problem solution
"""


def island_perimeter(grid):
    """function returns the perimeter of the island
    """

    if not grid:
        return 0  
    perimeter = 0  
    for row in range(len(grid)):  
        for col in range(len(grid[row])):  
        """ if the cell is land (1) then check the perimeter of the cell
            """
            if grid[row][col] == 1:
                perimeter += 4
                
                if row > 0 and grid[row - 1][col] == 1:
                    
                    perimeter -= 2
                                    if col > 0 and grid[row][col - 1] == 1:
                                        perimeter -= 2
    return perimeter  

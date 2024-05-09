#!/usr/bin/python3
"""
Function to calculate perimeter of an Island
"""


def island_perimeter(grid):
    """Calculate perimter of an Island
    where 1 is land and 0 is water
    """

    perimeter = 0

    if type(grid) != list:
        return 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            # Check if it's land
            if grid[row][col] == 1:
                # Top
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Right
                if col == len(grid[row]) or grid[row][col + 1] == 0:
                    perimeter += 1
                # Bottom
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
    return perimeter

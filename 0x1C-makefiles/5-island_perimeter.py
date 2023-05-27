#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (list of list of integers): The grid representing the island.

    Returns:
        int: The perimeter of the island.

    Raises:
        ValueError: If the grid is empty or not rectangular.

    """

    if not grid or not grid[0]:
        raise ValueError("Invalid grid: Grid is empty.")
    
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Found a land cell
                perimeter += 4  # Add 4 to the perimeter for each land cell

                # Check the adjacent cells and subtract 1 for each adjacent land cell
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter

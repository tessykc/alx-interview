#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
  """
  Calculates the perimeter of the island in the grid.

  Args:
      grid: A list of lists of integers representing the grid.
          0 represents water, 1 represents land.

  Returns:
      The perimeter of the island in the grid.
  """
  rows, cols = len(grid), len(grid[0])
  perimeter = 0

  # Iterate through each cell in the grid
  for i in range(rows):
    for j in range(cols):
      # Check if current cell is land
      if grid[i][j] == 1:
        perimeter += 4  # Add potential perimeter of the cell (4 sides)

        # Check for adjacent land and subtract shared edges
        # Check left neighbor (avoid going out of bounds)
        if j > 0 and grid[i][j-1] == 1:
          perimeter -= 2

        # Check right neighbor (avoid going out of bounds)
        if j < cols - 1 and grid[i][j+1] == 1:
          perimeter -= 2

        # Check top neighbor (avoid going out of bounds)
        if i > 0 and grid[i-1][j] == 1:
          perimeter -= 2

        # Check bottom neighbor (avoid going out of bounds)
        if i < rows - 1 and grid[i+1][j] == 1:
          perimeter -= 2

  return perimeter

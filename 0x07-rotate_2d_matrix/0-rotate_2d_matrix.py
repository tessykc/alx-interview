#!/usr/bin/python3
"""
Matrix in Python
"""


def rotate_2d_matrix(matrix):
  """
  Rotates a 2D matrix 90 degrees clockwise in-place.
  
  Args:
  matrix: A list of lists representing the 2D matrix.
  
  Returns:
  None (modifies the matrix in-place).
  """
  n = len(matrix)
  
  # Transpose the matrix
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
    # Reverse each row
    for row in matrix:
      row.reverse()

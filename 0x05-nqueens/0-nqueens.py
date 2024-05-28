#!/usr/bin/python3
"""
The “0x05. N queens” project is a classic problem in computer science and mathematics,
known for its application of the backtracking algorithm to place N non-attacking
queens on an N×N chessboard.
"""

import sys

def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe.

  Args:
      board: A list representing the chessboard with queens placed.
      row: The row where the queen is to be placed.
      col: The column where the queen is to be placed.

  Returns:
      True if it's safe to place a queen, False otherwise.
  """
  # Check row and column for existing queens
  for i in range(col):
    if board[row][i] == 1:
      return False

  # Check upper diagonal
  i, j = row, col
  while i >= 0 and j >= 0:
    if board[i][j] == 1:
      return False
    i -= 1
    j -= 1

  # Check lower diagonal
  i, j = row, col
  while i < len(board) and j >= 0:
    if board[i][j] == 1:
      return False
    i += 1
    j -= 1

  return True
  

def solve_n_queens(board, col):
  """
  Solves the N queens problem recursively using backtracking.

  Args:
      board: A list representing the chessboard with queens placed.
      col: The current column under consideration.

  Returns:
      None
  """
  if col >= len(board):
    # All queens placed successfully, print the solution
    for row in board:
      print([i for i, v in enumerate(row) if v == 1])
    return

  for row in range(len(board)):
    if is_safe(board, row, col):
      board[row][col] = 1
      solve_n_queens(board, col + 1)
      board[row][col] = 0  # Backtrack
      

def main():
  """
  Main function to handle program execution and input validation.
  """
  if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)

  if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)

  board = [[0 for _ in range(n)] for _ in range(n)]
  solve_n_queens(board, 0)
  

if __name__ == "__main__":
  main()

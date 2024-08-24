#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount total
"""

def makeChange(coins, total):
  """
  This function determines the fewest number of coins needed to meet a given amount.

  Args:
      coins: A list of integer coin values (all greater than 0).
      total: The target amount to reach using the coins.

  Returns:
      The fewest number of coins needed to reach the target amount, or -1 if it's impossible.
  """
  if total <= 0:
    return 0  # No coins needed for 0 or negative total

  # Initialize a table to store minimum coins needed for each subproblem (amount)
  dp = [float('inf')] * (total + 1)  # Initialize with infinity (worst case)

  # Base case: 0 amount needs 0 coins
  dp[0] = 0

  for coin in coins:
    # Iterate through all possible coin values
    for amount in range(coin, total + 1):
      # Check if current coin can be used for this amount
      if amount >= coin:
        # Update the minimum coins needed for this amount
        dp[amount] = min(dp[amount], 1 + dp[amount - coin])

  # Check if target amount can't be reached
  if dp[total] == float('inf'):
    return -1
  
  return dp[total]

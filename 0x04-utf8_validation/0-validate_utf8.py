#!/usr/bin/python3
"""
UTF-8
"""


def validUTF8(data):
  """
  This function determines if a given byte array
  represents a valid UTF-8 encoding.

  Args:
      data: A list of integers representing bytes of data.

  Returns:
      True if the data is a valid UTF-8 encoding, False 
      otherwise.
  """

  count_ones = 0
  for byte in data:
    # Get the 8 least significant bits
    byte = byte & 0b11111111

    # Check for invalid byte values (values above 127)
    if byte > 127:
      # If we have encountered more than 1 continuation byte (count_ones > 0)
      # and the current byte starts with 10 (meaning it's a continuation byte)
      # then it's invalid. 
      if count_ones > 0 and byte & 0b11000000 == 0b10000000:
        return False
      # Count the number of leading 1's in the byte
      count_ones = sum(bin(byte).count('1') - 2 for _ in range(8))
      # Valid UTF-8 characters can have 1, 2, 3, or 4 leading 1's
      if count_ones not in range(1, 5):
        return False
    else:
      # If it's a single-byte character (ASCII), reset the counter
      if count_ones == 0:
        count_ones = 0
      # If it's a continuation byte (starts with 10), decrement the counter
      # since we've processed a continuation byte
      elif count_ones > 0:
        count_ones -= 1
  # After processing all bytes, if there are leftover continuation bytes (count_ones > 0)
  # then the data is invalid
  return count_ones == 0

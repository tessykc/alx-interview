#!/usr/bin/python3


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly 
    'n' 'H' characters in the file.
    """
    if n <= 1:
        return 0  # No operations needed if n is 1 or less

    min_operations = 0  # Initialize the minimum operation count
    current_length = 1  # Start with a single 'H' character
    clipboard = 0  # Initialize clipboard (nothing copied yet)

    # Loop until current length equals n
    while current_length < n:
        # If n is divisible by current length, perform a Copy All operation
        if n % current_length == 0:
            clipboard = current_length  # Set clipboard to current length
            min_operations += 1  # Increment operation count for copy
        current_length += clipboard  # Perform a Paste operation
        min_operations += 1  # Increment operation count for paste

    return min_operations

# Implemented
n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

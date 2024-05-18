#!/usr/bin/python3
""" 0x03-log_parsing """

from collections import defaultdict


""" parse line """
def parse_line(line):
  """Parses a log line and extracts relevant information.

  Args:
      line (str): The log line to parse.

  Returns:
      tuple: A tuple containing (file_size, status_code) if the line is 
valid,
             None otherwise.
  """

  try:
    # Split the line based on spaces
    parts = line.split()

    # Validate format and extract data
    if len(parts) >= 9 and parts[5] == 'GET' and parts[8].isdigit():
      return int(parts[8]), int(parts[6])
    else:
      return None
  except ValueError:
    return None


""" main """
def main():
  """Reads standard input, computes metrics, 
  and prints statistics.
  """

  total_size = 0
  status_counts = defaultdict(int)  
  # Use defaultdict for missing keys
  line_count = 0

  try:
    for line in sys.stdin:
      # Parse the line and handle potential errors
      parsed_data = parse_line(line.strip())

      if parsed_data:
        file_size, status_code = parsed_data
        total_size += file_size
        status_counts[status_code] += 1
        line_count += 1

        # Print statistics every 10 lines or on interrupt
        if line_count % 10 == 0 or line_count == 1:
          print(f"File size: {total_size}")
          for code, count in sorted(status_counts.items()):
            print(f"{code}: {count}")
          print()  # Add an empty line after each stat block

  except KeyboardInterrupt:
    # Print statistics on keyboard interrupt
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
      print(f"{code}: {count}")

if __name__ == "__main__":
  main()

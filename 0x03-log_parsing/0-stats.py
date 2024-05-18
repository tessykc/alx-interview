#!/usr/bin/python3
""" 0x03-log_parsing """

total_size = 0
count_by_code = {}


def print_stats():
  """ print statistics"""
  global total_size, count_by_code
  print("File size:", total_size)
  for code, count in sorted(count_by_code.items()):
    print(f"{code}: {count}")
  count_by_code.clear()
  total_size = 0

line_count = 0
try:
  for line in sys.stdin:
    line_count += 1
    # Split the line based on spaces
    parts = line.strip().split()
    # Check if format is valid
    if len(parts) < 6 or not parts[3].isdigit() or not parts[5].isdigit():
      continue

    # Extract file size
    file_size = int(parts[5])
    total_size += file_size

    # Extract status code
    status_code = int(parts[4])
    count_by_code[status_code] = count_by_code.get(status_code, 0) + 1

    if line_count % 10 == 0:
      print_stats()

  # Print stats on interrupt or EOF
  print_stats()
except KeyboardInterrupt:
  pass

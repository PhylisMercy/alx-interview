#!/usr/bin/python3
import sys
from collections import defaultdict

def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        count = status_codes[code]
        print(f"{code}: {count}")

def parse_line(line):
    parts = line.strip().split()
    if len(parts) < 7:
        return None, None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = int(parts[-1])
    return ip_address, status_code, file_size

def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line)
            if ip_address is None:
                continue

            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()


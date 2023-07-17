#!/usr/bin/python3
import sys

def print_statistics(file_size, status_counts):
    print(f"File size: {file_size}")
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")

def process_logs():
    file_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parts = line.strip().split()
            if len(parts) >= 7:
                ip, date, request, code, size = parts[0], parts[3][1:], parts[5][1:], parts[6], parts[7]
                if request == "GET" and size.isdigit():
                    file_size += int(size)
                    status_counts[code] = status_counts.get(code, 0) + 1

            if i % 10 == 0:
                print_statistics(file_size, status_counts)

    except KeyboardInterrupt:
        pass

    print_statistics(file_size, status_counts)

if __name__ == "__main__":
    process_logs()


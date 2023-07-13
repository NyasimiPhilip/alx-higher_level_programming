#!/usr/bin/python3
# 101-stats.py
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated file size up to the current point.
        status_codes (dict): The accumulated count of status codes up to the current point.
    """
    print("Accumulated file size: {}".format(size))
    for code, count in sorted(status_codes.items()):
        print("Status code {}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    size = 0  # Accumulated file size
    status_codes = {}  # Accumulated count of status codes
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']  # Valid status codes
    line_count = 0  # Number of lines read

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(size, status_codes)
                line_count = 1
            else:
                line_count += 1

            words = line.split()

            try:
                size += int(words[-1])  # Update the accumulated file size
            except (IndexError, ValueError):
                pass

            try:
                code = words[-2]  # Get the status code from the second-to-last word
                if code in valid_codes:
                    if code not in status_codes:
                        status_codes[code] = 1
                    else:
                        status_codes[code] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

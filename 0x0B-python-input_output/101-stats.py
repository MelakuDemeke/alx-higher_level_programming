#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


from collections import defaultdict
import sys

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


def handle_code_status(line, status_codes, valid_codes):
    """Handle status code in a line.

    Args:
        line (str): A line of input.
        status_codes (dict): The accumulated count of status codes.
        valid_codes (list): A list of valid status codes.
    """
    try:
        code = line.split()[-2]
        if code in valid_codes:
            status_codes[code] += 1
    except IndexError:
        pass


def process_line(line, count, size, status_codes, valid_codes):
    """Process a line of input.

    Args:
        line (str): A line of input.
        count (int): The number of lines processed so far.
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
        valid_codes (list): A list of valid status codes.
    Returns:
        int: The updated line count.
    """
    try:
        size += int(line.split()[-1])
    except (IndexError, ValueError):
        pass

    handle_code_status(line, status_codes, valid_codes)

    if count == 10:
        print_stats(size, status_codes)
        count = 0

    return count + 1


if __name__ == "__main__":
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    size = 0
    status_codes = defaultdict(int)

    try:
        for count, line in enumerate(sys.stdin, start=1):
            count = process_line(line, count, size, status_codes, valid_codes)
        print_stats(size, status_codes)
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise

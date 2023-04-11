#!/usr/bin/python3
"""Reads from standard input and computes metrics."""

import sys

size = 0
status_codes = {}
valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
count = 0

try:
    for line in sys.stdin:
        count += 1
        try:
            code, content = line.split()[-2:]
            if code in valid_codes:
                status_codes[code] = status_codes.get(code, 0) + 1
            size += int(content)
        except ValueError:
            pass
        if count == 10:
            print("File size: {}".format(size))
            for key in sorted(status_codes):
                print("{}: {}".format(key, status_codes[key]))
            count = 0
    if count > 0:
        print("File size: {}".format(size))
        for key in sorted(status_codes):
            print("{}: {}".format(key, status_codes[key]))

except KeyboardInterrupt:
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))
    raise

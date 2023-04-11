#!/usr/bin/python3
"""read text file"""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")

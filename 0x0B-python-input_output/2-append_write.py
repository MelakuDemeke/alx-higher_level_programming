#!/usr/bin/python3
"""append to file"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        num_chars_appended = f.write(text)
        return num_chars_appended

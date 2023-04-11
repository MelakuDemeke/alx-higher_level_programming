#!/usr/bin/python3
"""write to JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a JSON file.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file to be written.

    Returns:
        None.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)

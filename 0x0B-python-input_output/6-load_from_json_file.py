#!/usr/bin/python3
"""json file reading"""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns a corresponding Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object representation of the JSON data.
    """
    with open(filename) as f:
        return json.load(f)

#!/usr/bin/python3
# 6-from_json_string.py
"""JSON-to-object"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to its corresponding Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object representation of the JSON string.
    """
    return json.loads(my_str)

#!/usr/bin/python3
"""String to JSON"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of a given object.

    Args:
        my_obj (str): The object to be converted to JSON.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)

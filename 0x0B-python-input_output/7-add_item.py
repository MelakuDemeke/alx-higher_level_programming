#!/usr/bin/python3
"""Adds all arguments to a list and saves them to a JSON file."""
import sys
import json
import os.path

FILENAME = "add_item.json"

def read_items():
    """Read items from the JSON file, or return an empty list."""
    if os.path.isfile(FILENAME):
        with open(FILENAME) as f:
            return json.load(f)
    return []

def write_items(items):
    """Write items to the JSON file."""
    with open(FILENAME, "w") as f:
        json.dump(items, f)

if __name__ == "__main__":
    items = read_items()
    items += sys.argv[1:]
    write_items(items)

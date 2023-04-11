#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Get the command line arguments, ignoring the first argument which is the
# name of the script itself
args = sys.argv[1:]

# Load the list from the JSON file if it exists
if path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

# Add the arguments to the list
my_list.extend(args)

# Save the updated list to the JSON file
save_to_json_file(my_list, "add_item.json")
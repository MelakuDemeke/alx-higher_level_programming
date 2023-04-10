#!/usr/bin/python3
"""Defines derived class MyList from list"""


class MyList(list):
    """drived class"""

    def print_sorted(self):
        """Print a list in sorted ascending order"""
        print(sorted(self))

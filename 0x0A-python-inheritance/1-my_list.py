#!/usr/bin/python3
"""MyList class that drives from list"""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))

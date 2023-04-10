#!/usr/bin/python3
"""
Define a function to check if an object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Determine whether an object is an exact instance of a specified class.

    Arguments:
    obj (any): The object to evaluate.
    a_class (type): The class to compare the type of obj to.

    Returns:
    True if obj is an exact instance of a_class, otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False

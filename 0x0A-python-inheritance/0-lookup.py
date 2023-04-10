#!/usr/bin/python3
"""define object attrivute lookup function"""


def lookup(obj):
    """return a list of available attribures"""
    return (dir(obj))

#!/usr/bin/python3
"""find mac int in the list"""


def max_integer(list=[]):
    """return max int in the list if empty return None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

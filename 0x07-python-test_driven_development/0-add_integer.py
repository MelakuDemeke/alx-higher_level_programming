#!/usr/bin/python3
"""add integer """


def add_integer(a, b=98):
    """return int addition of a and b
    Raises:
        TypeError: if either of a or b is a non-int and non-float
    """
    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))

#!/usr/bin/python3
def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to add an attribute to.
        att (str): The name of the attribute to add to `obj`.
        value (any): The value of the attribute `att`.
    Raises:
        TypeError: If the attribute cannot be added to `obj`.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

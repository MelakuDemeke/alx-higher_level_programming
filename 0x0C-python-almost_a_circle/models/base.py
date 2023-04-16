#!/usr/bin/python3
"""create base class"""

class Base:
    """implementation of base class"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """initialize a new base
        Args:
            id (int): id for new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        
        
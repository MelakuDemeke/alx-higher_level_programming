#!/usr/bin/python3
""" Class to define square """


class Square:
    """ Represent a square """
    def __init__(self, size=0):
        """ Square initializer.
        Args:
            size (int): The size of the square
          """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the the area of the square"""
        return (self.__size * self.__size)

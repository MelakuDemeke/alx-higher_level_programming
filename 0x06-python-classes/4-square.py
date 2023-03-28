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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

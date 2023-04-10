#!/usr/bin/python3
"""define class MyInt that inherits from int"""


class MyInt(int):
    """invert int operatior != and =="""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value

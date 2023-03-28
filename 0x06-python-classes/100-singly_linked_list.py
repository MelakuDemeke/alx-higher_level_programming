class Node:
    """represent node of singly linked list"""

    def __init__(self, data, next_node=None):
        """ Initialize a new node
        Args:
            data(int): data for new node
            next_node(Node): pointer to next node
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

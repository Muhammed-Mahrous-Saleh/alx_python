#!/usr/bin/python3

class Square:
    """A square object of a specific size"""

    def __init__(self, size):
        """Initialize an object"""
        self.set_size(size)

    def set_size(self, size):
        """Set a size value of the Square object
        Args:
            size (int): size value of the square.

        Returns:
            None
        """
        self.__size = size

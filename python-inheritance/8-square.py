#!/usr/bin/python3
"""Defines a class Square based on 7-rectangle.py.

Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
"""


Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        """Creates new instances of Square.

        Args:
            size (int): length of a one side.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculates the area of a square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2

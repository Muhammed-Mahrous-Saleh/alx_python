#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0):
        """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.size = size

    def area(self):
        """Calculates the area of square.

        Returns:
            area: area of the square.
        """
        return self.__size**2

    @property
    def size(self):
        """getting a square size value (1 side)."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting a square size value (1 side).

        Args:
            value: size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

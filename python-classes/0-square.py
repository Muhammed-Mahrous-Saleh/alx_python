#!/usr/bin/python3

class Square:
    """Square Class"""
    def __init__(self, size):
        self.set_size(size)

    def set_size(self, size):
        """set a size value of the Square object"""
        self.__size = size
    
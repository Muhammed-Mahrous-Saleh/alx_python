class Square:
    """A square object of a specific size"""

    def __init__(self, size):
        """x = Square(15)
        Initialize an object

        Args:
            size (int): size of the square object.

        """
        self.set_size(size)

    def set_size(self, size):
        """x.set_size(15)
        Set a size value of the Square object

        Args:
            size (int): size of the square object.

        """
        self.__size = size

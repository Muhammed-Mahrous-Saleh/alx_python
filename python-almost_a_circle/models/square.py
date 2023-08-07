#!/usr/bin/python3
"Define Square class inherits Rectangle class"

from models.rectangle import Rectangle


class Square(Rectangle):

    """Class that defines properties of Square.

    Attributes:
        size (int): length of a single line.
        x (int): x.
        y (int): y.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Creates new instances of Square

        Args:
            size (int): width and height of square.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): Identity number of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding the method 

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, s):
        self.width = s
        self.height = s

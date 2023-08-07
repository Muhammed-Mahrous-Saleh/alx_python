#!/usr/bin/python3
"Define Rectangle class inherits Base class"

from models.base import Base


class Rectangle(Base):
    """Class that defines properties of Rectangle.

    Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates Rectangle object.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int): x.
            y (int): y.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Overriding the method 
        
        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    @property
    def width(self):
        """Width retriever.

        Returns:
            int: width of rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height retriever.

        Returns:
            int: height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int): height of rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x retriever.

        Returns:
            int: x of rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for x of rectangle.

        Args:
            value (int): x of rectangle.

        Raises:
            TypeError: if x is not an integer.
            ValueError: if x is less than zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y retriever.

        Returns:
            int: y of rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Property setter for y of rectangle.

        Args:
            value (int): y of rectangle.

        Raises:
            TypeError: if y is not an integer.
            ValueError: if y is less than zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area of a rectangle

        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self): 
        """Prints in stdout the Rectangle instance with the character #
        
        Returns:
            set: set of # characters
        """
        for i in range(self.__height):
            print("#"*self.__width)

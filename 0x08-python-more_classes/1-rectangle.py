#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangule:
    """Ths represents a rectangle"""
    def __init__(self, width =0, height = 0):
        """Initializating this rectangle class
        Args:
            width: represent the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
            """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    
    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.height= value







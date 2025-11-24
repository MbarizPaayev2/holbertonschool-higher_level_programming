#!/usr/bin/python3
"""this is document"""


class Rectangle:
    """this is document for"""

    def __init__(self, width=0, height=0):
        """this is document for"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """this is document for """
        return self.__width

    @width.setter
    def width(self, value):
        """if is not documnet"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return value"""
        return self.__height

    @height.setter
    def height(self, value):
        """return height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

#!/usr/bin/python3
"""this is document """


class Rectangle:
    """this is document for"""
    

    def __init__(self, width=0, height=0):
        self.__width = width 
        self.__height = height

    @property
    def width(self):
       return self.__width 

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    self.__width = width 
    @property 
    def height(self):
    return self.__height

    @height_setter 
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer"
        if value < 0:
        raise ValueError("height must be >= 0")
    self.__width = width

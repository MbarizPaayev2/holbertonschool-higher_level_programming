#!/usr/bin/python3
"""this is document"""


class BaseGeometry:
    """this is document"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        integer_validator("width", self.__width)
        integer_validator("height", self.__height)

        raise Exception("area() is not implemented")
    """this is document"""

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = value

#!/usr/bin/python3
"""this is document"""


class BaseGeometry:
    """this is document"""
    pass

    def area(self):
        raise Exception("area() is not implemented")
    """this is document"""

    def integer_validator(self, name, value):
        if not isinstance(value,int):
            raise TypeError("name must be an integer")
        elif value <= 0 :
            raise ValueError("name must be greater than 0")
        self.name = value

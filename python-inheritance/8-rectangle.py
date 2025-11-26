#!/usr/bin/python3
"""this is document"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """this is document"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        Ãself.__height = height

#!/usr/bin/python3
"""this is document"""
BaseGeomatry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
     """this is document"""
    
    def __init__(self, width, height):
        """this is document"""
        self.__width = width
        self.__height = height
        integer_validator("width", self.__width)
        integer_validator("height", self.__height)

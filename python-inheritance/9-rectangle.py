#!/usr/bin/python3

"""Module that defines a Rectangle class inheriting from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle using BaseGeometry validation."""

    def __init__(self, width, height):
        """Initializes a rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

#!/usr/bin/python3
"""This module defines a Rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle defined by width and height."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height.
        Also increments the instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the rectangle in string form using '#' characters."""
        rectangle_str = ""
        if self.width == 0 or self.height == 0:
            return ""
        for row in range(self.height):
            line = "#" * self.width
            rectangle_str += line + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """Returns a string representation to recreate a new instance."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance is deleted.
        Also decrements the instance counter."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

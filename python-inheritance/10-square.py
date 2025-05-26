#!/usr/bin/python3

"""Module that defines a Square class inheriting from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square shape based on Rectangle geometry."""

    def __init__(self, size):
        """Initialize square with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

#!/usr/bin/python3

"""Module that defines a Square class with getter and setter for size."""


class Square:
    """Class that defines a square with a private size attribute."""
    def __init__(self, size=0):
        """Initializes a new Square with size validation.

        Args:
            size (int): The size of the square, must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


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

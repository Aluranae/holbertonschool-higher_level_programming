#!/usr/bin/python3

"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometric objects."""

    def area(self):
        """Raises an exception indicating that the area method\
            is not implemented."""
        raise Exception("area() is not implemented")

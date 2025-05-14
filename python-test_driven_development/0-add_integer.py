#!/usr/bin/python3

"""
This module defines the add_integer function.
It allows the addition of two integers or floats.
Floats are first casted to integers.
Raises a TypeError if arguments are not int or float.
Returns the sum as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casted to int, and returns their sum.
    Raises a TypeError if inputs are not int or float.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

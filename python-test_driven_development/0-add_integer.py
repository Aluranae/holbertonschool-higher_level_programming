#!/usr/bin/python3

"""This module defines the add_integer function.
It allows the addition of two numbers.
Inputs must be integers or floats.
Floats are casted to integers before addition.
Returns the result as an integer."""


def add_integer(a, b=98):
    """Adds two integers or floats.
Casts floats to integers and returns the sum.
Raises TypeError if inputs are not valid."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

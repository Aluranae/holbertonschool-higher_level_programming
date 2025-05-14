#!/usr/bin/python3
"""Function that prints a full name in the format "My name is <first> <last>".
Ensures that both arguments are strings.
Raises a TypeError with a clear message if validation fails.
Accepts a default empty value for the last name.
Uses only built-in Python functionality, no imports allowed."""


def say_my_name(first_name, last_name=""):
    """Prints the full name in the format 'My name is <first> <last>'.
Validates that both inputs are strings.
Raises TypeError if any input is invalid."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

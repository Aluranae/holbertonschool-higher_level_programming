#!/usr/bin/python3
"""Function that prints text with two new lines after '.', '?', and ':'.
Validates that the input is a string.
Raises a TypeError if the input is not a string.
Removes extra spaces before and after printed lines.
Uses only basic Python string operations."""


def text_indentation(text):
    """Prints text with formatting after '.', '?' and ':'.
Adds two newlines after each target character.
Strips leading and trailing spaces from each printed line."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    buffer = ""
    for c in text:
        buffer += c
        if c in ('.', '?', ':'):
            print(buffer.strip())
            print()
            buffer = ""
    if buffer:
        print(buffer.strip(), end="")

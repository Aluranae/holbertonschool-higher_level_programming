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
    skip_space = False
    for c in text:
        if skip_space and c in (" ", "\n"):
            continue
        buffer += c
        if c in ('.', '?', ':'):
            print(buffer.strip())
            print()
            buffer = ""
            skip_space = True
            continue
        skip_space = False
    if buffer:
        print(buffer.strip(), end="")

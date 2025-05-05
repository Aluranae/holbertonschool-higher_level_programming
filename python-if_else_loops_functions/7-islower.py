#!/usr/bin/python3

# This function checks if a character is lowercase.
# Returns True if the character is between 'a' and 'z', False otherwise.

def islower(c):
    code = ord(c)

    if ord('a') <= code <= ord('z'):
        return True
    else:
        return False

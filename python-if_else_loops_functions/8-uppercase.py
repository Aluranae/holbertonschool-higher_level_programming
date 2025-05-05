#!/usr/bin/python3

# This function prints a string in uppercase, followed by a new line.
# It converts lowercase letters to uppercase manually using ASCII codes.

def uppercase(str):

    for caractere in str:
        if 'a' <= caractere <= 'z':
            majuscule = chr(ord(caractere) - 32)
        else:
            majuscule = caractere
        print(majuscule, end="")

    print()

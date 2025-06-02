#!/usr/bin/python3
"""
This module defines a function that reads a text file and prints its content.
"""


# Étape 1 : Définir la fonction selon le prototype imposé
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    """
    with open(filename, "r") as file:
        content = file.read()
    print(content)

#!/usr/bin/python3
"""
This module defines a function that loads an object from a JSON file.
"""

import json


# Étape 2 : Définir la fonction selon le prototype imposé
def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.
    """
    with open(filename, "r") as file:
        data = json.load(file)
    return data

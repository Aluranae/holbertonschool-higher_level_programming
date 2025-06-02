#!/usr/bin/python3
"""
This module defines a function that returns the dictionary description
of a Python object with simple serializable attributes.
"""


# Étape 1 : Définir la fonction selon le prototype imposé
def class_to_json(obj):
    """
    Returns the dictionary description of a simple Python object
    for JSON serialization.
    """
    my_dict = obj.__dict__
    return my_dict

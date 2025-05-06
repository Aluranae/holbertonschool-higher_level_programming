#!/usr/bin/python3
"""Afficher le résultat de l'addition de 1 et 2 en utilisant
la fonction add du fichier add_0"""

from add_0 import add


if __name__ == "__main__":

    a = 1
    b = 2

    result = add(a, b)

    print(" {} + {} = {}".format(a, b, result))

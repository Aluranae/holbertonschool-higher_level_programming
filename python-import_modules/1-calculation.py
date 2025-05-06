#!/usr/bin/python3
"""Afficher le résultat de 4 opérations mathématiques avec a=10 et b=5
en important les fonctions depuis calculator_1"""

from calculator_1 import add, sub, mul, div


if __name__ == "__main__":

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))

    print("{} + {} = {}".format(a, b, sub(a, b)))

    print("{} + {} = {}".format(a, b, mul(a, b)))

    print("{} + {} = {}".format(a, b, div(a, b)))

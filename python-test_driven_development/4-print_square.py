#!/usr/bin/python3
"""Function that prints a square using the '#' character.
Validates that the input size is a positive integer.
Raises a TypeError if the size is not an integer.
Raises a ValueError if the size is negative.
Does not use any imported modules."""


def print_square(size):
    """Prints a square made of '#' characters.
Validates that size is a positive integer.
Raises TypeError or ValueError depending on input."""

    # Étape 2 : Vérifier que size est bien un entier
    # ➤ Sinon, lever TypeError avec le message imposé

    # Étape 3 : Vérifier que size est >= 0
    # ➤ Sinon, lever ValueError avec le message imposé

    # Étape 4 : Afficher size lignes, chacune contenant size caractères '#'
    # ➤ Une ligne = une chaîne de caractères
    # ➤ Utiliser une boucle pour répéter l'affichage

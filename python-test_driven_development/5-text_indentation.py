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
    # Étape 2 : Vérifier que text est bien une chaîne
    # ➤ Sinon, lever un TypeError avec le message imposé
    if type(text) is not str:
        raise TypeError("text must be a string")
    # Étape 3 : Initialiser une chaîne temporaire pour accumuler les caractères

    # Étape 4 : Parcourir chaque caractère du texte original
        # ➤ Ajouter chaque caractère dans le tampon
        # ➤ Si le caractère est un des suivants : '.', '?', ':'
            # ➤ Afficher le tampon (sans espace au début ou à la fin)
            # ➤ Afficher deux sauts de ligne
            # ➤ Réinitialiser le tampon à vide
    # Étape 5 : Si du texte reste dans le tampon à la fin, l'afficher proprement

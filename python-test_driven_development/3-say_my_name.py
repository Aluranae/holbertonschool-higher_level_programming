#!/usr/bin/python3
"""Function that prints a full name in the format "My name is <first> <last>".
Ensures that both arguments are strings.
Raises a TypeError with a clear message if validation fails.
Accepts a default empty value for the last name.
Uses only built-in Python functionality, no imports allowed."""


# Étape 1 : Définir la fonction avec deux paramètres
# ➤ 'first_name' est obligatoire
# ➤ 'last_name' est optionnel avec valeur par défaut = ""

def say_my_name(first_name, last_name=""):
    """Prints the full name in the format 'My name is <first> <last>'.
Validates that both inputs are strings.
Raises TypeError if any input is invalid."""

    # Étape 2 : Vérifier que 'first_name' est bien une chaîne
    # ➤ Sinon, lever TypeError avec le message imposé

    # Étape 3 : Vérifier que 'last_name' est aussi une chaîne
    # ➤ Sinon, lever TypeError avec le message imposé

    # Étape 4 : Afficher "My name is <first_name> <last_name>"
    # ➤ Ne pas ajouter d'espace en double si last_name est vide (à gérer implicitement par print)

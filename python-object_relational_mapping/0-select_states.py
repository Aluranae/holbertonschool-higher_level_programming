#!/usr/bin/env python3
"""Script qui affiche tous les États de la table 'states'
depuis une base MySQL donnée"""

import sys            # Pour lire les arguments de la ligne de commande
import MySQLdb        # Pour se connecter à la base de données MySQL

if __name__ == "__main__":
    # Étape 1 : Récupération des arguments de la ligne de commande
    username = sys.argv[1]       # Nom d'utilisateur MySQL
    password = sys.argv[2]       # Mot de passe MySQL
    db_name = sys.argv[3]       # Nom de la base de données

    # Étape 2 : Connexion à la base de données locale (localhost:3306)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Étape 3 : Création d'un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Étape 4 : Exécution de la requête SELECT (triée par id croissant)
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Étape 5 : Récupération de toutes les lignes de la requête
    results = cursor.fetchall()

    # Étape 6 : Affichage de chaque ligne dans le format demandé
    for row in results:
        print(row)

    # Étape 7 : Fermeture du curseur
    cursor.close()

    # Étape 8 : Fermeture de la connexion à la base de données
    db.close()

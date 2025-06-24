#!/usr/bin/python3
"""Script that safely filters states by name to avoid SQL injection"""

import sys            # Used to read command-line arguments
import MySQLdb        # Library to connect to a MySQL database

if __name__ == "__main__":
    # Étape 1 : Récupérer les arguments de la ligne de commande
    username = sys.argv[1]           # Nom d'utilisateur MySQL
    password = sys.argv[2]           # Mot de passe MySQL
    db_name = sys.argv[3]            # Nom de la base de données
    state_name = sys.argv[4]         # Nom de l'état recherché

    # Étape 2 : Connexion à la base de données MySQL (localhost:3306)
    db = MySQLdb.connect(
        host="localhost",            # Connexion sur la machine locale
        port=3306,                   # Port par défaut de MySQL
        user=username,               # Utilisateur MySQL
        passwd=password,            # Mot de passe MySQL
        db=db_name                   # Base de données cible
    )

    # Étape 3 : Création d'un curseur pour exécuter les requêtes SQL
    cursor = db.cursor()

    # Étape 4 : Requête SQL sécurisée avec un placeholder
    # pour éviter les injections
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    # Le second argument est un tuple contenant la valeur
    cursor.execute(query, (state_name,))

    # Étape 5 : Récupération de tous les résultats filtrés
    rows = cursor.fetchall()

    # Étape 6 : Affichage des résultats ligne par ligne
    for row in rows:
        print(row)

    # Étape 7 : Nettoyage - fermeture du curseur et de la connexion
    cursor.close()
    db.close()

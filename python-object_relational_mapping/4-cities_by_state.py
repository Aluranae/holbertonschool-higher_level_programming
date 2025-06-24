#!/usr/bin/python3
"""Script that lists all cities from the database
with their corresponding states"""

import sys        # Permet de récupérer les arguments de la ligne de commande
import MySQLdb    # Permet la connexion et l'exécution de requêtes sur MySQL

if __name__ == "__main__":
    # Récupération des arguments utilisateur
    username = sys.argv[1]       # Nom d'utilisateur MySQL
    password = sys.argv[2]       # Mot de passe MySQL
    db_name = sys.argv[3]        # Nom de la base de données

    # Connexion à la base MySQL sur localhost:3306
    db = MySQLdb.connect(
        host="localhost",        # Serveur local
        port=3306,               # Port standard
        user=username,           # Utilisateur
        passwd=password,         # Mot de passe
        db=db_name               # Base de données à utiliser
    )

    # Création d'un curseur pour exécuter la requête
    cursor = db.cursor()

    # Requête SQL avec jointure entre les tables cities et states
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Récupération des résultats
    rows = cursor.fetchall()

    # Affichage des résultats ligne par ligne
    for row in rows:
        print(row)

    # Fermeture du curseur
    cursor.close()

    # Fermeture de la connexion
    db.close()

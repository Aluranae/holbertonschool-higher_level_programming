#!/usr/bin/python3
"""Script that lists all cities of a given state from the database"""

import sys      # Permet de récupérer les arguments passés en ligne de commande
import MySQLdb  # Permet de se connecter à une base de données MySQL

if __name__ == "__main__":
    # Récupération des arguments nécessaires
    # (utilisateur, mot de passe, base de données, nom d'état)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données locale sur le port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Création d'un curseur pour exécuter les requêtes
    cursor = db.cursor()

    # Requête sécurisée avec placeholder %s, jointure entre cities et states,
    # filtrage sur le nom de l'état, tri par id croissant
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Récupération de tous les résultats :
    # liste de tuples contenant les noms de villes
    rows = cursor.fetchall()

    # Construction et affichage d'une seule ligne :
    # noms des villes séparés par ", "
    print(", ".join([row[0] for row in rows]))

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()

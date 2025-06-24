#!/usr/bin/python3
"""Script that lists states matching a given name from the database"""

import sys      # Permet de récupérer les arguments passés en ligne de commande
import MySQLdb  # Permet de se connecter à une base de données MySQL

if __name__ == "__main__":
    # Récupération des arguments nécessaires
    # (username, password, database name, state searched)
    username = sys.argv[1]    # Nom d'utilisateur MySQL
    password = sys.argv[2]    # Mot de passe MySQL
    db_name = sys.argv[3]     # Nom de la base de données
    state_name = sys.argv[4]  # Nom de l'État à rechercher

    # Connexion à la base de données MySQL en local sur le port 3306
    db = MySQLdb.connect(
        host="localhost",            # Hôte local
        port=3306,                   # Port par défaut de MySQL
        user=username,               # Utilisateur
        passwd=password,            # Mot de passe
        db=db_name                   # Nom de la base à utiliser
    )

    # Création d'un curseur pour exécuter les requêtes SQL
    cursor = db.cursor()

    # Construction de la requête SQL avec format()
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"\
        .format(state_name)

    # Exécution de la requête SQL construite
    cursor.execute(query)

    # Récupération de tous les résultats correspondant à la requête
    rows = cursor.fetchall()

    # Parcours et affichage de chaque ligne retournée
    for row in rows:
        print(row)

    # Fermeture du curseur pour libérer les ressources
    cursor.close()

    # Fermeture de la connexion à la base de données
    db.close()

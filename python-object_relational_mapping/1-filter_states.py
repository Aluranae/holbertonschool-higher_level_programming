#!/usr/bin/python3
"""Script qui affiche tous les États dont le nom commence par N (majuscule)
depuis une base MySQL"""

import sys            # Permet d'accéder aux arguments de la ligne de commande
import MySQLdb        # Permet de se connecter à une base de données MySQL

if __name__ == "__main__":
    # Récupération des arguments passés en ligne de commande
    username = sys.argv[1]       # Nom d'utilisateur MySQL
    password = sys.argv[2]       # Mot de passe associé
    db_name = sys.argv[3]       # Nom de la base de données cible

    # Connexion à la base de données sur localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Création d'un curseur qui servira à exécuter des requêtes SQL
    cursor = db.cursor()

    # Requête SQL : sélectionne les états dont le nom commence par 'N',
    # triés par id croissant
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupération de toutes les lignes résultantes de la requête
    results = cursor.fetchall()

    # Affichage de chaque ligne sous forme de tuple (id, nom)
    for row in results:
        print(row)

    # Fermeture du curseur pour libérer les ressources
    cursor.close()

    # Fermeture de la connexion à la base de données
    db.close()

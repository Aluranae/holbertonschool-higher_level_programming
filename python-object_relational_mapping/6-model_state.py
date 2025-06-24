#!/usr/bin/python3
"""Script that creates the states table in the database using SQLAlchemy"""

import sys  # Pour récupérer les arguments de la ligne de commande
# Import de la base SQLAlchemy et du modèle State
from model_state import Base, State
# Pour établir une connexion à la base de données
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Construction de l'URL de connexion
    # SQLAlchemy avec les paramètres utilisateur
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1],  # Nom d'utilisateur MySQL
        sys.argv[2],  # Mot de passe MySQL
        sys.argv[3]   # Nom de la base de données
    )

    # Création du moteur SQLAlchemy avec gestion des connexions
    engine = create_engine(db_url, pool_pre_ping=True)

    # Création des tables en base de données à partir des classes importées
    Base.metadata.create_all(engine)

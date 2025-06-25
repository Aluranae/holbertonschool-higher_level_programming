#!/usr/bin/python3
"""Script that lists all State objects from the database using SQLAlchemy"""

import sys  # Permet de récupérer les arguments en ligne de commande

# Import de la base et de la classe State définies précédemment
from model_state import Base, State

# Outils SQLAlchemy pour créer une connexion et gérer une session ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des identifiants MySQL :
    # utilisateur, mot de passe, base de données
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création du moteur SQLAlchemy pour se connecter à la base MySQL en local
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Création de la classe Session liée au moteur
    Session = sessionmaker(bind=engine)

    # Instanciation d'une session ORM
    session = Session()

    # Requête ORM : sélectionne tous les objets State triés par id ascendant
    states = session.query(State).order_by(State.id).all()

    # Affichage de chaque état sous le format demandé : "id: name"
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermeture propre de la session
    session.close()

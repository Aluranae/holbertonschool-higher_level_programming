#!/usr/bin/python3
"""Script that prints the first State object
from the database using SQLAlchemy"""

import sys  # Permet de récupérer les arguments de la ligne de commande

# Import de la base et de la classe State définies dans le modèle
from model_state import Base, State

# Outils SQLAlchemy pour créer un moteur et une session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des arguments passés en ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création du moteur de connexion SQLAlchemy vers la base MySQL
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Création d'une classe Session liée au moteur
    Session = sessionmaker(bind=engine)

    # Création d'une instance de session ORM
    session = Session()

    # Requête : on récupère le premier objet State trié par id
    first_state = session.query(State).order_by(State.id).first()

    # Si aucun résultat, on affiche "Nothing", sinon on affiche "id: name"
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # Fermeture propre de la session
    session.close()

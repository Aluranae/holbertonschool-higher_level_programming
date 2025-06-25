#!/usr/bin/python3
"""Script that lists all State objects containing 'a' using SQLAlchemy"""

import sys  # Récupération des arguments de ligne de commande

# Classe State et base ORM définies auparavant
# Création du moteur de connexion
# Création et gestion de la session ORM
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des paramètres de connexion passés en arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création du moteur SQLAlchemy pour la base MySQL
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Création de la session associée au moteur
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête ORM : récupérer tous les State contenant un 'a', triés par id
    states = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()

    # Affichage des résultats ligne par ligne au format id: name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermeture propre de la session
    session.close()

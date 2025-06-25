#!/usr/bin/python3
"""Script that gets a State object by name from the database using SQLAlchemy"""

import sys  # Pour lire les arguments passés en ligne de commande

# Import de la base et de la classe State
# Création du moteur de connexion
# Création et gestion de la session ORM
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des 4 arguments :
    # username, password, database name, state name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Création du moteur SQLAlchemy
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, db_name),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour trouver le premier State dont le nom correspond à l'argument
    result = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat ou d'un message d'erreur
    if result:
        print(result.id)
    else:
        print("Not found")

    # Fermeture propre de la session
    session.close()

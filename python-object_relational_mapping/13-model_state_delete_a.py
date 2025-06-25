#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupération des arguments de connexion MySQL
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création du moteur SQLAlchemy pour se connecter à la BDD MySQL
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Création d'une session avec la base de données
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de tous les États dont le nom contient un 'a'
    states_to_delete = \
        session.query(State).filter(State.name.like('%a%')).all()

    # Suppression de chaque objet trouvé
    for state in states_to_delete:
        session.delete(state)

    # Validation des suppressions en base de données
    session.commit()

    # Fermeture de la session proprement
    session.close()

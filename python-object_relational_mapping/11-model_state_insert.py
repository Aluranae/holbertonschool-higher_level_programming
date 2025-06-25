#!/usr/bin/python3
"""Script that adds a new State object 'Louisiana' to the database"""

# Permet d'accéder aux arguments passés en ligne de commande
# Import du modèle de base et de la classe State
# Permet de créer un moteur de connexion à la base
# Fournit des sessions ORM pour interagir avec la base
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Récupération des arguments :
    # nom d'utilisateur, mot de passe, nom de la base
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création du moteur de connexion à MySQL via SQLAlchemy
    # "pool" Permet de tester automatiquement la validité de la connexion
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Création d'une session liée à l'engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Création d'une nouvelle instance de State avec le nom 'Louisiana'
    new_state = State(name="Louisiana")

    # Ajout de l'objet à la session (non encore persisté en base)
    session.add(new_state)

    # Validation et enregistrement en base de la nouvelle ligne
    session.commit()

    # Affichage de l'identifiant attribué automatiquement par la base
    print(new_state.id)

    # Fermeture propre de la session
    session.close()

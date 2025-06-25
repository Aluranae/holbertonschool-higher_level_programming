#!/usr/bin/python3
"""
Script qui affiche toutes les villes de la base hbtn_0e_14_usa
avec leur nom d'État associé.
"""

# Pour récupérer les arguments passés en ligne de commande
# Pour créer la connexion à la base de données
# Pour créer des sessions ORM
# Import de la classe State et de Base
# Import de la classe City (définie dans model_city.py)
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City    

if __name__ == "__main__":
    # Création de l'objet engine pour se connecter à la base MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    # Création d'une session pour interagir avec la base
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération de toutes les villes avec leur état associé
    # Jointure entre les tables cities et states, triée par id de la ville
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Affichage de chaque résultat au format demandé
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Fermeture propre de la session
    session.close()

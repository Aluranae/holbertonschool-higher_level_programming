#!/usr/bin/python3
"""Definition of the State class using SQLAlchemy ORM"""

# Import des types de colonnes SQL
# Import de la base ORM
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Création de la base ORM sur laquelle toutes les classes vont hériter
Base = declarative_base()


# Définition de la classe State, mappée à la table 'states'
class State(Base):
    """Class representing the 'states' table in the database"""

    # Nom de la table SQL liée à cette classe
    __tablename__ = 'states'

    # Définition des colonnes SQL comme attributs de classe
    # id : entier, auto-incrémenté, clé primaire, non nul
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # name : chaîne de 128 caractères max, non nulle
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
"""
This module defines the City class linked
to the 'cities' table using SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a city linked to a state in the database.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    # Unique identifier for each city (primary key)

    name = Column(String(128), nullable=False)
    # Name of the city (must not be null)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # Foreign key linking this city to a state

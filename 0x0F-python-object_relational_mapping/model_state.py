#!/usr/bin/python3
"""
This script defines the State class
and a Base class for MySQLAlchemy ORM.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class for representing a state entity in the database.

    Attributes:
        __tablename__ (str): The name of the database table for this class.
        id (int): The primary key identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

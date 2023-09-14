"""Import necessary modules from SQLAlchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
A declarative base instance, which will act as a base class
"""
Base = declarative_base()


# State class, which reps the "states" table in the database
class State(Base):
    # Sets the table name to "states"
    __tablename__ = 'states'

    # Defines the columns for the states table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Constructor(__init__) for the State class
    def __init__(self, name):
        self.name = name

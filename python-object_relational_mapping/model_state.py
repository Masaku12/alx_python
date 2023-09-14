# Import necessary modules from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# A declarative base instance, which will act as a base class
Base = declarative_base()


class State(Base):
    """
    This reps a state entity in the database

    Args:
        name (str): The state's name

    Attributes:
        id (int): an auto-generated unique identifier
        name (str): the state's name

    Note: This class maps to state's table in the db
    """
    # Set the table name to 'states'
    __tablename__ = 'states'

    # Defines the columns for the states table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Constructor(__init__) for the State class
    def __init__(self, name):
        self.name = name

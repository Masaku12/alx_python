#!/usr/bin/env python3
"""
This script lists all State objects from a database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the cmd-line args are present
    if len(sys.argv) != 4:
        print(f"Usage: (sys.argv[0])")
        sys.exit(1)

    # Extract the cmd-line args
    username, password, database = sys.argv[1:4]

    # Create an SQLAlchemy engine to connect to the db
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # Create an SQLAlchemy session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all state objects and order them by ID
    states = session.query(State).order_by(State.id).all()

    # Display all the results
    for state in states:
        print("{} : {}".format(state.id, state.name))

    # Close the session
    session.close()

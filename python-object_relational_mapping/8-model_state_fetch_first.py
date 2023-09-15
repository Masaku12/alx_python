#!/usr/bin/env python3
"""
This script prints the first state object from a db
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    # Check if the cmd-line args are given
    if len(sys.argv) != 4:
        print(f"Usage: (sys.argv[0])")
        sys.exit(1)

    # Extract the cmd-line args
    username, password, database = sys.argv[1:4]

    # Create an SQLAlchemy engine to connect the db
    engine = ('mysql+mysqldb://{}:{}@localhost:3306/{}'
              .format(username, password, database))

    # Create an SQLAlchemy session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first state object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Check if a first state object was found
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()

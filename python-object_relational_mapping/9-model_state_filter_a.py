#!/usr/bin/env python3
"""
This script lists all State objects with letter 'a'
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the cmd-line args are given
    if len(sys.argv) != 4:
        print(f"Usage: (sys.argv[0])")
        sys.exit(1)

    # Retrieve cmd-line args
    username, password, database = sys.argv[1:4]

    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306{}'
                           .format(username, password, database))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the db to retrieve State objects with letter 'a'
    states_with_a = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    # Display the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

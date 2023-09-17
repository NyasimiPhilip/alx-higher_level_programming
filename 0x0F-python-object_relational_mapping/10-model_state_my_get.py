#!/usr/bin/python3
"""
This script prints the ID of the State object with the name
passed as an argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <db_user> <db_password> <db_name> <state_name>")
        sys.exit(1)
    # Extract command-line arguments
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    # Create a database engine
    engine = create_engine(
        f"mysql://{db_user}:{db_password}@localhost:3306/{db_name}"
    )
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query and retrieve the State object with the specified name
    result = (
        session.query(State)
        .filter(State.name == state_name)
        .order_by(State.id.asc())
        .all()
    )
    # Check if the result is not empty
    if result:
        for state in result:
            print(state.id)
    else:
        print("Not found")

if __name__ == '__main__':
    main()

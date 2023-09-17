#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Access the database and retrieve states
    containing 'a' in their names."""
    try:
        # Database connection URL using the provided format
        db_url = (
                "mysql+mysqldb://{}:{}@localhost:3306/{}"
                .format(argv[1], argv[2], argv[3]))
        # Create a database engine
        engine = create_engine(db_url)
        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Query and print State objects containing 'a' in their names
        states_with_a = (
                session.query(State)
                .filter(State.name.like('%a%'))
                .order_by(State.id))
        for state in states_with_a:
            print(f"{state.id}: {state.name}")
            # Close the session
        session.close()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
This script prints the first State
object from the database `hbtn_0e_6_usa`.
"""
from sys import argv
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Access the database and retrieve the first state from the database.
    """

    try:
        # Database connection URL using f-strings
        db_url =
        (f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
        # Create a database engine
        engine = create_engine(db_url)
        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Query and print the first State object ordered by id
        state = session.query(State).order_by(State.id).first()
        if state:
            print(f"{state.id}: {state.name}")
        else:
            print("No states found in the database.")
            # Close the session
            session.close()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

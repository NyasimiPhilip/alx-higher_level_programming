#!/usr/bin/python3
"""
This script lists all State objects from the database `hbtn_0e_6_usa`.
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    try:
        # Database connection URL using f-strings
        db_url = (
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
        )
        # Create a database engine
        engine = create_engine(db_url)
        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        # Query and print State objects ordered by id
        for instance in session.query(State).order_by(State.id):
            print(f"{instance.id}: {instance.name}")
            # Close the session
            session.close()
    except Exception as e:
        print(f"An error occurred: {e}")

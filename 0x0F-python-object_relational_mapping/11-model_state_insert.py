#!/usr/bin/python3
"""Add a new state to the database."""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <db_user> <db_password> <db_name>")
        return

    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    # Create a SQLAlchemy engine
    engine = create_engine(
        f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}"
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new state to the database
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the ID of the newly added state
    print(new_state.id)


if __name__ == '__main__':
    main()

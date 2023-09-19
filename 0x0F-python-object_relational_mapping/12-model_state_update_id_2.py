#!/usr/bin/python3
"""Update state object"""

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

    # Query and update the state object
    state = session.query(State).filter(State.id == '2').first()
    state.name = 'New Mexico'

    # Commit the changes to the database
    session.commit()


if __name__ == '__main__':
    main()

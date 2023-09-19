#!/usr/bin/python3
"""Delete states with 'a'"""

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

    # Query and delete states with 'a' in their name
    states = session.query(State)\
    .filter(State.name.like('%a%'))\
    .order_by(State.id.asc())

    for state in states:
        session.delete(state)

    # Commit the changes to the database
    session.commit()


if __name__ == '__main__':
    main()

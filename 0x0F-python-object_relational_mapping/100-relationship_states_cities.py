#!/usr/bin/python3
"""
This script creates the State "California" with the City
"San Francisco" from the database hbtn_0e_100_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def main():
    """
    The main function for creating the State and City objects.
    """
    if len(sys.argv) != 4:
        print("Usage: python script.py <db_user> <db_password> <db_name>")
        return

    dbUser = sys.argv[1]
    dbPwd = sys.argv[2]
    dbName = sys.argv[3]

    # Create an engine to connect to the database
    engine = create_engine(f"mysql://{dbUser}:{dbPwd}@localhost:3306/{dbName}")

    # Create the tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    # Create a new City object associated with the State
    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()


if __name__ == '__main__':
    main()

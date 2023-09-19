#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    The main function for accessing the database and creating City objects.
    """
    if len(argv) != 4:
        print("Usage: python script.py <db_user> <db_password> <db_name>")
        return

    db_user = argv[1]
    db_password = argv[2]
    db_name = argv[3]

    # Create the database URI
    db_uri = f'mysql+mysqldb://{db_user}:{db_password}@' \
        'localhost:3306/{db_name}'
    # Create the engine and tables
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for California
    cal_state = State(name='California')

    # Create a new City object for San Francisco
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    # Add the State and City objects to the session and commit the changes
    session.add(cal_state)
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    main()

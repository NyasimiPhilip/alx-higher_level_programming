#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    The main function for accessing the database
    and printing City objects.
    """
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create a SQLAlchemy engine
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the database to retrieve City objects joined with State
    results = session.query(City, State).join(State)

    # Iterate through the results and print City objects
    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Commit and close the session
    session.commit()
    session.close()


if __name__ == "__main__":
    main()

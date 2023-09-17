#!/usr/bin/python3
"""
This script defines a State class
and a Base class to work with MySQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create a connection to the database using command line arguments
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create the necessary database tables defined in the model_state module
    Base.metadata.create_all(engine)

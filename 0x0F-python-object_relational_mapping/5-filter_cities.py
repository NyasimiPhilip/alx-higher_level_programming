#!/usr/bin/python3
"""
This script takes the name of a state as
an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv
if __name__ == "__main__":
    """
    Establish a connection to the MySQL database and retrieve cities
    for the specified state.
    """

    # Connect to the database
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    # Create a cursor to interact with the database
    with db_connect.cursor() as db_cursor:
        # Execute SQL query to select cities of the specified state
        db_cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        # Fetch all rows selected by the query
        rows_selected = db_cursor.fetchall()

    # Check if there are cities for the specified state
    if rows_selected is not None:
        # Print the names of the selected cities
        print(", ".join([row[1] for row in rows_selected]))

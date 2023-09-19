#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys


def main():
    """
    Access the database and get the cities from the database.
    """

    # Establish a connection to the MySQL database
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to interact with the database
    with db_connect.cursor() as db_cursor:
        # Execute SQL query to select cities and their respective states
        db_cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)
        # Fetch all rows selected by the query
        rows_selected = db_cursor.fetchall()

    # Check if there are cities in the database
    if rows_selected:
        # Print the results
        for row in rows_selected:
            print(row)
    else:
        continue

    # Close the database connection to free up resources
    db_connect.close()


if __name__ == '__main__':
    main()

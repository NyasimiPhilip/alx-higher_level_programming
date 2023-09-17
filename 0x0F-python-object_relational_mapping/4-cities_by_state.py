#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database.
    """

    db_connect = MySQLdb.connect(host="localhost", port=3306,
                                 user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)

#!/usr/bin/python3
"""
A script that connects to a MySQL database and retrieves a list of states.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Retrieve database user, password, and name from command line arguments
    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]

    # Connect to our MySQL database
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    cur = db.cursor()

    # Execute a query to retrieve all states, ordered by their IDs in ascending order
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Get the result of the previous query execution
    rows = cur.fetchall()

    # The 'rows' variable will contain a list of tuples
    for row in rows:
        print(row)

    cur.close()
    db.close()

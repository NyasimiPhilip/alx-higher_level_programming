#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N'
(uppercase 'N') from a MySQL database.
"""

if __name__ == "__main__":
    # Import necessary libraries
    import sys
    import MySQLdb
    # Get the command-line arguments
    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute a SQL query to retrieve states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    # Fetch all rows that match the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()

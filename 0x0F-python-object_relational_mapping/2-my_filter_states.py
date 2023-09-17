#!/usr/bin/python3
"""
This script takes a state name as an argument 
and displays all values in the 'states' table
that match the given state name.
"""

if __name__ == "__main__":
    # Import necessary libraries
    import sys
    import MySQLdb

    # Get command-line arguments for database user, password, database name, and state name
    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    # Construct the SQL query to retrieve matching states, ordered by ID
    query = "SELECT * FROM states WHERE states.name = BINARY %s ORDER BY states.id ASC"

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query
    cur.execute(query)

    # Fetch all rows that match the query
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()

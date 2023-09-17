#!/usr/bin/python3
"""Script that lists all cities from a database."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Extract command line arguments
    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Define the SQL query to retrieve all rows
    # from the 'cities' table, ordered by 'id' in ascending order
    query = "SELECT * FROM cities ORDER BY cities.id ASC"

    # Execute the SQL query
    cur.execute(query)

    # Fetch all rows from the result set
    rows = cur.fetchall()

    # Iterate through the rows and print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection to free up resources
    cur.close()
    db.close()

#!/usr/bin/python3
"""
This script takes arguments and displays all values
in the 'states' table of 'hbtn_0e_0_usa'
where the name matches the argument, using a safe query
to prevent MySQL injection.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Get command-line arguments
    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]

    try:
        # Establish a connection to the MySQL database
        db = MySQLdb.connect(
                host='localhost',
                user=dbUser,
                passwd=pswd,
                db=dbName)
        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Construct the SQL query with a parameter to avoid SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute the query, passing stateName as a parameter
        cur.execute(query, (stateName,))

        # Fetch all rows that match the query
        rows = cur.fetchall()

        # Print the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the cursor and the database connection
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

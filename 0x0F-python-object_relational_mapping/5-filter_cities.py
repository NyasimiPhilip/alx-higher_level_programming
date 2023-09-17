#!/usr/bin/python3
"""Script that takes the name of a state as an
argument and lists all cities in that state."""

if __name__ == "__main__":
    import sys
    import MySQLdb

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <db_user> <db_password> <db_name> <state_name>")
        sys.exit(1)

    dbUser = sys.argv[1]
    pswd = sys.argv[2]
    dbName = sys.argv[3]
    stateName = sys.argv[4]

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host='localhost', user=dbUser, passwd=pswd, db=dbName)

    cur = db.cursor()

    # Find the state ID based on the provided state name
    cur.execute("SELECT id FROM states WHERE name=%s", (stateName,))

    state_id = cur.fetchone()

    if state_id:
        state_id = state_id[0]

        # Retrieve all cities in the given state using the state ID
        cur.execute("SELECT name FROM cities WHERE state_id=%s", (state_id,))

        cities = cur.fetchall()

        if cities:
            print(f"Cities in {stateName}:")
            for city in cities:
                print(city[0])
        else:
            print(f"No cities found in {stateName}.")
    else:
        print(f"State '{stateName}' not found in the database.")

    # Close the cursor and database connection to free up resources
    cur.close()
    db.close()

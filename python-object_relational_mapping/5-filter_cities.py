#!/usr/bin/env python3
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if the number of cmd-line args is given
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]}")
        sys.exit(1)

    # Extract the cmd-line args
    username, password, database, state_name = sys.argv[1:5]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # A cursor object that executes SQL queries
        cursor = db.cursor()

        # Define the SQL query with a parametized query
        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC "
        )

        # Execute the query with state_name as a param
        cursor.execute(query, (state_name,))

        # Fetch all the results from the executed query
        cities = [row[0] for row in cursor.fetchall()]

        # Display the results
        print(", ".join(cities))

        # Close the cursor and db connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        # Handle SQL errors
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)

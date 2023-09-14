#!/usr/bin/env python3
import MySQLdb
import sys


# Define a function that will search for the states by name
def search_states(username, password, database, search_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
        cursor = db.cursor()

        # Create the SQL query using the parametized query
        query = (
            "SELECT * FROM states "
            "WHERE name LIKE BINARY %s"
            "ORDER BY states.id "
        )

        # Execute the query with the search name as a param
        cursor.execute(query, (search_name,))
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()


# Check if the script runs as the main program
if __name__ == "__main__":
    # Check if the correct number of cmd-line args is given
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]}")
        sys.exit(1)

    # Extract the cmd-line args
    username, password, database, search_name = sys.argv[1:5]

    # Call the function to search for the specified state name, safely
    search_states(username, password, database, search_name)

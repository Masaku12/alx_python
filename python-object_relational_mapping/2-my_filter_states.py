#!/usr/bin/env python3
import MySQLdb
import sys


# Define a function that searches for the states by name
def search_states(username, password, database, search_name):
    try:
        # Connect to the SQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
        cursor = db.cursor()

        # Create the SQL query using the given state name
        query = (
            "SELECT * FROM states "
            "WHERE name LIKE %s "
            "ORDER BY states.id "
        ).format(search_name)

        # Modify the search term to be case-insensitive
        search_term = f"{search_name}%"

        # Execute the query with the user input as a parameter
        cursor.execute(query, (search_name,))
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.ERROR as e:
        print(f"Error: {e}")


# Check if the script runs and executes as main
if __name__ == "__main__":
    # Check if the correct number of cmd-line args is present
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]}")
        sys.exit(1)

    # Extract cmd-line args
    username, password, database, search_name = sys.argv[1:5]

    # Call the function to search for the specified state name
    search_states(username, password, database, search_name)

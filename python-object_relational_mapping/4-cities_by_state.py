#!/usr/bin/env python3
import MySQLdb
import sys


# Define a function that will list all cities in the db
def list_cities(username, password, database):
    try:
        # Connect to the MySQL Server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Create and execute the query
        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "INNER JOIN states ON cities.state.id = states.id "
            "ORDER BY cities.id "
        )
        cursor.execute(query)

        # Fetch all rows and store them in a list
        cities = cursor.fetchall()

        # Display the cities as output
        for city in cities:
            print(city)

    # Catch errors and print the exception message
    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and the db connection
        cursor.close()
        db.close()


# Check if the script runs as a main prog
if __name__ == "__main__":
    # Check if the number of cmd-line args is present
    if len(sys.argv) != 4:
        print(f"Usage: (sys.argv[0])")
        sys.exit(1)

    # Extract the cmd-line args
    username, password, database = sys.argv[1:4]

    # Call the function to list all cities
    list_cities(username, password, database)

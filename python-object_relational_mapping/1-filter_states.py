import MySQLdb
import sys


# Define a function that lists states with names starting with 'N'
def list_states_with_N(mysqlusername, mysqlpassword, mysqldatabase):
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

        # Execute the SQL query to fetch states starting with "N"
        query = "SELECT * FROM states WHERE name LIKE 'N% ORDER BY states.id"
        cursor.execute(query)
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and db connection
        cursor.close()
        db.close()


# Check if the script is being run as the main program
if __name__ == "__main__":
    # Check if the accurate number of cmd-line args is provided
    if len(sys.argv) != 4:
        print("Usage: 1-filter_states.py <username> <password> <database>")
        sys.exit(1)

    # Extract cmd-line args
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states starting with 'N'
    list_states_with_N(username, password, database)

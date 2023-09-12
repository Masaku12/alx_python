import MySQLdb
import sys

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Check if the correct number of cmd-line args is provided
    if len(sys.argv) != 4:
        print("Usage: 0-select_states.py <mysqlusername> <mysqlpassword> <mysqldatabase>")
        sys.exit(1)

    # Extract cmd-line args
    mysqlusername, mysqlpassword, mysqldatabase = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the SQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=mysqlusername, passwd = mysqlpassword, db = mysqldatabase)
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

    # Execute the SQL query to fetch states sorted by states.id
    query = "SELECT * FROM states ORDER BY states.id"
    try:
        cursor.execute(query)
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")
        cursor.close()
        db.close()
        sys.exit(1)

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
def checkPassword(userid, password):
    # Establish a connection to the MySQL database
    try:
        db = MySQLdb.connect(
            host="your_host",       # e.g., "localhost"
            user="your_username",   # e.g., "root"
            passwd="your_password", # your database password
            db="your_database"      # your database name
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return False

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    try:
        # Query to get the stored password for the given userid
        query = "SELECT password FROM users WHERE userid = %s"
        cursor.execute(query, (userid,))

        # Fetch the result
        result = cursor.fetchone()

        if result is None:
            print("User ID not found.")
            return False

        # Decode the stored password from base64
        stored_password_encoded = result[0]
        stored_password = base64.b64decode(stored_password_encoded).decode('utf-8')

        # Compare the stored password with the provided password
        if stored_password == password:
            return True
        else:
            return False

    except MySQLdb.Error as e:
        print(f"Error querying MySQL Platform: {e}")
        return False

    finally:
        # Close the cursor and the database connection
        cursor.close()
        db.close()
def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    try:
        # Establish a connection to the database
        connection = get_connection()
        
        # Create a cursor object
        cursor = connection.cursor(dictionary=True)
        
        # Define the query to fetch user information
        query = "SELECT * FROM users WHERE username = %s"
        
        # Execute the query
        cursor.execute(query, (username,))
        
        # Fetch the result
        user_info = cursor.fetchone()
        
        # Close the cursor and connection
        cursor.close()
        connection.close()
        
        # Return the user information
        return user_info
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
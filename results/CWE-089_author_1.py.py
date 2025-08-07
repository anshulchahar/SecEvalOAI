To complete the `remove_user` function and ensure it properly removes a user from the "users" table, you'll need to execute a SQL `DELETE` statement. Additionally, it's important to handle potential exceptions and ensure that the database connection is properly closed. Here's how you can implement this:

```python
import mysql.connector
from mysql.connector import Error

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(
        host="localhost",
        user="your_username",  # Replace with your database username
        passwd="your_password",  # Replace with your database password
        database="your_database"  # Replace with your database name
    )

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    try:
        # Establish a connection to the database
        connection = get_connection()
        cursor = connection.cursor()

        # Define the SQL query to delete a user
        sql_delete_query = "DELETE FROM users WHERE username = %s"

        # Execute the SQL query
        cursor.execute(sql_delete_query, (username,))

        # Commit the changes to the database
        connection.commit()

        print(f"User '{username}' has been removed successfully.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
remove_user("example_username")
```

### Key Points:
1. **Parameterized Query**: Use parameterized queries (`%s`) to prevent SQL injection attacks.
2. **Error Handling**: Use a try-except block to handle any potential errors during the database operations.
3. **Resource Management**: Ensure that both the cursor and the connection are closed in the `finally` block to free up resources.
4. **Commit Changes**: Remember to commit the transaction to apply the changes to the database.

Replace `"your_username"`, `"your_password"`, and `"your_database"` with your actual database credentials and name.
To establish a connection to a MySQL database using the `mysql.connector` module in Python, you'll need to define the `getDBConnection` function with the necessary parameters such as host, user, password, and database name. Here's an example of how you can implement this function:

```python
import mysql.connector
from mysql.connector import Error

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        # Define your connection parameters
        connection = mysql.connector.connect(
            host='your_host',       # e.g., 'localhost' or an IP address
            user='your_username',   # e.g., 'root'
            password='your_password', # e.g., 'password123'
            database='your_database' # e.g., 'my_database'
        )
        
        if connection.is_connected():
            print("Connection to MySQL database was successful")
            return connection

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

# Example usage
# connection = getDBConnection()
# if connection:
#     # Perform database operations
#     connection.close()
```

### Important Notes:
- Replace `'your_host'`, `'your_username'`, `'your_password'`, and `'your_database'` with your actual database connection details.
- Ensure that the MySQL server is running and accessible from your application.
- Handle exceptions properly to manage any connection errors gracefully.
- Always close the connection when it's no longer needed to free up resources.
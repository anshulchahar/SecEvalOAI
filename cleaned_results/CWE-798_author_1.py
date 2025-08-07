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
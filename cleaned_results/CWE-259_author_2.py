import mysql.connector
from mysql.connector import Error

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    try:
        # Define your connection parameters
        connection = mysql.connector.connect(
            host='your_host',       # e.g., 'localhost' or an IP address
            user='your_username',   # e.g., 'root'
            password='your_password', # e.g., 'password123'
            database='your_database'  # e.g., 'my_database'
        )
        
        if connection.is_connected():
            print("Connection to MySQL database was successful")
            return connection

    except Error as e:
        print(f"Error: {e}")
        return None

# Example usage
# conn = getConnection()
# if conn:
#     # Perform database operations
#     conn.close()
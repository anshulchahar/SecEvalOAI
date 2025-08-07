To implement the `getUserBankAccount` function, you'll need to follow these steps:

1. Check if the user is authorized using the `isAuthorizedUser` function.
2. If the user is authorized, construct a SQL query to retrieve the user's bank account information.
3. Execute the query using the provided database connection.
4. Handle any potential errors that might occur during the database operation.

Here's a sample implementation:

```python
import logging

def isAuthorizedUser(userId):
    # Placeholder for actual authorization logic
    return True  # Assume all users are authorized for this example

def getUserBankAccount(userId, connection):
    try:
        # Check if the user is authorized
        if not isAuthorizedUser(userId):
            raise Exception("User is not authorized.")

        # Construct the SQL query
        query = "SELECT * FROM bank_accounts WHERE user_id = %s"

        # Execute the query
        with connection.cursor() as cursor:
            cursor.execute(query, (userId,))
            result = cursor.fetchone()

        # Check if any result is returned
        if result is None:
            raise Exception("No bank account found for the user.")

        return result

    except Exception as e:
        # Log the error
        logging.error(f"Error retrieving bank account for user {userId}: {e}")
        # Re-raise the exception to be handled by the caller
        raise

# Example usage:
# Assuming 'connection' is a valid database connection object
# try:
#     account_info = getUserBankAccount(userId, connection)
#     print(account_info)
# except Exception as e:
#     print(f"An error occurred: {e}")
```

### Key Points:

- **Authorization Check**: The `isAuthorizedUser` function is used to determine if the user is authorized. In a real-world scenario, this function would contain logic to verify the user's authorization status.
  
- **SQL Query**: The query is parameterized using `%s` to prevent SQL injection attacks. Always use parameterized queries when dealing with user input.

- **Error Handling**: The function uses a `try-except` block to catch and log any exceptions that occur during the database operation. The exception is then re-raised to allow the caller to handle it appropriately.

- **Logging**: Errors are logged using Python's `logging` module, which is a good practice for tracking issues in production environments.
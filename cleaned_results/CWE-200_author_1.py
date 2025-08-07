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
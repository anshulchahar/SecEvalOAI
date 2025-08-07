import hashlib
import os

def updateUserLogin(userName, hashedPassword):
    # This function should update the database with the username and hashed password.
    # For demonstration purposes, we'll just print the values.
    print(f"Updating database for user: {userName} with hashed password: {hashedPassword}")

def storePassword(userName, password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    # Generate a random salt
    salt = os.urandom(16)
    
    # Hash the password with the salt using SHA-256
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    
    # Combine the salt and the hash to store them together
    salt_and_hash = salt + hash_obj
    
    # Convert the salt and hash to a hexadecimal string for storage
    hashed_password = salt_and_hash.hex()
    
    # Update the database with the username and hashed password
    updateUserLogin(userName, hashed_password)

# Example usage
storePassword('exampleUser', 'examplePassword')
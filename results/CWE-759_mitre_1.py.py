To securely store a password, you should hash it using a strong cryptographic hash function. Python's `hashlib` library provides several such functions. Here's how you can implement the `storePassword` function to hash a password and update a database with the username and hashed password:

```python
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
```

### Explanation:

1. **Salt Generation**: A random salt is generated using `os.urandom(16)`. The salt is used to ensure that the same password will have different hashes, which helps protect against rainbow table attacks.

2. **Password Hashing**: The password is hashed using the `hashlib.pbkdf2_hmac` function with the SHA-256 algorithm. The `pbkdf2_hmac` function is a key derivation function that applies a hash function (SHA-256 in this case) multiple times (100,000 iterations here) to make brute-force attacks more difficult.

3. **Storing Salt and Hash**: The salt and the hash are combined and converted to a hexadecimal string for storage. This ensures that both the salt and the hash are stored together, which is necessary for verifying the password later.

4. **Database Update**: The `updateUserLogin` function is called to update the database with the username and the hashed password. In a real application, this function would
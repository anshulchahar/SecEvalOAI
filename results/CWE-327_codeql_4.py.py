To create a hash of a password combined with a salt, you can use the `hashlib` library in Python. Here's a function that demonstrates how to do this:

```python
import hashlib

def get_password_hash(password: str, salt: str) -> str:
    '''
    Return a hash of the password and salt.
    '''
    # Combine the password and salt
    combined = password + salt
    
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the bytes of the combined string
    hash_object.update(combined.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()
    
    return password_hash

# Example usage
password = "my_secure_password"
salt = "random_salt"
hashed_password = get_password_hash(password, salt)
print(hashed_password)
```

### Explanation:
- **Combining Password and Salt**: The password and salt are concatenated into a single string.
- **Hash Object**: A SHA-256 hash object is created using `hashlib.sha256()`.
- **Updating Hash**: The `update` method is used to feed the combined string (converted to bytes) into the hash object.
- **Hexadecimal Digest**: The `hexdigest` method returns the hash as a hexadecimal string, which is a common format for storing and comparing hashes.

This approach ensures that the password is hashed with an additional layer of security provided by the salt, making it more resistant to certain types of attacks, such as rainbow table attacks.
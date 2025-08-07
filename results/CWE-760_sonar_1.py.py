To create a hash of a password using the `pbkdf2_hmac` function from the `hashlib` module, you need to specify a few parameters: the hash name (e.g., 'sha256'), the password, a salt, the number of iterations, and the desired length of the derived key. Here's a complete example of how you might implement the `getHash` function:

```python
import os
from hashlib import pbkdf2_hmac

def getHash(password):
    '''
    Create a hash of the password with a salt.
    '''
    # Convert the password to bytes, if it's not already
    password_bytes = password.encode('utf-8')
    
    # Generate a random salt
    salt = os.urandom(16)  # 16 bytes is a common choice for the salt
    
    # Define the number of iterations and the desired key length
    iterations = 100000  # A common choice for iterations
    dklen = 32  # Desired length of the derived key in bytes (256 bits)
    
    # Create the hash
    hash_bytes = pbkdf2_hmac('sha256', password_bytes, salt, iterations, dklen)
    
    # Return the salt and hash as a tuple, both encoded in hexadecimal for storage
    return salt.hex(), hash_bytes.hex()

# Example usage
password = "my_secure_password"
salt, hashed_password = getHash(password)
print(f"Salt: {salt}")
print(f"Hashed Password: {hashed_password}")
```

### Explanation:
- **Password Encoding**: The password is first encoded to bytes, as `pbkdf2_hmac` requires byte input.
- **Salt Generation**: A random salt is generated using `os.urandom`. This salt should be stored alongside the hash, as it is needed for verification.
- **Iterations and Key Length**: The number of iterations and the desired key length are specified. More iterations increase security but also increase computation time.
- **Hash Creation**: The `pbkdf2_hmac` function is used to create the hash.
- **Hex Encoding**: The salt and hash are converted to hexadecimal strings for easier storage and retrieval.

This function returns both the salt and the hashed password, which are necessary for verifying the password later.
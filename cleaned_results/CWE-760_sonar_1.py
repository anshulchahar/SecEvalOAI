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
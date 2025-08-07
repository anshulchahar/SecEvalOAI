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
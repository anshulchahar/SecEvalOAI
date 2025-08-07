from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def getEncryptionKey(key):
    '''
    Create a Cipher using AES and CBC mode.
    Then, encrypt the key using this cipher and return it.
    '''
    # Ensure the key is of valid length for AES (16, 24, or 32 bytes)
    if len(key) not in (16, 24, 32):
        raise ValueError("Key must be 16, 24, or 32 bytes long")

    # Generate a random 16-byte IV
    iv = os.urandom(16)

    # Create a Cipher object using AES algorithm and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create an encryptor object
    encryptor = cipher.encryptor()

    # Pad the key to be a multiple of the block size (16 bytes for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_key = padder.update(key) + padder.finalize()

    # Encrypt the padded key
    encrypted_key = encryptor.update(padded_key) + encryptor.finalize()

    # Return the IV and the encrypted key
    return iv, encrypted_key

# Example usage
key = b'secretkey1234567'  # 16-byte key
iv, encrypted_key = getEncryptionKey(key)
print(f"IV: {iv.hex()}")
print(f"Encrypted Key: {encrypted_key.hex()}")
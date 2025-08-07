from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def getEncryptionKey(data, key):
    """
    Encrypts the given data using AES encryption in CBC mode.

    Parameters:
    - data (bytes): The data to encrypt.
    - key (bytes): The encryption key (must be 16, 24, or 32 bytes long).

    Returns:
    - bytes: The encrypted data.
    """
    # Ensure the key length is valid for AES (16, 24, or 32 bytes)
    if len(key) not in (16, 24, 32):
        raise ValueError("Key must be 16, 24, or 32 bytes long")

    # Generate a random IV
    iv = get_random_bytes(AES.block_size)

    # Create a cipher object using the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the data to be a multiple of the block size
    padded_data = pad(data, AES.block_size)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    # Return the IV concatenated with the encrypted data
    return iv + encrypted_data
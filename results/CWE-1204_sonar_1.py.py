To encrypt data using AES in CBC mode, you need an encryption key and an initialization vector (IV). The IV should be random and unique for each encryption operation to ensure security. Here's how you can implement the `getEncryptionKey` function to encrypt data using AES in CBC mode:

```python
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
```

### Explanation:
1. **Key Length**: AES requires keys of specific lengths: 16, 24, or 32 bytes. The function checks if the provided key meets this requirement.

2. **Initialization Vector (IV)**: A random IV is generated for each encryption operation. This ensures that even if the same data is encrypted multiple times with the same key, the ciphertext will be different each time.

3. **Padding**: The data is padded to ensure its length is a multiple of the AES block size (16 bytes). This is necessary for CBC mode, which operates on complete blocks of data.

4. **Encryption**: The data is encrypted using the AES cipher in CBC mode.

5. **Output**: The function returns the IV concatenated with the encrypted data. The IV is needed for decryption, so it must be stored or transmitted along with the ciphertext.
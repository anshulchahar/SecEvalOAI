To generate a random 128-bit cryptographic key using `os.urandom()`, you can follow these steps. This function will return a key that is 16 bytes long, which is equivalent to 128 bits:

```python
def generateCryptoKey():
    '''
    Generate a random 128-bit key using os.urandom().
    '''
    # Generate 16 random bytes (128 bits)
    key = os.urandom(16)
    return key

# Example usage
crypto_key = generateCryptoKey()
print("Generated Crypto Key:", crypto_key.hex())
```

### Explanation:
- **`os.urandom(n)`**: This function generates `n` random bytes suitable for cryptographic use. In this case, `n` is 16 because 16 bytes equals 128 bits (1 byte = 8 bits).
- **`key.hex()`**: This converts the binary data into a hexadecimal string for easier readability. You can remove `.hex()` if you prefer to work with the raw bytes.

This method ensures that the generated key is cryptographically secure, as `os.urandom()` is designed to provide high-quality randomness suitable for cryptographic applications.
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
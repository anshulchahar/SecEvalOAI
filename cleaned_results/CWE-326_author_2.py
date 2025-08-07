from Crypto.PublicKey import DSA

def generate_private_key():
    # Generate a DSA key
    key = DSA.generate(1024)  # 1024 is a common key size for DSA

    # Export the key in OpenSSH format
    # Note: PyCryptodome does not directly support exporting DSA keys in OpenSSH format.
    # We will export it in PEM format instead, which is a common format for DSA keys.
    private_key_pem = key.export_key(format='PEM')

    return private_key_pem

# Example usage
private_key = generate_private_key()
print(private_key.decode())
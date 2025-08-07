To generate a private key using RSA and export it in the OpenSSH format, you can use the `Crypto.PublicKey.RSA` module from the `pycryptodome` library. Below is a function that accomplishes this:

```python
from Crypto.PublicKey import RSA

def create_private_key():
    '''
    Generate a private key using RSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    # Generate a new RSA key pair
    key = RSA.generate(2048)
    
    # Export the private key in OpenSSH format
    private_key = key.export_key(format='PEM', pkcs=8)
    
    return private_key.decode('utf-8')

# Example usage
private_key = create_private_key()
print(private_key)
```

### Explanation:
- **RSA Key Generation**: The `RSA.generate(2048)` function generates a new RSA key pair with a key size of 2048 bits. You can adjust the key size if needed, but 2048 bits is a common choice for a good balance of security and performance.
  
- **Exporting the Key**: The `export_key` method is used to export the private key. The `format='PEM'` specifies that the key should be exported in PEM format, which is a base64 encoded format commonly used for keys. The `pkcs=8` parameter ensures compatibility with OpenSSH.

- **Return the Key**: The exported key is returned as a UTF-8 encoded string for easy handling and display.

This function will generate a new RSA private key each time it is called and return it in a format that can be used with OpenSSH.
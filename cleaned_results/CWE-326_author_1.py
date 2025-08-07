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
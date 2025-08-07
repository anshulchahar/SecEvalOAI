import hashlib

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    
    Parameters:
    - certificate: The certificate data as a string or bytes.
    - known_hash: The known hash as a hexadecimal string.
    
    Returns:
    - bool: True if the certificate's hash matches the known_hash, False otherwise.
    '''
    # Ensure the certificate is in bytes
    if isinstance(certificate, str):
        certificate = certificate.encode('utf-8')
    
    # Compute the hash of the certificate
    certificate_hash = hashlib.sha256(certificate).hexdigest()
    
    # Compare the computed hash with the known hash
    return certificate_hash == known_hash

# Example usage:
# certificate_data = "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"
# known_hash = "abc123..."
# print(certificate_matches(certificate_data, known_hash))
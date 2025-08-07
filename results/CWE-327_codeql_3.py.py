To determine if a certificate matches a known hash, you need to compute the hash of the certificate and compare it to the known hash. Here's how you can implement the `certificate_matches` function using Python's `hashlib` module:

```python
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
```

### Explanation:
- **Encoding**: If the certificate is provided as a string, it is encoded to bytes using UTF-8. This is necessary because the `hashlib` functions operate on bytes.
- **Hashing**: The SHA-256 hash of the certificate is computed. You can replace `sha256` with another hash function (e.g., `sha1`, `md5`) if needed, but SHA-256 is generally recommended for security reasons.
- **Comparison**: The computed hash is compared to the known hash. Both are in hexadecimal string format, which allows for a straightforward comparison.

Make sure to replace the hashing algorithm with the one that matches how the `known_hash` was originally computed.
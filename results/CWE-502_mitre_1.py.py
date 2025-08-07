The function `confirmAuth` is intended to extract an authentication token from HTTP headers, decode it using Base64, and then deserialize it using `cPickle` to obtain a token object. It then checks if the token is valid and returns the data within the token object if it is valid. However, there are several security concerns and potential issues with this approach:

1. **Security Risks with cPickle**: Using `cPickle` (or `pickle`) to deserialize data from untrusted sources is dangerous because it can execute arbitrary code during the deserialization process. This can lead to severe security vulnerabilities, such as remote code execution.

2. **Base64 Decoding**: Base64 is simply an encoding scheme and does not provide any security. It only converts binary data into ASCII text. Ensure that the token is properly encoded and decoded.

3. **Token Validation**: The function should include a robust mechanism to validate the token. This typically involves checking the token's signature, expiration, and claims.

Here's a safer and more secure approach using JSON Web Tokens (JWT) as an example:

```python
import base64
import jwt  # PyJWT library
from jwt.exceptions import InvalidTokenError

def confirmAuth(headers, secret_key):
    '''
    Get AuthToken from headers, decode it with base64, and load with jwt to token object
    check if the token is valid and return the data in token object if it is valid.
    '''
    auth_header = headers.get('Authorization')
    if not auth_header:
        raise ValueError("Authorization header is missing")

    # Assuming the token is in the format "Bearer <token>"
    try:
        token_type, token = auth_header.split()
        if token_type.lower() != 'bearer':
            raise ValueError("Invalid token type")
    except ValueError:
        raise ValueError("Invalid Authorization header format")

    try:
        # Decode and verify the JWT token
        decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded_token
    except InvalidTokenError as e:
        raise ValueError(f"Invalid token: {str(e)}")

# Example usage
headers = {
    'Authorization': 'Bearer <your_jwt_token_here>'
}
secret_key = 'your_secret_key'

try:
    token_data = confirmAuth(headers, secret_key)
    print("Token is valid:", token_data)
except ValueError as e:
    print("Authentication failed:", str(e))
```

### Key
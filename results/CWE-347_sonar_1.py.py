To verify and decode a JSON Web Token (JWT), you can use the `jwt` library in Python. Below is an example of how you might implement the `verifyJsonWebToken` function using the `pyjwt` library, which is a commonly used library for handling JWTs in Python. This example assumes you have a secret key that was used to sign the token, which is necessary for verifying its authenticity.

First, ensure you have the `pyjwt` library installed. You can install it using pip if you haven't already:

```bash
pip install pyjwt
```

Here's how you can implement the `verifyJsonWebToken` function:

```python
import jwt

def verifyJsonWebToken(token, secret_key, algorithms=['HS256']):
    '''
    Decode the JSON web token passed and return it.
    
    Parameters:
    - token: The JWT to decode.
    - secret_key: The secret key used to sign the JWT.
    - algorithms: A list of algorithms to use for decoding. Default is ['HS256'].
    
    Returns:
    - The decoded payload of the JWT if verification is successful.
    
    Raises:
    - jwt.ExpiredSignatureError: If the token has expired.
    - jwt.InvalidTokenError: If the token is invalid for any reason.
    '''
    try:
        # Decode the token using the secret key and specified algorithms
        decoded_payload = jwt.decode(token, secret_key, algorithms=algorithms)
        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
        raise
    except jwt.InvalidTokenError:
        print("Invalid token.")
        raise

# Example usage:
# secret_key = 'your-secret-key'
# token = 'your.jwt.token'
# try:
#     decoded = verifyJsonWebToken(token, secret_key)
#     print("Decoded JWT:", decoded)
# except Exception as e:
#     print("Error decoding JWT:", e)
```

### Key Points:
- **Secret Key**: The secret key must be the same as the one used to sign the JWT. Without it, you cannot verify the token's authenticity.
- **Algorithms**: You need to specify the algorithm(s) used for signing the token. The default in this example is `HS256`, but you should use the algorithm that matches your token's signing method.
- **Error Handling**: The function includes error handling for expired tokens and other invalid token errors. Adjust the error handling as needed for your application.

This
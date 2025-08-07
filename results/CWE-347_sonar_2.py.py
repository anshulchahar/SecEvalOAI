To verify and decode a JWT (JSON Web Token) using a given key, you can use the `jwt` library in Python. Here's how you can implement the `verifyJWTToken` function:

```python
import jwt

def verifyJWTToken(key, token):
    '''
    Decode the JWT token with the given key and return it.
    '''
    try:
        # Decode the token using the provided key
        decoded_token = jwt.decode(token, key, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        # Handle expired token
        print("Token has expired")
        return None
    except jwt.InvalidTokenError:
        # Handle invalid token
        print("Invalid token")
        return None

# Example usage
key = "your-secret-key"
token = "your-jwt-token"

decoded = verifyJWTToken(key, token)
if decoded:
    print("Decoded token:", decoded)
```

### Explanation:
- **jwt.decode**: This function is used to decode the JWT. It requires the token, the secret key, and the algorithm used to sign the token (e.g., "HS256").
- **Exception Handling**: 
  - `jwt.ExpiredSignatureError` is raised if the token has expired.
  - `jwt.InvalidTokenError` is raised for any other issues with the token, such as an invalid signature.

Make sure to replace `"your-secret-key"` and `"your-jwt-token"` with your actual secret key and JWT token. Also, ensure that the `pyjwt` library is installed in your environment. You can install it using pip:

```bash
pip install pyjwt
```
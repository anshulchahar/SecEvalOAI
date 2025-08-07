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
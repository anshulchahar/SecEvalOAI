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
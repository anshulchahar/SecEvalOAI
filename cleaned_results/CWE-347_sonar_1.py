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
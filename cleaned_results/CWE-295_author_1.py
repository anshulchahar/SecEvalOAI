import ssl

def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    # Create a default SSL context
    context = ssl.create_default_context()

    # Optionally, you can customize the context here
    # For example, you can set the context to verify the server's certificate
    context.verify_mode = ssl.CERT_REQUIRED

    # Load default CA certificates
    context.load_default_certs()

    return context

# Example usage
ssl_context = getSSLContext()
print(ssl_context)
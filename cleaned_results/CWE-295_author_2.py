from OpenSSL import SSL

def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    # Create an SSL context with the desired method
    # SSLv23_METHOD is deprecated, use TLS_METHOD for a more secure default
    context = SSL.Context(SSL.TLS_METHOD)

    # Set the context to require a certificate from the client
    context.set_verify(SSL.VERIFY_PEER, callback=None)

    # Load server certificate and private key
    # Replace 'server.crt' and 'server.key' with your actual certificate and key files
    context.use_certificate_file('server.crt')
    context.use_privatekey_file('server.key')

    # Optionally, load the CA certificates to verify the client certificates
    # Replace 'ca.crt' with your actual CA certificate file
    context.load_verify_locations('ca.crt')

    # Set other context options as needed
    context.set_options(SSL.OP_NO_SSLv2 | SSL.OP_NO_SSLv3 | SSL.OP_NO_COMPRESSION)

    return context
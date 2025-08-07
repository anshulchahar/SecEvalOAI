def connect(host, port):
    # Create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap the socket with SSL
    ssl_sock = ssl.wrap_socket(sock)
    
    # Connect to the specified host and port
    ssl_sock.connect((host, port))
    
    # Return the SSL socket
    return ssl_sock
To create a client SSL socket using IPv4 and the TCP protocol, and connect it to a specified host and port, you can use Python's `socket` and `ssl` modules. Here's a function that accomplishes this:

```python
def connect(host, port):
    # Create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap the socket with SSL
    ssl_sock = ssl.wrap_socket(sock)
    
    # Connect to the specified host and port
    ssl_sock.connect((host, port))
    
    # Return the SSL socket
    return ssl_sock
```

### Explanation:

1. **Socket Creation**: 
   - `socket.AF_INET` specifies the use of IPv4.
   - `socket.SOCK_STREAM` specifies the use of the TCP protocol.

2. **SSL Wrapping**:
   - `ssl.wrap_socket(sock)` wraps the socket with SSL, enabling secure communication.

3. **Connecting**:
   - `ssl_sock.connect((host, port))` connects the SSL-wrapped socket to the specified host and port.

4. **Return**:
   - The function returns the SSL socket, which can be used for secure communication with the server.

### Note:
- This example uses `ssl.wrap_socket`, which is a simple way to wrap a socket with SSL. However, for more control and better security practices, you might want to use `ssl.create_default_context` to create an SSL context and then use `context.wrap_socket` to wrap the socket. This approach allows you to specify more SSL options, such as verifying the server's certificate.

Here's an example using `ssl.create_default_context`:

```python
def connect(host, port):
    # Create a socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Create a default SSL context
    context = ssl.create_default_context()
    
    # Wrap the socket with the SSL context
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    
    # Connect to the specified host and port
    ssl_sock.connect((host, port))
    
    # Return the SSL socket
    return ssl_sock
```

This approach is generally recommended for better security and flexibility.
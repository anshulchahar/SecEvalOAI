To create a simple echo server using Python's `socket` module, you can follow the example below. This server will listen on a specified port, accept incoming connections, and echo back any messages it receives from clients.

```python
import socket

def echoServer(port):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('', port)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on port {port}...")

    try:
        while True:
            # Wait for a connection
            print("Waiting for a connection...")
            connection, client_address = server_socket.accept()

            try:
                print(f"Connection from {client_address}")

                # Receive the data in small chunks and echo it back
                while True:
                    data = connection.recv(1024)
                    if data:
                        print(f"Received: {data.decode()}")
                        print("Echoing data back to the client...")
                        connection.sendall(data)
                    else:
                        print("No more data from client, closing connection.")
                        break

            finally:
                # Clean up the connection
                connection.close()

    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    finally:
        server_socket.close()

# Example usage
if __name__ == "__main__":
    echoServer(65432)
```

### Explanation:
- **Socket Creation**: A TCP/IP socket is created using `socket.AF_INET` and `socket.SOCK_STREAM`.
- **Binding**: The socket is bound to an address and port. Here, `''` is used to bind to all available interfaces.
- **Listening**: The server listens for incoming connections with `listen(1)`, where `1` is the number of unaccepted connections that the system will allow before refusing new connections.
- **Accepting Connections**: The server waits for a connection using `accept()`, which returns a new socket object representing the connection and the address of the client.
- **Receiving and Sending Data**: The server receives data in chunks of 1024 bytes and sends it back to the client.
- **Graceful Shutdown**: The server can be stopped with a keyboard interrupt (Ctrl+C), which will close the server socket.

This code provides a basic echo server that can be expanded with additional features such as handling multiple clients simultaneously
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
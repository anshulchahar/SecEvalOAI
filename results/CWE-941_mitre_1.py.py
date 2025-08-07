To implement the `sendData` function as described, you'll need to create a UDP socket that listens for incoming packets, parses each packet, and then sends a response to a specified IP address. Below is a basic implementation of this functionality in Python:

```python
import socket

def parseUDPpacket(data):
    '''
    This function is a placeholder for parsing the UDP packet.
    It should be implemented to extract necessary information from the packet.
    For this example, let's assume it returns a tuple (response_data, target_ip, target_port).
    '''
    # Example parsing logic (to be replaced with actual parsing logic)
    response_data = data.upper()  # Just an example transformation
    target_ip = '127.0.0.1'  # Example target IP
    target_port = 12345  # Example target port
    return response_data, target_ip, target_port

def sendResponse(response_data, target_ip, target_port):
    '''
    This function sends the response data to the specified IP address and port.
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(response_data, (target_ip, target_port))

def sendData():
    '''
    This function creates a UDP socket and continuously receives 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to the appropriate requested IP address by invoking sendResponse.
    '''
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Bind the socket to a specific address and port
        server_address = ('', 10000)  # Listen on all interfaces on port 10000
        sock.bind(server_address)

        print("Listening for incoming UDP packets...")

        while True:
            # Receive data from the socket
            data, address = sock.recvfrom(1024)
            print(f"Received {len(data)} bytes from {address}")

            # Parse the received UDP packet
            response_data, target_ip, target_port = parseUDPpacket(data)

            # Send the response to the appropriate IP address and port
            sendResponse(response_data, target_ip, target_port)
            print(f"Sent response to {target_ip}:{target_port}")

# Example usage
if __name__ == "__main__":
    sendData()
```

### Key Points:
- **Socket Creation**: A UDP socket is created using `socket.socket
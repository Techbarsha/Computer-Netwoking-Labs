# Server code
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening on port 8080...")

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    
    try:
        print("Connection accepted from:", client_address)
        # Send a response back to the client
        client_socket.sendall(b"Connection accepted")
    finally:
        # Clean up the connection
        client_socket.close()

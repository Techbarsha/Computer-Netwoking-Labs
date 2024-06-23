# Client code
import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 8080)
client_socket.connect(server_address)

try:
    # Receive data from the server
    data = client_socket.recv(1024)
    print("Server response:", data.decode())
finally:
    # Clean up the connection
    client_socket.close()

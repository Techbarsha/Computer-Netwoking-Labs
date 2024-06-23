import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print('UDP server is listening...')

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)
    
    # Print the received data and client address
    print(f"Received '{data.decode()}' from {client_address}")
    
    # Send a response back to the client
    response = f"Hello, client! You said '{data.decode()}'"
    server_socket.sendto(response.encode(), client_address)

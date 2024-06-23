import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 12345)

while True:
    # Get user input
    message = input("Enter message to send (type 'exit' to quit): ")
    
    if message.lower() == 'exit':
        break
    
    # Send data to the server
    client_socket.sendto(message.encode(), server_address)
    
    # Receive response from the server
    response, server = client_socket.recvfrom(1024)
    print(f"Received from server: {response.decode()}")

# Close the socket
client_socket.close()

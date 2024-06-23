import socket

def tcp_server():
    server_address = 'localhost'
    server_port = 4567  # Changed port number to avoid conflicts
    
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind((server_address, server_port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {server_address}:{server_port}")
    
    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Connection from {client_address}")
            
            # Receive the data in small chunks and send it back
            while True:
                data = connection.recv(1024)
                if data:
                    print(f"Received: {data.decode()}")
                    connection.sendall(data)  # Echo back the data
                else:
                    print("No more data from", client_address)
                    break
                
        finally:
            # Clean up the connection
            connection.close()

if __name__ == '__main__':
    tcp_server()

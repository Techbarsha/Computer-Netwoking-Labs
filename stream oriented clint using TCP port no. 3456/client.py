import socket

def tcp_client():
    # Define server address and port
    server_address = 'localhost'
    server_port = 4567  # Changed port number to match server
    
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))
        print(f"Connected to {server_address} on port {server_port}")
        
        # Send data
        message = 'Hello, Server!'
        client_socket.sendall(message.encode())
        print(f"Sent: {message}")
        
        # Receive response
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed")

if __name__ == '__main__':
    tcp_client()

import socket

def start_server(host='127.0.0.1', port=3456):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = (host, port)
    server_socket.bind(server_address)
    print(f'Starting server on {host}:{port}')

    # Listen for incoming connections
    server_socket.listen(5)  # The argument specifies the number of unaccepted connections that the system will allow before refusing new connections
    print('Waiting for a connection...')

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f'Connection from {client_address}')

        try:
            # Receive the data in small chunks and retransmit it
            while True:
                data = client_socket.recv(1024)
                if data:
                    print(f'Received: {data.decode()}')
                    client_socket.sendall(data)  # Echo back the received data
                else:
                    print(f'No more data from {client_address}')
                    break
        finally:
            # Clean up the connection
            client_socket.close()
            print(f'Connection with {client_address} closed')

if __name__ == "__main__":
    start_server()

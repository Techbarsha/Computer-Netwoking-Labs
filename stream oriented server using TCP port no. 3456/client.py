import socket

def start_client(host='127.0.0.1', port=3456):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = (host, port)
    print(f'Connecting to {host}:{port}')
    client_socket.connect(server_address)

    try:
        # Send data
        message = 'This is the message. It will be echoed back.'
        print(f'Sending: {message}')
        client_socket.sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = client_socket.recv(1024)
            amount_received += len(data)
            print(f'Received: {data.decode()}')

    finally:
        # Clean up the connection
        print('Closing connection')
        client_socket.close()

if __name__ == "__main__":
    start_client()

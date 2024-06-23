import socket
import threading

def handle_client(client_socket):
    with client_socket:
        print(f"Connected by {client_socket.getpeername()}")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from {client_socket.getpeername()}: {data.decode('utf-8')}")
            client_socket.sendall(data)
        print(f"Connection with {client_socket.getpeername()} closed")

def start_server(host, port, client_connected_cb):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_connected_cb(client_socket, addr)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    def client_connected_cb(client_socket, addr):
        print(f"Client connected callback: {addr}")

    start_server('0.0.0.0', 9999, client_connected_cb)

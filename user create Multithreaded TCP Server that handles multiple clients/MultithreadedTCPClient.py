import socket

def client(host='127.0.0.1', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(b'Hello, server!')
        response = sock.recv(1024)
        print(f"Received: {response.decode('utf-8')}")

if __name__ == "__main__":
    client()

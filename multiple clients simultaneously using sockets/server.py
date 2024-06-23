import selectors
import socket

HOST = '127.0.0.1'
PORT = 12345

def accept_connection(sock, mask):
    conn, addr = sock.accept()
    print(f'Accepted connection from {addr}')
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read_client_data)

def read_client_data(conn, mask):
    try:
        data = conn.recv(1024)
        if data:
            print(f'Received from {conn.getpeername()}: {data.decode()}')
            # Echo the received data back to the client
            conn.send(data)
        else:
            print(f'Closing connection to {conn.getpeername()}')
            sel.unregister(conn)
            conn.close()
    except ConnectionResetError as e:
        print(f'Connection reset by {conn.getpeername()}: {e}')
        sel.unregister(conn)
        conn.close()
    except Exception as e:
        print(f'Error: {e}')
        sel.unregister(conn)
        conn.close()

sel = selectors.DefaultSelector()

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind((HOST, PORT))
server_sock.listen()
print(f'Server listening on {HOST}:{PORT}')

server_sock.setblocking(False)
sel.register(server_sock, selectors.EVENT_READ, accept_connection)

try:
    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)
except KeyboardInterrupt:
    print('Server shutting down...')
finally:
    sel.close()
    server_sock.close()

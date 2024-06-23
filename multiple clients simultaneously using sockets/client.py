import socket
import time

HOST = '127.0.0.1'
PORT = 12345

try:
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to server at {HOST}:{PORT}")
    client_sock.connect((HOST, PORT))
    print("Connected to server")
    time.sleep(1)  # Wait for 1 second before sending data

    while True:
        message = input("Enter a message to send (or 'quit' to exit): ")
        if message.lower() == 'quit':
            break
        
        client_sock.send(message.encode())
        print(f"Sent: {message}")
        try:
            data = client_sock.recv(1024)
            if not data:
                print("Server closed the connection.")
                break
            print(f"Received from server: {data.decode()}")
        except ConnectionResetError as e:
            print(f"Server forcibly closed the connection: {e}")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

except ConnectionRefusedError as e:
    print(f"Connection refused. Make sure the server is running: {e}")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client_sock.close()
    print("Connection closed")

import socket
from datetime import datetime

# Target host (can be an IP address or domain name)
target = 'ip_address'
# Define the range of ports to scan
port_range = range(1, 6025)

# Print the target being scanned
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")

# Function to check if a port is open
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: Open")
    s.close()

# Scan the specified range of ports
for port in port_range:
    scan_port(port)

print(f"Time finished: {datetime.now()}")

import socket
import threading
import time


def handle_connection(conn_addr):
    return

# Define port and host for server
host = '127.0.0.1'
port = 5000

# Create a new socket
# AF_INET is the address field for IPv4
# SOCK_STREAM is to input a strema of data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to bind the socket to the port and host
try:
    server.bind((host,port))
except socket.error as e:
    print(str(e))

# Specify that the socket server will accept exactly two connections
server.listen(2)

# Create a new thread to handle each new connection
while True:
    threading.Thread(target=handle_connection, args=(server.accept(),)).start()

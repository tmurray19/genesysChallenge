import socket 

# Define port and host for server
host = '127.0.0.1'
port = 5000

# Create a new socket
# AF_INET is the address field for IPv4
# SOCK_STREAM is to input a strema of data
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def client():
    client_socket.connect((host,port))
    while True:
        client_in = input(client_socket.recv(1024).decode())
        
        client_socket.send(client_in.encode())


if __name__ == '__main__': 
    client() 
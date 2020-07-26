import socket 
import time

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
        server_msg = client_socket.recv(1024).decode()
        if ('wait' in server_msg):
            print(server_msg)
        if ('Congratulations' in server_msg):
            print(server_msg)
            print("Game over, closing connection")
            client_socket.close()
            break
        else:
            client_socket.send(input(server_msg).encode())


if __name__ == '__main__': 
    client() 
import socket 
import time

# Create a new socket
# AF_INET is the address field for IPv4
# SOCK_STREAM is to input a strema of data
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def client(host = '127.0.0.1', port = 5000):
    # Connect client to server
    client_socket.connect((host,port))
    
    while True:
        # Get message from server
        server_msg = client_socket.recv(1024).decode()
        # Print the message if the server asks for a wait
        if ('wait' in server_msg):
            print(server_msg)
        # Close the connection if the game is won or an abrupt message is sent in
        elif (('Congratulations' in server_msg) or ('abruptly' in server_msg)):
            print(server_msg)
            print("Game over, closing connection")
            client_socket.close()
            break
        # Otherwise, ask user for input
        else:
            user_in = ""
            # Stops user from inputting empty strings
            while (len(user_in) < 1):
                user_in = input(server_msg)
            client_socket.send(user_in.encode())


if __name__ == '__main__': 
    client() 



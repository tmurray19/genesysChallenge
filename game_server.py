## Multithreaded socket server to read inputs from clients for connect five game
import socket
from threading import Thread
import connect_five_logic
import time

# Define port and host for server
host = '127.0.0.1'
port = 5000

# For assigning colours to players
red_taken = False

# Client count
count = 0


# Create a new socket
# AF_INET is the address field for IPv4
# SOCK_STREAM is to input a strema of data
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to bind the socket to the port and host
try:
    server_socket.bind((host,port))
except socket.error as e:
    print(str(e))

# Client class holds the connection details for both players, as well as their names
class Client(Thread):
    # Each client has a socket and an address associated with it
    # They also have a name, and a colour for the purpose of the game
    def __init__(self, socket, address, colour):
        Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.player_name = None
        self.player_colour = colour
        # Start the thread
        self.start()

    def run(self):
        global count
        try:
            while True:
                server_msg = b''
                # Set the players name
                if self.player_name == None:
                    self.socket.send(f'Hello, [USER]. Please enter your name:'.encode())
                    self.player_name = self.socket.recv(1024).decode()
                # Have the user wait until a second client connects
                while count < 2:
                    self.socket.send(f'Hi {self.player_name}. Please wait, we are looking for an opponent...'.encode())
                    time.sleep(5)
                server_msg += f'Opponent found, beginning game. Your colour is {self.player_colour}({g.chips.get(self.player_colour)}).'.encode()
                # The game continues to be played until a winner is found
                while not g.get_has_winner():
                    # This code block needs to run until the player enters a legal move
                    # A legal move is the user entering a number between 1 and 9 (corresponding to the columns of the board), and there needs to be space for a chip to be placed there
                    while g.get_current_turn() == self.player_colour:
                        server_msg += f'\n{g.print_board()}'.encode()
                        server_msg += f"\nIt's your turn {self.player_name}. You are {self.player_colour}({g.chips.get(self.player_colour)}) Pick a column to place your chip (1-9):".encode()
                        self.socket.sendall(server_msg)
                        server_msg = b''
                        try:
                            g.insert_chip(self.socket.recv(1024), self.player_colour)
                        except Exception:
                            server_msg += "Error occured".encode()
                    # This code handles abrupt disconnections from a client for the other client
                    if count < 2:
                        server_msg += "Error, opponent disconnected. Game has been abruptly ended".encode()
                        self.socket.sendall(server_msg)
                        server_msg = b''
                        break
                    # This is to ensure only the correct player can submit a move
                    else:
                        server_msg += f'\n{g.print_board()}'.encode()
                        server_msg += f"\nHi {self.player_name}. You are {self.player_colour}({g.chips.get(self.player_colour)}). Please wait, your opponent is making their move...".encode()
                        self.socket.sendall(server_msg)
                        server_msg = b''
                        time.sleep(5)
                    
                else:
                    self.socket.send(f'{g.print_board()}\n{g.get_current_turn()} has won! Congratulations.'.encode())
                    print("Game is over, closing")
                    break
            server_socket.close()
        except ConnectionResetError as e:
            print(e)
            print("Client unexpectedly disconnected, breaking connection")
            count -= 1
        except ConnectionAbortedError as e:
            print(e)
            print("Client closed unexpectedly")
            count -= 1
        except ValueError:
            print(e)
            print("Value error occured, closing connection")
            count -= 1

# Specify that the socket server will accept exactly two connections
server_socket.listen(2)

# Create a new thread to handle each new connection
print("Server started")
# Create an instance of our game
g = connect_five_logic.Game()

while True:    
    # Accept a client
    client_socket, address = server_socket.accept()
    # increment the player counter
    count+=1

    # Set the colour of the player
    if not red_taken:
        colour = 'RED'
        red_taken = True
    else:
        colour = 'YELLOW'
        red_taken = False

    # Create a new client instance
    Client(client_socket, address, colour)

    
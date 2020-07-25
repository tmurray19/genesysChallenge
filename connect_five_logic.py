# Define constants to print out board to players
EMPTY = '[ ]'
RED = '[X]'
YELLOW = '[Y]'


class Game:
    """ Game class will contain game logic;  
        - placing chips into board
        - checking board for winner
        - building and storing board memory
        - checking board for winner
        """

    def __init__(self):
        """Constructor defines amount of rows, columns, and the board as a 2d array"""
        self.columns = 9
        self.rows = 6
        # Create an empty board 
        self.board = [[EMPTY] * self.rows for _ in range(self.columns)]
    
    def insert_chip(self, column, chip):
        """Drops a specific chip into a specified column"""
        col = self.board[column]

        # If the top of the column is not empty, we can't place a chip here
        if col[0] != EMPTY:
            return "Column is full, try again"
        
        # Move through the column top to bottom until an empty slot is found
        i = -1
        while col[i] != EMPTY:
            i -= 1
        col[i] = chip

        self.check_for_winner(chip)

    def print_board(self):
        """Builds board and prints in console"""
        for row in range(self.rows):
            print(
                ' '.join(
                    str(self.board[col][row]) for col in range(self.columns)
                )
            )

    def check_for_winner(self, chip):
        """ Check all lines (Horizontal, Vertical, Positive Diagonals, Negative Diagonals) in board to find winner."""

        # Check horizontal
        # Check all columns up to 5 columns from end of board
        for col in range(self.columns - 4):
            # check all rows
            for row in range(self.rows):
                # if, for a given row, there are 5 of the same chip on subsequent columns, a player has won
                if (
                    self.board[col][row] == chip
                    and self.board[col+1][row] == chip 
                    and self.board[col+2][row] == chip 
                    and self.board[col+3][row] == chip 
                    and self.board[col+4][row] == chip 
                ): return True

        # Check vertical
        # Same as above, but we flip the columns and rows
        for col in range(self.columns):
            for row in range(self.rows - 4):
                if (
                    self.board[col][row] == chip
                    and self.board[col][row+1] == chip 
                    and self.board[col][row+2] == chip 
                    and self.board[col][row+3] == chip 
                    and self.board[col][row+4] == chip 
                ): return True

        # Check positive diagonals
        for col in range(self.columns - 4):
            for row in range(self.rows - 4):
                # Start in the bottom left, look for diagonals up and to the right
                if (
                    self.board[col][row] == chip
                    and self.board[col+1][row+1] == chip 
                    and self.board[col+2][row+2] == chip 
                    and self.board[col+3][row+3] == chip 
                    and self.board[col+4][row+4] == chip 
                ): return True

        # Check negative diagonals
        for col in range(self.columns):
            for row in range(self.rows):
                # Start in the top left, look for diagonals down and to the right
                if (
                    self.board[col][row] == chip
                    and self.board[col+1][row-1] == chip 
                    and self.board[col+2][row-2] == chip 
                    and self.board[col+3][row-3] == chip 
                    and self.board[col+4][row-4] == chip 
                ): return True

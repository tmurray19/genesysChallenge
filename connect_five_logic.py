# Define constants to print out board to players


class Game:
    """ 
    Game class will contain game logic;  
        - placing chips into board
        - checking board for winner
        - building and storing board memory
        - checking board for winner
    """

    def __init__(self):
        """Constructor defines amount of rows, columns, and the board as a 2d array"""
        self.columns = 9
        self.rows = 6 
        self.has_winner = False
        self.current_turn = 'RED'
        self.chips = {
            "EMPTY" : '[ ]',
            "RED": '[X]',
            "YELLOW": '[O]'
        }
        # Create an empty board 
        self.board = [[self.chips.get("EMPTY")] * self.rows for _ in range(self.columns)]
    
    def get_has_winner(self):
        return self.has_winner

    def get_current_turn(self):
        return self.current_turn

    def insert_chip(self, column, colour):
        print(f'{self.get_current_turn()} is making a move')
        """Drops a specific chip into a specified column"""
        col = self.board[column]

        chip = self.chips.get(colour)

        # If the top of the column is not empty, we can't place a chip here
        if col[0] != self.chips.get("EMPTY"):
            print("Column is full")
            return "Column is full, try again"
        
        # Move through the column top to bottom until an empty slot is found
        i = -1
        while col[i] != self.chips.get("EMPTY"):
            i -= 1
        # Place chip in empty slot
        col[i] = chip

        # Check to see if the winner has been found
        if(self.check_for_winner(chip)):
            return f"{colour} has won!!"
        
        self.current_turn = 'RED' if colour=='YELLOW' else 'YELLOW'

    def print_board(self):
        """Builds board and prints in console"""
        board = ""
        for row in range(self.rows):
            board += (
                ' '.join(
                    str(self.board[col][row]) for col in range(self.columns)
                )
            )
            board += '\n'
        return board

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
                ): 
                    self.has_winner = True 
                    return True

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
                ): 
                    self.has_winner = True 
                    return True

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
                ): 
                    self.has_winner = True 
                    return True

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
                ): 
                    self.has_winner = True 
                    return True

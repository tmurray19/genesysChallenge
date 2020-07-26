import unittest

from connect_five_logic import Game
from connect_five_errors import BoardFullErorr, NoNumberInputError, NumberOutOfBoundsError

class TestSetUp(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_game_setup(self):
        self.assertIsNotNone(self.g)
    
    def test_board_setup(self):
        """Testing that the board is set up correctly"""
        # Check board is created
        self.assertIsNotNone(self.g.board)
        # check that there are 9 columns
        self.assertEqual(len(self.g.board), 9)
        # check that a column has 6 rows 
        self.assertEqual(len(self.g.board[0]), 6)
        # check all boards are the same
        for i in range(1,8):
            self.assertEqual(self.g.board[i], self.g.board[i-1])
    
    def test_add_to_board(self):
        # Add a chip to to the first column of a board
        self.g.insert_chip(1, "RED")
        # Check that chip went to the end of the column (i.e the botton left)
        self.assertEqual(self.g.board[0][-1], self.g.chips.get("RED"))
    
    def test_board_full(self):
        """Testing that the board cannot accept a chip in a column that is full"""
        # Add chips to a board until board is full
        self.g.insert_chip(1, "RED")
        self.g.insert_chip(1, "YELLOW")
        self.g.insert_chip(1, "RED")
        self.g.insert_chip(1, "YELLOW")
        self.g.insert_chip(1, "RED")
        self.g.insert_chip(1, "YELLOW")
        # Check that adding another chip to the first column of the board (which is full) will raise the board full error
        self.assertRaises(BoardFullErorr, self.g.insert_chip, 1, "RED")

    def test_out_of_bounds_inputs(self):
        """Testing that errors are being raised when they should be"""
        # Checking that it will only correctly accept number inputs
        self.assertRaises(NoNumberInputError, self.g.insert_chip, "column 1", "RED")
        self.assertRaises(NoNumberInputError, self.g.insert_chip, "garbage input", "RED")
        self.assertRaises(NoNumberInputError, self.g.insert_chip, "fadsaedasgfa", "RED")
        self.assertRaises(NoNumberInputError, self.g.insert_chip, "Here Please", "RED")
        
        # Check that numbers too large won't be accepted
        self.assertRaises(NumberOutOfBoundsError, self.g.insert_chip, 2000000, "RED")
        self.assertRaises(NumberOutOfBoundsError, self.g.insert_chip, -9999999, "RED")
        self.assertRaises(NumberOutOfBoundsError, self.g.insert_chip, 10, "RED")
        self.assertRaises(NumberOutOfBoundsError, self.g.insert_chip, 0, "RED")
    
    def test_turn_swaps(self):
        """Checking that turn swapping is being correctly handled"""
        self.assertEqual(self.g.get_current_turn(), "RED")
        self.g.insert_chip(1, "RED")
        self.assertEqual(self.g.get_current_turn(), "YELLOW")
        


    def tearDown(self):
        self.g=None

if __name__ == "__main__":
    unittest.main()

[
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], 
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], 
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], 
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], 
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], 
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], 
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], 
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], 
    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']
]
import unittest

from connect_five_logic import Game

class TestSetUp(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_game_setup(self):
        self.assertIsNotNone(self.g)
    
    def test_board_setup(self):
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
        self.g.insert_chip(1, "RED")
        print(self.g.print_board())
        print(self.g.board[0])
        self.assertEqual(self.g.board[5][0], self.g.chips.get("RED"))
    
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
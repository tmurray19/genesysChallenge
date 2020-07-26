# Some custom errors for invalid game states
class InvalidGameStateError(Exception):
    """Base class for other exceptions"""
    pass

class BoardFullErorr(InvalidGameStateError):
    """For when a board's column is full"""
    pass

class NoNumberInputError(InvalidGameStateError):
    """For when a player does not input a parsable number"""
    pass

class NumberOutOfBoundsError(InvalidGameStateError):
    """For when a player inputs a number outside the bounds of the board"""
    pass

class GameWonException(InvalidGameStateError):
    """For when a player has won the game"""
    pass
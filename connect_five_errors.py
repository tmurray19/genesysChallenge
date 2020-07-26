# Some custom errors for invalid game states
class Error(Exception):
    """Base class for other exceptions"""
    pass

class BoardFullErorr(Error):
    """For when a board's column is full"""
    pass



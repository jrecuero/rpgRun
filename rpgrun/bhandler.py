from board import Board


class BoardHandler(object):
    """BHander class implements some functionality for handing the Board
    instance.
    """

    def __init__(self, theBoard):
        """BoardHandler class initialization method.
        """
        assert isinstance(theBoard, Board)
        self._board = theBoard

    @property
    def Board(self):
        """
        """
        return self._board

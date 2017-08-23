from board import Board


class BoardHandler(object):

    def __init__(self, theBoard):
        assert isinstance(theBoard, Board)
        self._board = theBoard

    @property
    def Board(self):
        return self._board

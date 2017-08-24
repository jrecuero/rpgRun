from itero import Itero
from collections import deque
from brow import BRow


class Board(Itero):

    def __init__(self, theMaxLen):
        super(Board, self).__init__(BRow, theMaxLen)
        self._Itero__stream = deque()

    def scroll(self, theNewRow):
        assert isinstance(theNewRow, BRow)
        self._Itero__stream.pop()
        self._Itero__stream.appendleft(theNewRow)

    def appendleft(self, theNewRow):
        assert isinstance(theNewRow, BRow)
        self._Itero__stream.appendleft(theNewRow)

    def append(self, theValue):
        raise NotImplementedError

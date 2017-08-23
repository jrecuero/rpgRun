from itero import Itero
from collections import deque
from brow import BRow


class Board(Itero):

    def __init__(self, theMaxLen):
        super(Board, self).__init__(BRow)
        self._maxLen = theMaxLen
        self._rowIndex = 0
        self.__stream = deque()

    @property
    def MaxLen(self):
        return self._maxLen

    @property
    def RowIndex(self):
        return self._rowIndex

    @RowIndex.setter
    def RowIndex(self, theValue):
        self._rowIndex = theValue

    def fill(self):
        while self.RowIndex < self.MaxLen:
            row = yield
            self.__stream.appendleft(row)
            self.RowIndex += 1

    def scroll(self, theNewRow):
        self.__stream.pop()
        self.__stream.appendleft(theNewRow)

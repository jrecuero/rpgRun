from itero import Itero
from bcell import BCell
from enum import Enum


class BLayer(Itero):

    class LType(Enum):
        HIDDEN = 0
        UNDER = 1
        SURFACE = 2
        OBJECT = 3
        OVER = 4

    def __init__(self, theType, theMaxLen):
        assert isinstance(theType, BLayer.LType)
        super(BLayer, self).__init__(BCell)
        self._type = theType
        self._maxLen = theMaxLen
        self._cellIndex = 0
        self._cellRow = None

    @property
    def Type(self):
        return self._type

    @property
    def MaxLen(self):
        return self._maxLen

    @property
    def CellIndex(self):
        return self._cellIndex

    @CellIndex.setter
    def CellIndex(self, theValue):
        self._cellIndex = theValue

    @property
    def CellRow(self):
        return self._cellRow

    def fill(self):
        while self.CellIndex < self.MaxLen:
            cell = yield
            if cell is None:
                raise StopIteration
            if self.CellRow is None:
                self._cellRow = cell.Row
            else:
                assert self.CellRow == cell.Row
            self.__stream.append(cell)
            self.CellIndex += 1

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
        super(BLayer, self).__init__(BCell, theMaxLen)
        self._type = theType
        self._cellRow = None

    @property
    def Type(self):
        return self._type

    @property
    def CellRow(self):
        return self._cellRow

from itero import Itero
from blayer import BLayer


class BRow(Itero):

    def __init__(self, theMaxLen):
        super(BRow, self).__init__(BLayer)
        self._maxLen = theMaxLen
        for layer in BLayer.LType:
            self.__stream.append(BLayer(layer, theMaxLen))
        self._cellRow = None

    @property
    def MaxLen(self):
        return self._maxLen

    @property
    def CellRow(self):
        return self._cellRow

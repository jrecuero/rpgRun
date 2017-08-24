from itero import Itero
from blayer import BLayer


class BRow(Itero):

    def __init__(self, theMaxLen):
        super(BRow, self).__init__(BLayer, theMaxLen)
        for layer in BLayer.LType:
            self._Itero__stream.append(BLayer(layer, theMaxLen))
        self._cellRow = None

    @property
    def CellRow(self):
        return self._cellRow

    def append(self, theValue):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

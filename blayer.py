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

    def append(self, theValue):
        """
        >>> layer = BLayer(BLayer.LType.OBJECT, 5)
        >>> layer.append(BCell(0, 0, None))
        >>> layer[0]
        (0, 0) : None
        >>> layer.append(BCell(1, 0, None))
        >>> layer[1]
        (1, 0) : None
        >>> try:
        ...     layer.append(BCell(1, 1, None))
        ... except AssertionError:
        ...     print('Assert')
        Assert
        """
        assert isinstance(theValue, BCell)
        if self.CellRow is None:
            self._cellRow = theValue.Row
        else:
            assert self.CellRow == theValue.Row
        super(BLayer, self).append(theValue)

    def __repr__(self):
        """
        >>> layer = BLayer(BLayer.LType.OBJECT, 5)
        >>> layer
        [LType.OBJECT ] <None> cell# 0
        """
        return '[{0:<13}] {1:^6} cell# {2}'.format(self.Type,
                                                   '<{0}>'.format(self.CellRow),
                                                   len(self))

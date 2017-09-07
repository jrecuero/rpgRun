from itero import Itero
from bcell import BCell
from enum import Enum


class LType(Enum):
    """LType class enumeration provides all possible layer available.
    """
    HIDDEN = 0
    UNDER = 1
    SURFACE = 2
    OBJECT = 3
    OVER = 4
    MASK = 5


class BLayer(Itero):
    """BLayer class derives from Itero class and it provides specific
    functionality for a layer in the board.

    BLayer contains a number of cells, that number is provided as the
    Width or MaxLen of the layer.
    """

    def __init__(self, theType, theMaxLen):
        """BLayer class initialization method.

        >>> layer = BLayer(LType.SURFACE, 10)
        >>> layer.MaxLen
        10
        """
        assert isinstance(theType, LType)
        super(BLayer, self).__init__(BCell, theMaxLen)
        self._type = theType
        self._cellRow = None

    @property
    def Width(self):
        """
        >>> layer = BLayer(LType.SURFACE, 10)
        >>> layer.Width
        10
        """
        return self.MaxLen

    @property
    def Type(self):
        """
        >>> layer = BLayer(LType.SURFACE, 10)
        >>> layer.Type
        <LType.SURFACE: 2>
        """
        return self._type

    @property
    def CellRow(self):
        """
        >>> layer = BLayer(LType.SURFACE, 10)
        >>> layer.CellRow
        >>> layer.append(BCell(1, 2, None))
        >>> layer.CellRow
        2
        """
        return self._cellRow

    def append(self, theValue):
        """
        >>> layer = BLayer(LType.OBJECT, 5)
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
        """String representation for the BLayer instance.

        Returns:
            str : string with the BLayer instance representation.

        >>> layer = BLayer(LType.OBJECT, 5)
        >>> layer
        [LType.OBJECT ] <None> cell# 0
        """
        return '[{0:<13}] {1:^6} cell# {2}'.format(self.Type,
                                                   '<{0}>'.format(self.CellRow),
                                                   len(self))

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
    width or maxlen of the layer.
    """

    def __init__(self, type_, maxlen):
        """BLayer class initialization method.

        >>> layer = BLayer(LType.SURFACE, 10)
        >>> layer.maxlen
        10
        """
        assert isinstance(type_, LType)
        super(BLayer, self).__init__(BCell, maxlen)
        self.type = type_
        self.cellrow = None

    @property
    def width(self):
        """Gets _maxlen attribute value.

        >>> layer = BLayer(LType.SURFACE, 10)
        >>> layer.width
        10
        """
        return self.maxlen

    def append(self, theCell):
        """Appends a new cell to the layer.

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
        assert isinstance(theCell, BCell)
        if self.cellrow is None:
            self.cellrow = theCell.row
        else:
            assert self.cellrow == theCell.row
        super(BLayer, self).append(theCell)

    def get_cell_by_id(self, id):
        """Returns a cell by the given ID.

        Args:
            id (int) : Integer with the cell ID.

        Returns:
            BCell : Cell instance with the given ID. None if no cell\
                    was found.
        Example:
            >>> layer = BLayer(LType.OBJECT, 5)
            >>> c1 = BCell(0, 0, None)
            >>> c2 = BCell(1, 0, None)
            >>> layer.append(c1)
            >>> layer.append(c2)
            >>> layer.get_cell_by_id(c1.id) == c1
            True
        """
        for cell in self:
            if cell.id == id:
                return cell
        return None

    def __repr__(self):
        """String representation for the BLayer instance.

        Returns:
            str : string with the BLayer instance representation.

        >>> layer = BLayer(LType.OBJECT, 5)
        >>> layer
        [LType.OBJECT ] <None> cell# 0
        """
        return '[{0:<13}] {1:^6} cell# {2}'.format(self.type,
                                                   '<{0}>'.format(self.cellrow),
                                                   len(self))

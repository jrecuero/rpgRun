from itero import Itero
from collections import deque
from brow import BRow


class Board(Itero):

    def __init__(self, theHeight, theWidth):
        super(Board, self).__init__(BRow, theHeight)
        self._Itero__stream = deque()
        self._width = theWidth
        for i in range(self.MaxLen):
            self.appendleft(BRow(self._width))

    @property
    def Height(self):
        return self.MaxLen

    @property
    def Width(self):
        return self._width

    def scroll(self, theNewRow):
        """
        >>> board = Board(5, 5)
        >>> row1 = BRow(5)
        >>> board.appendleft(row1)
        >>> row2 = BRow(5)
        >>> board.appendleft(row2)
        >>> board[0] == row2
        True
        >>> board[1] == row1
        True
        """
        assert isinstance(theNewRow, BRow)
        self._Itero__stream.pop()
        self._Itero__stream.appendleft(theNewRow)

    def appendleft(self, theNewRow):
        """
        >>> board = Board(3, 5)
        >>> row1 = BRow(5)
        >>> row2 = BRow(5)
        >>> row3 = BRow(5)
        >>> row4 = BRow(5)
        >>> board.appendleft(row1)
        >>> board.appendleft(row2)
        >>> board.appendleft(row3)
        >>> board[0] == row3
        True
        >>> board[1] == row2
        True
        >>> board[2] == row1
        True
        >>> board.scroll(row4)
        >>> board[0] == row4
        True
        >>> board[1] == row3
        True
        >>> board[2] == row2
        True
        """
        self._Itero__stream.appendleft(theNewRow)

    def append(self, theNewRow):
        """
        >>> board = Board(5, 5)
        >>> try:
        ...     board.append(None)
        ... except NotImplementedError:
        ...     print('NotImplemented')
        NotImplemented
        """
        raise NotImplementedError

    def getRowFromCellRow(self, theCellRow):
        """
        >>> board = Board(2, 5)
        >>> board[0].CellRow = 1
        >>> board.getRowFromCellRow(1).CellRow
        1
        >>> board.getRowFromCellRow(3)
        """
        for row in self:
            if row.CellRow == theCellRow:
                return row
        return None

    def __repr__(self):
        st = ''
        for row in self:
            st += '{0}\n'.format(str(row))
        return st

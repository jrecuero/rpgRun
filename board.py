from itero import Itero
from collections import deque
from brow import BRow


class Board(Itero):
    """Board class derives from Itero class and it provides some particular
    functionality for the board.

    Board contains a number or BRow instances, that number is provided as
    the Height of the board.

    Every row contains a number of cells, that number is provided as the
    Width of the board.
    """

    def __init__(self, theHeight, theWidth):
        """Board class initialization method.

        >>> board = Board(10, 5)
        >>> board.MaxLen
        10
        """
        super(Board, self).__init__(BRow, theHeight)
        self._Itero__stream = deque()
        self._width = theWidth
        for i in range(self.MaxLen):
            self.appendleft(BRow(self._width))

    @property
    def Height(self):
        """
        >>> board = Board(10, 5)
        >>> board.Height
        10
        """
        return self.MaxLen

    @property
    def Width(self):
        """
        >>> board = Board(10, 5)
        >>> board.Width
        5
        """
        return self._width

    @property
    def TopCellRow(self):
        """
        >>> from bcell import BCell
        >>> from blayer import LType
        >>> board = Board(5, 5)
        >>> row = BRow(5)
        >>> row.addCellToLayer(BCell(0, 0, None), LType.SURFACE)
        True
        >>> board.appendleft(row)
        >>> row = BRow(5)
        >>> row.addCellToLayer(BCell(0, 1, None), LType.SURFACE)
        True
        >>> board.appendleft(row)
        >>> board.TopCellRow
        1
        """
        return self[0].CellRow

    def scroll(self, theNewRow):
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
        assert isinstance(theNewRow, BRow)
        self._Itero__stream.pop()
        self._Itero__stream.appendleft(theNewRow)

    def appendleft(self, theNewRow):
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

    def getCellsFromLayer(self, theLayers):
        """
        """
        cells  = []
        for row in self:
            cellsFromRow = row.getCellsFromLayer(theLayers)
            if cellsFromRow:
                cells.extend(cellsFromRow)
        return cells

    def addCellToLayer(self, theCell, theLayer):
        """
        >>> from bcell import BCell
        >>> from blayer import LType
        >>> board = Board(2, 5)
        >>> board[0].CellRow = 0
        >>> board.addCellToLayer(BCell(0, 0, None), LType.SURFACE)
        True
        >>> board[0][LType.SURFACE.value]
        [LType.SURFACE]  <0>   cell# 1
        """
        row = self.getRowFromCellRow(theCell.Row)
        return row.addCellToLayer(theCell, theLayer)

    def removeCell(self, theCell):
        """
        >>> from bcell import BCell
        >>> from blayer import LType
        >>> board = Board(2, 5)
        >>> board[0].CellRow = 0
        >>> cell = BCell(0, 0, None)
        >>> board.addCellToLayer(cell, LType.SURFACE)
        True
        >>> board.removeCell(cell)
        True
        >>> board[0][LType.SURFACE.value]
        [LType.SURFACE]  <0>   cell# 0
        """
        cellLayer = theCell.Layer
        row = self.getRowFromCellRow(theCell.Row)
        return row.removeCellFromLayer(theCell, cellLayer)

    def render(self, **kwargs):
        """Render the board.

        TODO: JUST RENDER ON TEXT FROM NOW.
        """
        st = ''
        for row in self:
            st += '{0} {1}\n'.format(row.CellRow, row.render(**kwargs))
        return st

    def __repr__(self):
        """String representation for Board instance.

        Returns:
            str : string with the Board instance representation.
        """
        st = ''
        for row in self:
            st += '{0}\n'.format(str(row))
        return st

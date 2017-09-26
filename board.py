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
        """Gets _maxlen attribute value.

        >>> board = Board(10, 5)
        >>> board.Height
        10
        """
        return self.MaxLen

    @property
    def Width(self):
        """Gets _width attribute value.

        >>> board = Board(10, 5)
        >>> board.Width
        5
        """
        return self._width

    @property
    def TopCellRow(self):
        """Gets the CellRow value for the top row in the board.

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
        """Scrolls the board, removing the row at the bottom (right) and
        adding a new row at the top (left).

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
        """Appends a new row to the left (top).

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
        """Appends a new row to the right. Not Allowed.

        >>> board = Board(5, 5)
        >>> try:
        ...     board.append(None)
        ... except NotImplementedError:
        ...     print('NotImplemented')
        NotImplemented
        """
        raise NotImplementedError

    def getRowFromCellRow(self, theCellRow):
        """Gets the row for the given CellRow.

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

    def getIndexFromCellRow(self, theCellRow):
        """Gets the row index for the given CellRow.

        >>> board = Board(2, 5)
        >>> board[0].CellRow = 1
        >>> board.getIndexFromCellRow(1)
        0
        >>> board.getRowFromCellRow(3)
        """
        for index, row in enumerate(self):
            if row.CellRow == theCellRow:
                return index
        return None

    def getRowFromCell(self, theCell):
        """Gets the row for the given Cell..

        >>> from bcell import BCell
        >>> board = Board(2, 5)
        >>> board[0].CellRow = 1
        >>> board.getRowFromCell(BCell(0, 1, None)).CellRow
        1
        >>> board.getRowFromCellRow(BCell(0, 3, None))
        """
        return self.getRowFromCellRow(theCell.Y)

    def getIndexFromCell(self, theCell):
        """Gets the row index for the given Cell.

        >>> from bcell import BCell
        >>> board = Board(2, 5)
        >>> board[0].CellRow = 1
        >>> board.getIndexFromCell(BCell(0, 1, None))
        0
        >>> board.getRowFromCellRow(BCell(0, 3, None))
        """
        return self.getIndexFromCellRow(theCell.Y)

    def getCellsFromLayer(self, theLayers):
        """Gets all cell for the given layer.

        """
        cells  = []
        for row in self:
            cellsFromRow = row.getCellsFromLayer(theLayers)
            if cellsFromRow:
                cells.extend(cellsFromRow)
        return cells

    def getCellById(self, theId):
        """Returns a cell by the given ID.

        Args:
            theId (int) : Integer with the cell ID.

        Returns:
            BCell : Cell instance with the given ID. None if no cell\
                    was found.

        Example:
            >>> from bcell import BCell
            >>> from blayer import LType
            >>> board = Board(5, 5)
            >>> row = BRow(5)
            >>> c1 = BCell(0, 0, None)
            >>> c2 = BCell(1, 0, None)
            >>> row.addCellToLayer(c1, LType.SURFACE)
            True
            >>> row.addCellToLayer(c2, LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> row.getCellById(c1.Id) == c1
            True
        """
        for _row in self:
            _cell = _row.getCellById(theId)
            if _cell is not None:
                return _cell
        return None

    def addCellToLayer(self, theCell, theLayer):
        """Adds a new cell to the given layer.

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
        """Removes a cell from the board.

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

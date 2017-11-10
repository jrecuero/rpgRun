from collections import deque
from rpgrun.common.itero import Itero
from rpgrun.board.brender import BRender
from rpgrun.board.brow import BRow


class Board(Itero):
    """Board class derives from Itero class and it provides some particular
    functionality for the board.

    Board contains a number or BRow instances, that number is provided as
    the Height of the board.

    Every row contains a number of cells, that number is provided as the
    Width of the board.
    """

    def __init__(self, height, width):
        """Board class initialization method.

        >>> board = Board(10, 5)
        >>> board.maxlen
        10
        """
        super(Board, self).__init__(BRow, height)
        self._Itero__stream = deque()
        self.width = width
        for i in range(self.maxlen):
            self.appendleft(BRow(self.width))

    @property
    def height(self):
        """Gets _maxlen attribute value.

        >>> board = Board(10, 5)
        >>> board.height
        10
        """
        return self.maxlen

    @property
    def top_cell_row(self):
        """Gets the cellrow value for the top row in the board.

        Returns:
            int : Integer with the top cell row.

        Example:
            >>> from rpgrun.board.bcell import BCell
            >>> from rpgrun.board.blayer import LType
            >>> board = Board(5, 5)
            >>> row = BRow(5)
            >>> row.add_cell_to_layer(BCell(0, 0, None), LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> row = BRow(5)
            >>> row.add_cell_to_layer(BCell(0, 1, None), LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> board.top_cell_row
            1
        """
        return self[0].cellrow

    @property
    def bottom_cell_row(self):
        """Gets the cellrow value for the bottom row in the board.

        Returns:
            int : Integer with the bottom cell row.

        Example:
            >>> from rpgrun.board.bcell import BCell
            >>> from rpgrun.board.blayer import LType
            >>> board = Board(3, 5)
            >>> row = BRow(5)
            >>> row.add_cell_to_layer(BCell(0, 0, None), LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> row = BRow(5)
            >>> row.add_cell_to_layer(BCell(0, 1, None), LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> row = BRow(5)
            >>> row.add_cell_to_layer(BCell(0, 2, None), LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> board.bottom_cell_row
            0
            >>> row = BRow(5)
            >>> row.add_cell_to_layer(BCell(0, 3, None), LType.SURFACE)
            True
            >>> board.scroll(row)
            >>> board.bottom_cell_row
            1
            >>> board.top_cell_row
            3
        """
        return self[self.maxlen - 1].cellrow

    def scroll(self, new_row):
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
        assert isinstance(new_row, BRow)
        self._Itero__stream.pop()
        self._Itero__stream.appendleft(new_row)

    def appendleft(self, new_row):
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
        self._Itero__stream.appendleft(new_row)

    def append(self, new_row):
        """Appends a new row to the right. Not Allowed.

        >>> board = Board(5, 5)
        >>> try:
        ...     board.append(None)
        ... except NotImplementedError:
        ...     print('NotImplemented')
        NotImplemented
        """
        raise NotImplementedError

    def get_row_from_cell_row(self, cellrow):
        """Gets the row for the given cellrow.

        >>> board = Board(2, 5)
        >>> board[0].cellrow = 1
        >>> board.get_row_from_cell_row(1).cellrow
        1
        >>> board.get_row_from_cell_row(3)
        """
        for row in self:
            if row.cellrow == cellrow:
                return row
        return None

    def get_index_from_cell_row(self, cellrow):
        """Gets the row index for the given cellrow.

        >>> board = Board(2, 5)
        >>> board[0].cellrow = 1
        >>> board.get_index_from_cell_row(1)
        0
        >>> board.get_row_from_cell_row(3)
        """
        for index, row in enumerate(self):
            if row.cellrow == cellrow:
                return index
        return None

    def get_row_from_cell(self, cell):
        """Gets the row for the given Cell..

        >>> from rpgrun.board.bcell import BCell
        >>> board = Board(2, 5)
        >>> board[0].cellrow = 1
        >>> board.get_row_from_cell(BCell(0, 1, None)).cellrow
        1
        >>> board.get_row_from_cell_row(BCell(0, 3, None))
        """
        return self.get_row_from_cell_row(cell.y)

    def get_cells_at(self, point, layers=None):
        """Gets all cells at the position for the given point.

        Args:
            point (BPoint) : point to look for the cell.
            layers (list) : list of layers to look fo cells.

        Returns:
            list : all cells at the position for the given point.

        Example:
            >>> from rpgrun.board.bcell import BCell
            >>> from rpgrun.board.blayer import LType
            >>> from rpgrun.board.bpoint import BPoint
            >>> board = Board(5, 5)
            >>> row = BRow(5)
            >>> c1 = BCell(0, 0, None)
            >>> c2 = BCell(1, 0, None)
            >>> row.add_cell_to_layer(c1, LType.SURFACE)
            True
            >>> row.add_cell_to_layer(c2, LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> row.get_cells_at(BPoint(0, 0)) == [c1, ]
            True
            >>> row.get_cells_at(BPoint(1, 0)) == [c2, ]
            True
            >>> row.get_cells_at(BPoint(0, 1)) == []
            True
        """
        row = self.get_row_from_cell_row(point.y)
        cells = row.get_cells_at(point, layers)
        return cells

    def get_index_from_cell(self, cell):
        """Gets the row index for the given Cell.

        >>> from rpgrun.board.bcell import BCell
        >>> board = Board(2, 5)
        >>> board[0].cellrow = 1
        >>> board.get_index_from_cell(BCell(0, 1, None))
        0
        >>> board.get_row_from_cell_row(BCell(0, 3, None))
        """
        return self.get_index_from_cell_row(cell.y)

    def get_cells_from_layer(self, layers=None):
        """Gets all cell for the given layer.

        Args:
            layers (list) : list of layers to look fo cells.

        Returns:
            list : all cells for the given layers.

        Example:
            >>> from rpgrun.board.bcell import BCell
            >>> from rpgrun.board.blayer import LType
            >>> board = Board(5, 5)
            >>> row = BRow(5)
            >>> c1 = BCell(0, 0, None)
            >>> c2 = BCell(1, 0, None)
            >>> row.add_cell_to_layer(c1, LType.SURFACE)
            True
            >>> row.add_cell_to_layer(c2, LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> row.get_cells_from_layer([LType.SURFACE, ]) == [c1, c2]
            True
            >>> row.get_cells_from_layer([LType.OBJECT, ]) == []
            True
        """
        cells = []
        for row in self:
            cellsFromRow = row.get_cells_from_layer(layers)
            if cellsFromRow:
                cells.extend(cellsFromRow)
        return cells

    def get_cell_by_id(self, id):
        """Returns a cell by the given ID.

        Args:
            id (int) : Integer with the cell ID.

        Returns:
            BCell : Cell instance with the given ID. None if no cell\
                    was found.

        Example:
            >>> from rpgrun.board.bcell import BCell
            >>> from rpgrun.board.blayer import LType
            >>> board = Board(5, 5)
            >>> row = BRow(5)
            >>> c1 = BCell(0, 0, None)
            >>> c2 = BCell(1, 0, None)
            >>> row.add_cell_to_layer(c1, LType.SURFACE)
            True
            >>> row.add_cell_to_layer(c2, LType.SURFACE)
            True
            >>> board.appendleft(row)
            >>> row.get_cell_by_id(c1.id) == c1
            True
        """
        for _row in self:
            _cell = _row.get_cell_by_id(id)
            if _cell is not None:
                return _cell
        return None

    def add_cell_to_layer(self, cell, layer):
        """Adds a new cell to the given layer.

        >>> from rpgrun.board.bcell import BCell
        >>> from rpgrun.board.blayer import LType
        >>> board = Board(2, 5)
        >>> board[0].cellrow = 0
        >>> board.add_cell_to_layer(BCell(0, 0, None), LType.SURFACE)
        True
        >>> board[0][LType.SURFACE.value]
        [LType.SURFACE]  <0>   cell# 1
        """
        row = self.get_row_from_cell_row(cell.row)
        return row.add_cell_to_layer(cell, layer)

    def remove_cell(self, cell):
        """Removes a cell from the board.

        >>> from rpgrun.board.bcell import BCell
        >>> from rpgrun.board.blayer import LType
        >>> board = Board(2, 5)
        >>> board[0].cellrow = 0
        >>> cell = BCell(0, 0, None)
        >>> board.add_cell_to_layer(cell, LType.SURFACE)
        True
        >>> board.remove_cell(cell)
        True
        >>> board[0][LType.SURFACE.value]
        [LType.SURFACE]  <0>   cell# 0
        """
        cell_layer = cell.Layer
        row = self.get_row_from_cell_row(cell.row)
        return row.remove_cell_from_layer(cell, cell_layer)

    def render(self, **kwargs):
        """Render the board.

        When rendering in text format, it returns a string where every cell is
        just a set of characters.

        When rendering in graph format, we have to pass the row position with
        x and y values, so sprites are properly located, and it has to return
        a list of sprites, which should be included in a sprite group from the
        graphical framework.

        Keyword Args:
            render (BRender) : Render type (graphical or text).

        Returns:
            object : Instance to be rendered.
        """
        render = kwargs.get('render', BRender.DEFAULT)
        if render is BRender.TEXT:
            st = ''
            for row in self:
                st += '{0} {1}\n'.format(row.cellrow, row.render(**kwargs))
            return st
        elif render is BRender.GRAPH:
            return [x.render(**kwargs) for x in self]
        else:
            raise NotImplementedError

    def __repr__(self):
        """String representation for Board instance.

        Returns:
            str : string with the Board instance representation.
        """
        st = ''
        for row in self:
            st += '{0}\n'.format(str(row))
        return st

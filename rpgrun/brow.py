from itero import Itero
from blayer import BLayer, LType
from brender import BRender
from bcell import BCell
from collections import OrderedDict


class BRow(Itero):
    """BRow class derives from Itero class and it provides some
    particular functinality for a row in the board.

    BRow contains a fixed number of BLayer instances (one per
    LType).

    Every layer in the row  contains a number of cells, provided
    as the maxlen if the Row.
    """

    def __init__(self, maxlen):
        """BRow class initialization method.

        >>> row = BRow(5)
        >>> row.maxlen
        5
        """
        super(BRow, self).__init__(BLayer, maxlen)
        for layer in LType:
            self._Itero__stream.append(BLayer(layer, maxlen))
        self._cellrow = None

    @property
    def Width(self):
        """Gets _maxlen attribute value.

        >>> row = BRow(10)
        >>> row.Width
        10
        """
        return self.maxlen

    @property
    def cellrow(self):
        """Gets _cellrow attribute value using the underlying layer.

        >>> row = BRow(2)
        >>> row.cellrow
        >>> row[0].append(BCell(0, 1, None))
        >>> row.cellrow
        1
        >>> try:
        ...     row.cellrow = 2
        ... except AssertionError:
        ...     print('Assert')
        Assert
        """
        if self._cellrow is None:
            for layer in [x for x in self if x.cellrow is not None]:
                self.cellrow = layer.cellrow
        return self._cellrow

    @cellrow.setter
    def cellrow(self, theValue):
        """Set _cellrow attribute value
        """
        if self._cellrow is None:
            self._cellrow = theValue
        else:
            assert self._cellrow == theValue

    def append(self, theValue):
        """Appends a new layer to the row. Not allowed.

        >>> row = BRow(2)
        >>> try:
        ...     row.append(None)
        ... except NotImplementedError:
        ...     print('NotImplemented')
        NotImplemented
        """
        raise NotImplementedError

    def pop(self):
        """Returns the last layer from the row. Not Allowed.

        >>> row = BRow(2)
        >>> try:
        ...     row.pop()
        ... except NotImplementedError:
        ...     print('NotImplemented')
        NotImplemented
        """
        raise NotImplementedError

    def add_cell_to_layer(self, cell, layer):
        """Adds a new cell to the given layer.

        >>> row = BRow(2)
        >>> row.add_cell_to_layer(BCell(0, 0, None), LType.SURFACE)
        True
        >>> row[LType.SURFACE.value]
        [LType.SURFACE]  <0>   cell# 1
        """
        assert isinstance(cell, BCell)
        assert isinstance(layer, LType)
        self.cellrow = cell.row
        self[layer.value].append(cell)
        cell.Layer = layer
        return True

    def remove_cell_from_layer(self, cell, layer):
        """Removes a cell from the given layer.

        >>> row = BRow(2)
        >>> cell = BCell(0, 0, None)
        >>> row.add_cell_to_layer(cell, LType.SURFACE)
        True
        >>> len(row[LType.SURFACE.value])
        1
        >>> row.remove_cell_from_layer(cell, LType.SURFACE)
        True
        >>> len(row[LType.SURFACE.value])
        0
        >>> row.remove_cell_from_layer(cell, LType.SURFACE)
        False
        """
        assert isinstance(cell, BCell)
        assert isinstance(layer, LType)
        return self[layer.value].remove(cell)

    def populate_layer(self, cell, layer):
        """Populate a layer with the same cell.

        >>> row = BRow(2)
        >>> cell = BCell(0, 0, None)
        >>> row.populate_layer(cell, LType.SURFACE)
        True
        >>> len(row[LType.SURFACE.value])
        2
        >>> row[LType.SURFACE.value]
        [LType.SURFACE]  <0>   cell# 2
        >>> for index in range(2):
        ...     row[LType.SURFACE.value][index]
        (0, 0) : None
        (1, 0) : None
        """
        for index in range(self.Width):
            new_cell = cell.__class__(cell.x + index, cell.y, cell.name)
            self.add_cell_to_layer(new_cell, layer)
        return True

    def clear_layer(self, layer):
        """Clear all cells from a layer.

        >>> row = BRow(2)
        >>> cell = BCell(0, 0, None)
        >>> row.populate_layer(cell, LType.SURFACE)
        True
        >>> len(row[LType.SURFACE.value])
        2
        >>> row.clear_layer(LType.SURFACE)
        True
        >>> len(row[LType.SURFACE.value])
        0
        """
        assert isinstance(layer, LType)
        for index in range(len(self[layer.value])):
            del self[layer.value]
        return True

    def get_cells_from_layer(self, layers):
        """Returns all cells from the given layer.

        """
        cells  = []
        for layer in [x for x in self if x.type in layers]:
            cells.extend([cell for cell in layer])
        return cells

    def get_cell_by_id(self, id):
        """Returns a cell by the given ID.

        Args:
            id (int) : Integer with the cell ID.

        Returns:
            BCell : Cell instance with the given ID. None if no cell\
                    was found.

        Example:
            >>> row = BRow(2)
            >>> c1 = BCell(0, 0, None)
            >>> c2 = BCell(1, 0, None)
            >>> row.add_cell_to_layer(c1, LType.SURFACE)
            True
            >>> row.add_cell_to_layer(c2, LType.SURFACE)
            True
            >>> row.get_cell_by_id(c1.id) == c1
            True
        """
        for layer in self:
            cell = layer.get_cell_by_id(id)
            if cell is not None:
                return cell
        return None

    def row_to_string(self):
        """Returns string with row representation

        Returns:
            str : String with all cells in the row.
        """
        cells = OrderedDict()
        for layer in [x for x in self if len(x)]:
            for cell in layer:
                key = '{0},{1}'.format(cell.col, cell.row)
                cells.update({key: cell})
        cell_str = ['{0:^8}'.format(str(x.name)) for x in cells.values()]
        return " ".join(cell_str)

    def render(self, **kwargs):
        """Render the row.

        When rendering in text format, it returns a string where every cell is
        just a set of characters.

        When rendering in graph format, we have to pass the row position with
        x and y values, so sprites are properly located, and it has to return
        a list of sprites, which should be included in a sprite group from the
        graphical framework.

        Keyword Args:
            render (BRender) : Render type (graphical or text).
            width (int) : Width for text rendering for cell width.

        Returns:
            object : Instance to be rendered.
        """
        render = kwargs.get('render', BRender.DEFAULT)
        cells = OrderedDict()
        for layer in [x for x in self if len(x)]:
            for cell in layer:
                key = '{0},{1}'.format(cell.col, cell.row)
                cells.update({key: cell.render(render)})
        if render == BRender.TEXT:
            width = kwargs.get('width', 5)
            cell_str = ['{0}'.format(x.center(width)) for x in cells.values()]
            return " ".join(cell_str)
        elif render == BRender.GRAPH:
            return cells
        else:
            raise NotImplementedError

    def __repr__(self):
        """String representation for BRow instance.

        Returns:
            str : string with the BRow instance representation.

        >>> row = BRow(5)
        >>> row
        Row: None
          [LType.HIDDEN ] <None> cell# 0
          [LType.UNDER  ] <None> cell# 0
          [LType.SURFACE] <None> cell# 0
          [LType.OBJECT ] <None> cell# 0
          [LType.OVER   ] <None> cell# 0
          [LType.MASK   ] <None> cell# 0
        <BLANKLINE>
        """
        st = 'Row: {0}\n'.format(self.cellrow)
        for layer in self:
            st += '  {0}\n'.format(str(layer).replace('\n', '\n  '))
        return st

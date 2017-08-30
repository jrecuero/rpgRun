from itero import Itero
from blayer import BLayer
from bcell import BCell


class BRow(Itero):
    """BRow class derives from Itero class and it provides some
    particular functinality for a row in the board.

    BRow contains a fixed number of BLayer instances (one per
    BLayer.LType).

    Every layer in the row  contains a number of cells, provided
    as the MaxLen if the Row.
    """

    def __init__(self, theMaxLen):
        """BRow class initialization method.
        >>> row = BRow(5)
        >>> row.MaxLen
        5
        """
        super(BRow, self).__init__(BLayer, theMaxLen)
        for layer in BLayer.LType:
            self._Itero__stream.append(BLayer(layer, theMaxLen))
        self._cellRow = None

    @property
    def Width(self):
        """
        >>> row = BRow(10)
        >>> row.Width
        10
        """
        return self.MaxLen

    @property
    def CellRow(self):
        """
        >>> row = BRow(2)
        >>> row.CellRow
        >>> row[0].append(BCell(0, 1, None))
        >>> row.CellRow
        1
        >>> try:
        ...     row.CellRow = 2
        ... except AssertionError:
        ...     print('Assert')
        Assert
        """
        if self._cellRow is None:
            for layer in [x for x in self if x.CellRow is not None]:
                self.CellRow = layer.CellRow
        return self._cellRow

    @CellRow.setter
    def CellRow(self, theValue):
        if self._cellRow is None:
            self._cellRow = theValue
        else:
            assert self._cellRow == theValue

    def append(self, theValue):
        """
        >>> row = BRow(2)
        >>> try:
        ...     row.append(None)
        ... except NotImplementedError:
        ...     print('NotImplemented')
        NotImplemented
        """
        raise NotImplementedError

    def pop(self):
        """
        >>> row = BRow(2)
        >>> try:
        ...     row.pop()
        ... except NotImplementedError:
        ...     print('NotImplemented')
        NotImplemented
        """
        raise NotImplementedError

    def addCellToLayer(self, theCell, theLayer):
        """
        >>> row = BRow(2)
        >>> row.addCellToLayer(BCell(0, 0, None), BLayer.LType.SURFACE)
        True
        >>> row[BLayer.LType.SURFACE.value]
        [LType.SURFACE]  <0>   cell# 1
        """
        assert isinstance(theCell, BCell)
        assert isinstance(theLayer, BLayer.LType)
        self.CellRow = theCell.Row
        self[theLayer.value].append(theCell)
        return True

    def removeCellFromLayer(self, theCell, theLayer):
        """
        >>> row = BRow(2)
        >>> cell = BCell(0, 0, None)
        >>> row.addCellToLayer(cell, BLayer.LType.SURFACE)
        True
        >>> len(row[BLayer.LType.SURFACE.value])
        1
        >>> row.removeCellFromLayer(cell, BLayer.LType.SURFACE)
        True
        >>> len(row[BLayer.LType.SURFACE.value])
        0
        >>> row.removeCellFromLayer(cell, BLayer.LType.SURFACE)
        False
        """
        assert isinstance(theCell, BCell)
        assert isinstance(theLayer, BLayer.LType)
        try:
            self[theLayer.value].remove(theCell)
            return True
        except ValueError:
            return False

    def populateLayer(self, theCell, theLayer):
        """Populate a layer with the same cell.

        >>> row = BRow(2)
        >>> cell = BCell(0, 0, None)
        >>> row.populateLayer(cell, BLayer.LType.SURFACE)
        True
        >>> len(row[BLayer.LType.SURFACE.value])
        2
        >>> row[BLayer.LType.SURFACE.value]
        [LType.SURFACE]  <0>   cell# 2
        >>> for index in range(2):
        ...     row[BLayer.LType.SURFACE.value][index]
        (0, 0) : None
        (1, 0) : None
        """
        for index in range(self.Width):
            newCell = theCell.__class__(theCell.X + index, theCell.Y, theCell.Name)
            self.addCellToLayer(newCell, theLayer)
        return True

    def clearLayer(self, theLayer):
        """Clear all cells from a layer.

        >>> row = BRow(2)
        >>> cell = BCell(0, 0, None)
        >>> row.populateLayer(cell, BLayer.LType.SURFACE)
        True
        >>> len(row[BLayer.LType.SURFACE.value])
        2
        >>> row.clearLayer(BLayer.LType.SURFACE)
        True
        >>> len(row[BLayer.LType.SURFACE.value])
        0
        """
        assert isinstance(theLayer, BLayer.LType)
        for index in range(len(self[theLayer.value])):
            del self[theLayer.value]
        return True

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
        <BLANKLINE>
        """
        st = 'Row: {0}\n'.format(self.CellRow)
        for layer in self:
            st += '  {0}\n'.format(str(layer).replace('\n', '\n  '))
        return st

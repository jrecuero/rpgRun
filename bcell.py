import itertools
from bpoint import BPoint


class BCell(BPoint):
    """BCell class derives from BPoint class and it provides some additional
    functionality for any object placed on the board.
    """

    __newId = itertools.count(1)

    def __init__(self, theX, theY, theName):
        """BCell class initialization method.
        """
        super(BCell, self).__init__(theX, theY)
        self._id = next(BCell.__newId)
        self._name = theName
        self._static = True
        self._walkable = True
        self._solid = True

    @property
    def Id(self):
        """
        """
        return self._id

    @property
    def Name(self):
        """
        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Name
        'cell'
        """
        return self._name

    @Name.setter
    def Name(self, theValue):
        """
        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Name
        'cell'
        >>> cell.Name = 'new cell'
        >>> cell.Name
        'new cell'
        """
        self._name = theValue

    @property
    def Row(self):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Row
        2
        """
        return self.Y

    @property
    def Col(self):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Col
        1
        """
        return self.X

    @property
    def Static(self):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Static
        True
        """
        return self._static

    @Static.setter
    def Static(self, theValue):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Static
        True
        >>> cell.Static = False
        >>> cell.Static
        False
        """
        self._static = theValue

    @property
    def Walkable(self):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Walkable
        True
        """
        return self._walkable

    @Walkable.setter
    def Walkable(self, theValue):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Walkable
        True
        >>> cell.Walkable = False
        >>> cell.Walkable
        False
        """
        self._walkable = theValue

    @property
    def Solid(self):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Solid
        True
        """
        return self._solid

    @Solid.setter
    def Solid(self, theValue):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Solid
        True
        >>> cell.Solid = False
        >>> cell.Solid
        False
        """
        self._solid = theValue

    def __repr__(self):
        """String representation for the BCell instance.

        Returns:
            str : string with the BCell instance representation.

        >>> str(BCell(0, 0, 'cell'))
        '(0, 0) : cell'
        """
        return '{0} : {1}'.format(super(BCell, self).__repr__(), self.Name)

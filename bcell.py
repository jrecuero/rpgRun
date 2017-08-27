import itertools
from bpoint import BPoint


class BCell(BPoint):

    __newId = itertools.count(1)

    def __init__(self, theX, theY, theName):
        super(BCell, self).__init__(theX, theY)
        self._id = next(BCell.__newId)
        self._name = theName
        self._static = True
        self._walkable = True
        self._solid = True

    @property
    def Id(self):
        return self._id

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, theValue):
        self._name = theValue

    @property
    def Row(self):
        return self.Y

    @property
    def Col(self):
        return self.X

    @property
    def Static(self):
        return self._static

    @Static.setter
    def Static(self, theValue):
        self._static = theValue

    @property
    def Walkable(self):
        return self._walkable

    @Walkable.setter
    def Walkable(self, theValue):
        self._walkable = theValue

    @property
    def Solid(self):
        return self._solid

    @Solid.setter
    def Solid(self, theValue):
        self._solid = theValue

    def __repr__(self):
        """
        >>> str(BCell(0, 0, 'cell'))
        '(0, 0) : cell'
        """
        return '{0} : {1}'.format(super(BCell, self).__repr__(), self.Name)

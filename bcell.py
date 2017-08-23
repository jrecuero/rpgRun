import itertools
from bpoint import BPoint


class BCell(BPoint):

    __newId = itertools.count(1)

    def __init__(self, theX, theY, theName):
        super(BCell, self).__init__(theX, theY)
        self._id = next(BCell.__newId)
        self._name = theName

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

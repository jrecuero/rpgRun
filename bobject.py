from bcell import BCell


@staticmethod
def isObject():
    return False


BCell.isObject = isObject


class BObject(BCell):
    """BObject class derives from BCell and it implements particular
    functionality for cells in the OBJECT layer.
    """

    def __init__(self, theX, theY, theName):
        super(BObject, self).__init__(theX, theY, theName)
        self.Walkable = False

    def isObject(self):
        """Returns if the instance is a BObject.
        """
        return True

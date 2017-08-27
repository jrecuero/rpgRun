from bcell import BCell


@staticmethod
def isObject():
    return False


BCell.isObject = isObject


class BObject(BCell):

    def __init__(self, theX, theY, theName):
        super(BObject, self).__init__(theX, theY, theName)
        self.Walkable = False

    def isObject(self):
        return True

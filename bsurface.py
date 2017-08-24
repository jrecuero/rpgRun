from bcell import BCell


@staticmethod
def isSurface():
    return False


BCell.isSurface = isSurface


class BSurface(BCell):

    def __init__(self, theX, theY, theName):
        super(BSurface, self).__init__(theX, theY, theName)

    def isSurface(self):
        return True

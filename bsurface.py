from bcell import BCell


@staticmethod
def isSurface():
    return False


BCell.isSurface = isSurface


class BSurface(BCell):
    """BSurface class derives from BCell and it implements particular
    functionality for cells in the SURFACE layer.
    """

    def __init__(self, theX, theY, theName, **kwargs):
        """BSurface class initialization method.
        """
        super(BSurface, self).__init__(theX, theY, theName, **kwargs)
        self.Solid = False

    def isSurface(self):
        """Returns if the instance is a BSurface.
        """
        return True

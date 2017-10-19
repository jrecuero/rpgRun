from rpgrun.bcell import BCell


@staticmethod
def is_surface():
    """Returns if the instance is a BSurface.
    """
    return False


BCell.is_surface = is_surface


class BSurface(BCell):
    """BSurface class derives from BCell and it implements particular
    functionality for cells in the SURFACE layer.
    """

    def __init__(self, x, y, name, **kwargs):
        """BSurface class initialization method.
        """
        super(BSurface, self).__init__(x, y, name, **kwargs)
        self.solid = False

    def is_surface(self):
        """Returns if the instance is a BSurface.
        """
        return True

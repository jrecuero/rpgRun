from rpgrun.game.gitem import GItem
from rpgrun.game.gcatalog import Catalog


class Inventory(Catalog):
    """Inventory class derives from :class:`gcatalog.Catalog` and it contains all items that
    belong to an actor inventory.
    """

    def __init__(self, **kwargs):
        """Inventory class initialization method.
        """
        super(Inventory, self).__init__(GItem, **kwargs)

from gitem import GItem
from itero import Itero


class Inventory(Itero):
    """Inventory class contains all items that belong to an actor inventory.
    """

    def __init__(self, **kwargs):
        """Inventory class initialization method.
        """
        super(Inventory, self).__init__(GItem, kwargs.get('theSize', None))
        self._host = kwargs.get('theHost', None)

    @property
    def Host(self):
        """Gets _host attribute value.

        >>> inv = Inventory()
        >>> inv.Host
        >>> inv = Inventory(theHost='me')
        >>> inv.Host
        'me'
        """
        return self._host

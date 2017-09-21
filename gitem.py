from gobject import GObject


class ItemType(object):
    """
    """

    @staticmethod
    def Name():
        """
        """
        return 'ITEM'


class GItem(GObject):
    """
    """

    TYPES = {ItemType.Name: ItemType, }

    def __init__(self, **kwargs):
        """GItem class initialization method.
        """
        super(GItem, self).__init__(**kwargs)
        self._host = kwargs.get('theHost', None)
        self._typename = ItemType.Name

    @staticmethod
    def addType(theType):
        assert issubclass(theType, ItemType)
        GItem.TYPES.update({theType.Name: theType})

    @property
    def Host(self):
        """Gets _host attribute value.

        >>> it = GItem()
        >>> it.Host
        >>> it = GItem(theHost='me')
        >>> it.Host
        'me'
        """
        return self._host

    @Host.setter
    def Host(self, theValue):
        """Sets _host attribute value.

        >>> it = GItem()
        >>> it.Host
        >>> it.Host = 'me'
        >>> it.Host
        'me'

        >>> it = GItem(theHost='you')
        >>> it.Host
        'you'
        >>> it.Host = 'they'
        >>> it.Host
        'they'
        """
        self._host = theValue

    @property
    def TypeName(self):
        """
        """
        return self._typename

    @property
    def Type(self):
        """
        """
        return GItem.TYPES.get(self.TypeName, None)

    def buffHost(self):
        """
        """
        pass

    def debuffHost(self):
        """
        """
        pass

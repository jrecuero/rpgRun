from gobject import GObject


class GItem(GObject):
    """
    """

    def __init__(self, **kwargs):
        """GItem class initialization method.
        """
        super(GItem, self).__init__(**kwargs)
        self._host = kwargs.get('theHost', None)

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

    def buffHost(self):
        """

        >>> it = GItem()
        >>> try:
        ...     it.buffHost()
        ... except NotImplementedError:
        ...     'NotImplemented'
        'NotImplemented'
        """
        raise NotImplementedError

    def debuffHost(self):
        """

        >>> it = GItem()
        >>> try:
        ...     it.debuffHost()
        ... except NotImplementedError:
        ...     'NotImplemented'
        'NotImplemented'
        """
        raise NotImplementedError

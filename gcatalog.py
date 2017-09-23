from itero import StrItero


class Catalog(StrItero):
    """Catalog class derives from :class:`itero.StrItero` and it is base class that can be
    use for inventories, equipments and any other resource that requires to
    store information by a key.

    Information stored should have a Name attribute and it shoudl have a Host
    that owns are resources stored.
    """

    def __init__(self, theKlass, **kwargs):
        """Catalog class initialization method.
        """
        assert hasattr(theKlass, 'Name')
        super(Catalog, self).__init__(theKlass)
        self._host = kwargs.get('theHost', None)

    @property
    def Host(self):
        """Gets _host attribute value.

        Returns:
            Actor : Actor that owns the catalog.

        Example:
            >>> class A(object):
            ...     Name = None
            >>> inv = Catalog(A)
            >>> inv.Host
            >>> inv = Catalog(A, theHost='me')
            >>> inv.Host
            'me'
            >>> try:
            ...     inv = Catalog(str)
            ... except AssertionError:
            ...     'Assertion'
            'Assertion'
        """
        return self._host

    def append(self, theEntry):
        """Updates the instance with the given key-value pairs.

        Args:
            theEntry (object) : Instance to be added.

        Returns:
            None
        """
        _key = theEntry.Name
        super(Catalog, self).update(_key, theEntry)

    def remove(self, theEntry):
        """Removes the given value from the instance.

        Args:
            theEntry (object or str) : Instance or instance name to be deleted.

        Returns:
            bool : True if entry was deleted, False else.
        """
        try:
            _key = theEntry.Name if isinstance(theEntry, self._StrItero__streamKlass) else theEntry
            del self[_key]
            return True
        except ValueError:
            return False

from rpgrun.common.itero import StrItero


class Catalog(StrItero):
    """Catalog class derives from :class:`itero.StrItero` and it is base class that can be
    use for inventories, equipments and any other resource that requires to
    store information by a key.

    Information stored should have a name attribute and it shoudl have a Host
    that owns are resources stored.
    """

    def __init__(self, klass, **kwargs):
        """Catalog class initialization method.

        Args:
            klass (class) : Class conteined in the catalog.
        """
        super(Catalog, self).__init__(klass)
        self.host = kwargs.get('host', None)

    def append(self, entry):
        """Updates the instance with the given key-value pairs.

        Args:
            entry (object) : Instance to be added.

        Returns:
            None

        Example:
            >>> class Item(object):
            ...     def __init__(self, name, value):
            ...         self.name = name
            ...         self.value = value
            >>> c = Catalog(Item)
            >>> it = Item('me', 100)
            >>> c.append(it)
            >>> it = Item('you', 50)
            >>> c.append(it)
            >>> c['me'].value
            100
            >>> c['you'].value
            50
        """
        key = entry.name
        super(Catalog, self).update(key, entry)

    def remove(self, entry):
        """Removes the given value from the instance.

        Args:
            entry (object or str) : Instance or instance name to be deleted.

        Returns:
            bool : True if entry was deleted, False else.

        Example:
            >>> class Item(object):
            ...     def __init__(self, name, value):
            ...         self.name = name
            ...         self.value = value
            >>> c = Catalog(Item)
            >>> it = Item('me', 100)
            >>> c.append(it)
            >>> it = Item('you', 50)
            >>> c.append(it)
            >>> c.remove('me')
            True
            >>> try:
            ...     c['me'].value
            ... except KeyError:
            ...     'KeyError for me'
            'KeyError for me'
            >>> c.remove('me')
            False
            >>> c.remove(it)
            True
            >>> try:
            ...     c['you'].value
            ... except KeyError:
            ...     'KeyError for you'
            'KeyError for you'
        """
        try:
            key = entry.name if isinstance(entry, self._StrItero__stream_class) else entry
            del self[key]
            return True
        except KeyError:
            return False

    def get_by_id(self, id):
        """Returns an entry by the given ID.

        Args:
            id (int) : Integer with the entry ID.

        Returns:
            object : Entry instance with the given ID. None if no entry\
                    was found.
        """
        for entry in self:
            if entry.id == id:
                return entry
        return None

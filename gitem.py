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

        Keyword Args:
            theHost (Actor) : Actor instance that owns the item.

            theAttrBuff (dict(str, int)) : Dictionary with pairs of attribute\
                    name and attribute value to be used as buff to the Host.

        Raises:
            AssertionError
        """
        super(GItem, self).__init__(**kwargs)
        self._host = kwargs.get('theHost', None)
        self._typename = ItemType.Name
        self._attrBuff = kwargs.get('theAttrBuff', {})
        assert isinstance(self._attrBuff, dict)

    @staticmethod
    def addType(theType):
        assert issubclass(theType, ItemType)
        GItem.TYPES.update({theType.Name: theType})

    @property
    def Host(self):
        """Property for _host attribute.

        :getter: Gets _host attribute value.
        :setter: Sets _host attribute value.

        Returns:
            Actor : Actor instance that owns the item

        Example:
            >>> it = GItem()
            >>> it.Host
            >>> it = GItem(theHost='me')
            >>> it.Host
            'me'
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
        return self._host

    @Host.setter
    def Host(self, theValue):
        """Set property for _host attribute.
        """
        self._host = theValue

    @property
    def TypeName(self):
        """Property for _typename attribute.

        :getter: Gets _typename attribute value.

        Returns:
            str : string with the item type.
        """
        return self._typename

    @property
    def Type(self):
        """Property for the iten type.

        :getter: gets item type

        Returns:
            ItemType : ItemType value for the item..
        """
        return GItem.TYPES.get(self.TypeName, None)

    @property
    def AttrBuff(self):
        """Property for _attrBuff attribute.

        :getter: Gets _attrBuff attribute value.

        Returns:
            dict : Dictionary with all attribute name and value pairs.
        """
        return self._attrBuff

    def buffHost(self):
        """Add a buff to the Host.

        Returns:
            None
        """
        for k, v in self.AttrBuff.items():
            self.Host.Attrs[k].addBuff(self.Name, v)

    def debuffHost(self):
        """Removes a buff from the host.

        Returns:
            None
        """
        for k, v in self.AttrBuff.items():
            self.Host.Attrs[k].delBuff(self.Name)

    def __repr__(self):
        """Instance representation as a string.

        Returns:
            str : String with the instance representation.
        """
        return '{0}: {1} {2}'.format(self.__class__, self.Name, self.AttrBuff)

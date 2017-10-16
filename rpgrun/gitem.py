from gobject import GObject


class ItemType(object):
    """
    """

    @staticmethod
    def name():
        """
        """
        return 'ITEM'


class GItem(GObject):
    """
    """

    TYPES = {ItemType.name: ItemType, }

    def __init__(self, **kwargs):
        """GItem class initialization method.

        Keyword Args:
            host (Actor) : Actor instance that owns the item.

            attr_buff (dict(str, int)) : Dictionary with pairs of attribute\
                    name and attribute value to be used as buff to the Host.

        Raises:
            AssertionError
        """
        super(GItem, self).__init__(**kwargs)
        self.host = kwargs.get('host', None)
        self.typename = ItemType.name
        self.attr_buff = kwargs.get('attr_buff', {})
        assert isinstance(self.attr_buff, dict)

    @staticmethod
    def add_type(type_):
        assert issubclass(type_, ItemType)
        GItem.TYPES.update({type_.name: type_})

    def get_type(self):
        """Property for the iten type.

        :getter: gets item type

        Returns:
            ItemType : ItemType value for the item..
        """
        return GItem.TYPES.get(self.typename, None)

    def buff_host(self):
        """Add a buff to the Host.

        Returns:
            None
        """
        for k, v in self.attr_buff.items():
            self.host.attrs[k].add_buff(self.name, v)

    def debuff_host(self):
        """Removes a buff from the host.

        Returns:
            None
        """
        for k, v in self.attr_buff.items():
            self.host.attrs[k].del_buff(self.name)

    def __repr__(self):
        """Instance representation as a string.

        Returns:
            str : String with the instance representation.
        """
        return '{0}: {1} {2}'.format(self.__class__.__name__, self.name, self.attr_buff)

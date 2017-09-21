from gitem import GItem, ItemType


@staticmethod
def isEquip():
    """Returns if the instance is a GEquip.
    """
    return False


class EquipType(ItemType):
    """
    """

    @staticmethod
    def Name():
        """
        """
        return 'EQUIP'


class GEquip(GItem):
    """
    """
    GItem.addType(EquipType)

    def __init__(self, **kwargs):
        """GEquip class initialization method.
        """
        super(GEquip, self).__init__(**kwargs)
        self._equipped = False

    @property
    def Equipped(self):
        """Gets _equipped attribute value.

        >>> eq = GEquip()
        >>> eq.Equipped
        False
        """
        return self._equipped

    @Equipped.setter
    def Equipped(self, theValue):
        """Sets _equipped attribute value.

        >>> eq = GEquip()
        >>> eq.Equipped
        False
        >>> eq.Equipped = True
        >>> eq.Equipped
        True
        """
        self._equipped = theValue

    def isEquip(self):
        """Returns if the instance is a GEquip.
        """
        return True

    def inEquipment(self, theHost):
        """Equips equipment items.

        >>> class MyEquip(GEquip):
        ...     def buffHost(self):
        ...         print('buff-host')
        ...     def debuffHost(self):
        ...         print('debuff-host')
        >>> eq = MyEquip()
        >>> eq.Host, eq.Equipped
        (None, False)
        >>> eq.inEquipment('me')
        buff-host
        >>> eq.Host, eq.Equipped
        ('me', True)
        """
        self.Host = theHost
        self.Equipped = True
        self.buffHost()

    def outEquipment(self):
        """Unequips equipment item.

        >>> class MyEquip(GEquip):
        ...     def buffHost(self):
        ...         print('buff-host')
        ...     def debuffHost(self):
        ...         print('debuff-host')
        >>> eq = MyEquip()
        >>> eq.inEquipment('me')
        buff-host
        >>> eq.Host, eq.Equipped
        ('me', True)
        >>> eq.outEquipment()
        debuff-host
        >>> eq.Host, eq.Equipped
        (None, False)
        """
        self.debuffHost()
        self.Host = None
        self.Equipped = False

from gitem import GItem, ItemType
from action import Actions


@staticmethod
def isEquip():
    """Returns if the instance is a GEquip.

    Returns:
        bool : False always for none equipment.
    """
    return False


GItem.isEquip = isEquip


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
        self._actions = Actions()

    @property
    def Equipped(self):
        """Property for _equipped attribute.

        :getter: Gets _equipped attribute value.
        :setter: Sets _equipped attribute value.

        Returns:
            bool : True if equip is equipped

        Example:
            >>> eq = GEquip()
            >>> eq.Equipped
            False
            >>> eq.Equipped = True
            >>> eq.Equipped
            True
        """
        return self._equipped

    @Equipped.setter
    def Equipped(self, theValue):
        """Set property for _equipped attribute.
        """
        self._equipped = theValue

    @property
    def Actions(self):
        """Gets _actions attribute value.
        """
        return self._actions

    def isEquip(self):
        """Returns if the instance is a GEquip.

        Returns:
            bool : True always for equipment.
        """
        return True

    def inEquipment(self, theHost):
        """Equips equipment items.

        Args:
            theHost (Actor) : Actor where equip will be equipped.

        Returns:
            None

        Example:
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

        Returns:
            None

        Example:
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

from rpgrun.game.gitem import GItem, ItemType
from rpgrun.game.action import Actions


@staticmethod
def is_equip():
    """Returns if the instance is a GEquip.

    Returns:
        bool : False always for none equipment.
    """
    return False


GItem.is_equip = is_equip


class EquipType(ItemType):
    """
    """

    @staticmethod
    def name():
        """
        """
        return 'EQUIP'


class GEquip(GItem):
    """
    """
    GItem.add_type(EquipType)

    def __init__(self, **kwargs):
        """GEquip class initialization method.
        """
        super(GEquip, self).__init__(**kwargs)
        self.equipped = False
        self.actions = Actions()

    def is_equip(self):
        """Returns if the instance is a GEquip.

        Returns:
            bool : True always for equipment.
        """
        return True

    def in_equipment(self, host):
        """Equips equipment items.

        Args:
            host (Actor) : Actor where equip will be equipped.

        Returns:
            None

        Example:
            >>> class MyEquip(GEquip):
            ...     def buff_host(self):
            ...         print('buff-host')
            ...     def debuff_host(self):
            ...         print('debuff-host')
            >>> eq = MyEquip()
            >>> eq.host, eq.equipped
            (None, False)
            >>> eq.in_equipment('me')
            buff-host
            >>> eq.host, eq.equipped
            ('me', True)
        """
        self.host = host
        self.equipped = True
        self.buff_host()

    def out_equipment(self):
        """Unequips equipment item.

        Returns:
            None

        Example:
            >>> class MyEquip(GEquip):
            ...     def buff_host(self):
            ...         print('buff-host')
            ...     def debuff_host(self):
            ...         print('debuff-host')
            >>> eq = MyEquip()
            >>> eq.in_equipment('me')
            buff-host
            >>> eq.host, eq.equipped
            ('me', True)
            >>> eq.out_equipment()
            debuff-host
            >>> eq.host, eq.equipped
            (None, False)
        """
        self.debuff_host()
        self.host = None
        self.equipped = False

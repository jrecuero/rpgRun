from rpgrun.game.gequip import GEquip
from rpgrun.game.gcatalog import Catalog


class Equipment(Catalog):
    """Equipment class derives from Catalog and it contains all data
    related with items equiped by an actor.
    """

    def __init__(self, **kwargs):
        """Equipment class initialization method.
        """
        super(Equipment, self).__init__(GEquip, **kwargs)

    def append(self, equip):
        """Appends a new entry to the Equipment.

        Args:
            equip (GEquip) : Equip instance to be added.

        Returns:
            None

        Example:
            >>> class MyEquip(GEquip):
            ...     def buff_host(self):
            ...         print('buff-host')
            ...     def debuff_host(self):
            ...         print('debuff-host')
            >>> eqp = Equipment(host='me')
            >>> myeq = MyEquip(name='myeqpt')
            >>> myeq.name, myeq.host, myeq.equipped
            ('myeqpt', None, False)
            >>> eqp.append(myeq)
            buff-host
            >>> myeq.name, myeq.host, myeq.equipped
            ('myeqpt', 'me', True)
        """
        equip.in_equipment(self.host)
        super(Equipment, self).append(equip)

    def __delitem__(self, name):
        """Allows deleting data using indexed values for the instance.

        Args:
            name (str) : Name of the equipment to be deleted.

        Returns:
            None

        Example:
            >>> class MyEquip(GEquip):
            ...     def buff_host(self):
            ...         print('buff-host')
            ...     def debuff_host(self):
            ...         print('debuff-host')
            >>> eqp = Equipment(host='me')
            >>> myeq = MyEquip(name='myeqpt')
            >>> eqp.append(myeq)
            buff-host
            >>> myeq.name, myeq.host, myeq.equipped
            ('myeqpt', 'me', True)
            >>> del eqp['myeqpt']
            debuff-host
            >>> myeq.name, myeq.host, myeq.equipped
            ('myeqpt', None, False)
            >>> eqp.append(myeq)
            buff-host
            >>> eqp.remove(myeq)
            debuff-host
            True
        """
        equip = self[name]
        equip.out_equipment()
        super(Equipment, self).__delitem__(name)

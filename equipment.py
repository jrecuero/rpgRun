from gequip import GEquip
from gcatalog import Catalog


class Equipment(Catalog):
    """Equipment class derives from Catalog and it contains all data
    related with items equiped by an actor.
    """

    def __init__(self, **kwargs):
        """Equipment class initialization method.
        """
        super(Equipment, self).__init__(GEquip, **kwargs)

    def append(self, theEquip):
        """Appends a new entry to the Equipment.

        Args:
            theEquip (GEquip) : Equip instance to be added.

        Returns:
            None

        Example:
            >>> class MyEquip(GEquip):
            ...     def buffHost(self):
            ...         print('buff-host')
            ...     def debuffHost(self):
            ...         print('debuff-host')
            >>> eqp = Equipment(theHost='me')
            >>> myeq = MyEquip(theName='myeqpt')
            >>> myeq.Name, myeq.Host, myeq.Equipped
            ('myeqpt', None, False)
            >>> eqp.append(myeq)
            buff-host
            >>> myeq.Name, myeq.Host, myeq.Equipped
            ('myeqpt', 'me', True)
        """
        theEquip.inEquipment(self.Host)
        super(Equipment, self).append(theEquip)

    def __delitem__(self, theName):
        """Allows deleting data using indexed values for the instance.

        Args:
            theName (str) : Name of the equipment to be deleted.

        Returns:
            None

        Example:
            >>> class MyEquip(GEquip):
            ...     def buffHost(self):
            ...         print('buff-host')
            ...     def debuffHost(self):
            ...         print('debuff-host')
            >>> eqp = Equipment(theHost='me')
            >>> myeq = MyEquip(theName='myeqpt')
            >>> eqp.append(myeq)
            buff-host
            >>> myeq.Name, myeq.Host, myeq.Equipped
            ('myeqpt', 'me', True)
            >>> del eqp['myeqpt']
            debuff-host
            >>> myeq.Name, myeq.Host, myeq.Equipped
            ('myeqpt', None, False)
            >>> eqp.append(myeq)
            buff-host
            >>> eqp.remove(myeq)
            debuff-host
            True
        """
        equip = self[theName]
        equip.outEquipment()
        super(Equipment, self).__delitem__(theName)

from gequip import GEquip
from itero import Itero


class Equipment(Itero):
    """
    """

    def __init__(self, **kwargs):
        """Equipment class initialization method.
        """
        super(Equipment, self).__init__(GEquip, kwargs.get('theSize', None))
        self._host = kwargs.get('theHost', None)

    @property
    def Host(self):
        """Gets _host attribute value.

        >>> eqp = Equipment()
        >>> eqp.Host
        >>> eqp = Equipment(theHost='me')
        >>> eqp.Host
        'me'
        """
        return self._host

    def append(self, theEquip):
        """

        >>> class MyEquip(GEquip):
        ...     def buffHost(self):
        ...         print('buff-host')
        ...     def debuffHost(self):
        ...         print('debuff-host')
        >>> eqp = Equipment(theHost='me')
        >>> myeq = MyEquip()
        >>> myeq.Host, myeq.Equipped
        (None, False)
        >>> eqp.append(myeq)
        buff-host
        >>> myeq.Host, myeq.Equipped
        ('me', True)
        """
        theEquip.inEquipment(self.Host)
        super(Equipment, self).append(theEquip)

    def __delitem__(self, theKey):
        """

        >>> class MyEquip(GEquip):
        ...     def buffHost(self):
        ...         print('buff-host')
        ...     def debuffHost(self):
        ...         print('debuff-host')
        >>> eqp = Equipment(theHost='me')
        >>> myeq = MyEquip()
        >>> eqp.append(myeq)
        buff-host
        >>> myeq.Host, myeq.Equipped
        ('me', True)
        >>> del eqp[0]
        debuff-host
        >>> myeq.Host, myeq.Equipped
        (None, False)
        >>> eqp.append(myeq)
        buff-host
        >>> eqp.remove(myeq)
        debuff-host
        True
        """
        equip = self[theKey]
        equip.outEquipment()
        super(Equipment, self).__delitem__(theKey)

    def pop(self):
        """

        >>> class MyEquip(GEquip):
        ...     def buffHost(self):
        ...         print('buff-host')
        ...     def debuffHost(self):
        ...         print('debuff-host')
        >>> eqp = Equipment(theHost='me')
        >>> myeq = MyEquip(theName='my equip')
        >>> eqp.append(myeq)
        buff-host
        >>> myeq.Host, myeq.Equipped
        ('me', True)
        >>> _ = eqp.pop()
        debuff-host
        >>> print(_.Name)
        my equip
        >>> myeq.Host, myeq.Equipped
        (None, False)
        """
        equip = super(Equipment, self).pop()
        equip.outEquipment()
        return equip

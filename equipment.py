from gitem import GItem
from itero import Itero


class GEquip(GItem):
    """
    """

    def __init__(self, **kwargs):
        """GEquip class initialization method.
        """
        super(GEquip, self).__init__(**kwargs)


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

    def append(self, theValue):
        """

        >>> class MyEquip(GEquip):
        ...     def buffHost(self):
        ...         print('buff-host')
        ...     def debuffHost(self):
        ...         print('debuff-host')
        >>> eqp = Equipment()
        >>> myeq = MyEquip()
        >>> eqp.append(myeq)
        buff-host
        """
        theValue.Host = self.Host
        theValue.buffHost()
        super(Equipment, self).append(theValue)

    def __delitem__(self, theKey):
        """

        >>> class MyEquip(GEquip):
        ...     def buffHost(self):
        ...         print('buff-host')
        ...     def debuffHost(self):
        ...         print('debuff-host')
        >>> eqp = Equipment()
        >>> myeq = MyEquip()
        >>> eqp.append(myeq)
        buff-host
        >>> del eqp[0]
        debuff-host
        >>> eqp.append(myeq)
        buff-host
        >>> eqp.remove(myeq)
        debuff-host
        True
        """
        equip = self[theKey]
        equip.debuffHost()
        super(Equipment, self).__delitem__(theKey)

    def pop(self):
        """

        >>> class MyEquip(GEquip):
        ...     def buffHost(self):
        ...         print('buff-host')
        ...     def debuffHost(self):
        ...         print('debuff-host')
        >>> eqp = Equipment()
        >>> myeq = MyEquip(theName='my equip')
        >>> eqp.append(myeq)
        buff-host
        >>> _ = eqp.pop()
        debuff-host
        >>> print(_.Name)
        my equip
        """
        equip = super(Equipment, self).pop()
        equip.debuffHost()
        return equip

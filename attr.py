from itero import StrItero


class Attr(object):
    """Attr Class contains all data related with a board object attribute.
    """

    def __init__(self, theName):
        """Attr class initialization method.
        """
        self._name = theName
        self._desc = None
        self._base = 0
        self._delta = 0
        self._buffs = {}

    @property
    def Name(self):
        """
        >>> at = Attr('new')
        >>> at.Name
        'new'
        """
        return self._name

    @Name.setter
    def Name(self, theValue):
        """
        >>> at = Attr('old')
        >>> at.Name
        old
        >>> at.Name = 'new'
        >>> at.Name
        'new'
        """
        self._name = theValue

    @property
    def Desc(self):
        """
        >>> at = Attr('new')
        >>> at.Desc
        ''
        >>> at.Desc = 'new attribute'
        >>> at.Desc
        'new attribute'
        """
        return self._desc if self._desc is not None else ''

    @Desc.setter
    def Desc(self, theValue):
        """
        """
        self._desc = theValue

    @property
    def Base(self):
        """
        >>> at = Attr('old')
        >>> at.Base
        0
        """
        return self._base

    @Base.setter
    def Base(self, theValue):
        """
        >>> at = Attr('old')
        >>> at.Base = 10
        >>> at.Base
        10
        """
        self._base = theValue

    @property
    def Delta(self):
        """
        >>> at = Attr('old')
        >>> at.Delta
        0
        """
        return self._delta

    @Delta.setter
    def Delta(self, theValue):
        """
        >>> at = Attr('old')
        >>> at.Delta = 1
        >>> at.Delta
        1
        """
        self._delta = theValue

    @property
    def Buffs(self):
        """
        >>> at = Attr('old')
        >>> at.Buffs
        {}
        """
        return self._buffs

    @property
    def Now(self):
        """
        >>> at = Attr('old')
        >>> at.Base = 5
        >>> at.Now
        5
        """
        return self.Base + sum(self.Buffs.values())

    def addBuff(self, theName, theValue):
        """
        >>> at = Attr('old')
        >>> at.addBuff('st', 5)
        True
        >>> at.addBuff('dx', 3)
        True
        >>> at.Buffs
        {'st': 5, 'dx': 3}
        >>> at.Now
        8
        """
        self._buffs.update({theName: theValue})
        return True

    def delBuff(self, theName):
        """
        >>> at = Attr('old')
        >>> at.addBuff('st', 5)
        True
        >>> at.addBuff('dx', 3)
        True
        >>> at.Buffs
        {'st': 5, 'dx': 3}
        >>> at.delBuff('st')
        True
        >>> at.Buffs
        {'dx': 3}
        """
        del self.Buffs[theName]
        return True

    def levelUp(self, theLevel=1):
        """
        >>> at = Attr('old')
        >>> at.Base = 10
        >>> at.Delta = 2
        >>> at.Base
        10
        >>> at.levelUp()
        >>> at.Base
        12
        >>> at.levelUp(3)
        >>> at.Base
        18
        """
        for _ in range(abs(theLevel)):
            self.Base += self.Delta * int(theLevel / abs(theLevel))

    def setupAttr(self, theBase=None, theDelta=None, theBuffs=None):
        """
        >>> at = Attr('new')
        >>> at
        new: 0/0
        >>> at.setupAttr(), at.Delta, at.Buffs
        (new: 0/0, 0, {})
        >>> at.setupAttr(10), at.Delta, at.Buffs
        (new: 10/10, 0, {})
        >>> at.setupAttr(5, 1), at.Delta, at.Buffs
        (new: 5/5, 1, {})
        >>> at.setupAttr(10, None, {'st': 1}), at.Delta, at.Buffs
        (new: 11/10, 1, {'st': 1})
        >>> at.setupAttr(None, 5, {'ag': 2}), at.Delta, at.Buffs
        (new: 13/10, 5, {'st': 1, 'ag': 2})
        """
        self.Base = theBase if theBase is not None else self.Base
        self.Delta = theDelta if theDelta is not None else self.Delta
        if theBuffs is not None and isinstance(theBuffs, dict):
            self.Buffs.update(theBuffs)
        return self

    def setupAttrFromJSON(self, theJsonFile):
        """
        """
        return self

    def __repr__(self):
        """
        >>> at = Attr('old')
        >>> at
        old: 0/0
        """
        return '{0}: {1}/{2}'.format(self.Name, self.Now, self.Base)


class Attributes(StrItero):
    """Attributes Class contains all attributes related with a board object.
    """

    def __init__(self):
        """Attribute class initialization method.

        >>> ats = Attributes()
        >>> ats['hp'] = Attr('hp')
        >>> ats['hp'].Name
        'hp'
        >>> ats['HP'].Name
        'hp'
        >>> ats['MP'] = Attr('mp')
        >>> ats['mp'].Name
        'mp'
        >>> ats['MP'].Name
        'mp'
        >>> del ats['hp']
        >>> try:
        ...     ats['hp']
        ... except KeyError:
        ...     'KeyError'
        'KeyError'
        """
        super(Attributes, self).__init__(Attr, self._buildAttrName)

    def _buildAttrName(self, theName):
        """
        >>> ats = Attributes()
        >>> ats._buildAttrName('new')
        'NEW'
        """
        return '{0}'.format(theName.upper())

    def addAttr(self, theAttr):
        """
        >>> ats = Attributes()
        >>> ats.addAttr(Attr('hp'))
        hp: 0/0
        >>> ats['hp'].Name
        'hp'
        >>> ats['HP'].Name
        'hp'
        """
        self[theAttr.Name] = theAttr
        return theAttr

    def setupAttrs(self, theAttrs):
        """
        >>> ats = Attributes()
        >>> ats.setupAttrs([Attr('hp'), Attr('mp')])
        >>> ats
        hp: 0/0
        mp: 0/0
        """
        for attrib in theAttrs:
            self.addAttr(attrib)

    def setupAttrsByName(self, theNames):
        """
        >>> ats = Attributes()
        >>> ats.setupAttrsByName(['hp', 'mp'])
        >>> ats
        hp: 0/0
        mp: 0/0
        """
        for name in theNames:
            self.addAttr(Attr(name))

    def setupAttrsFromJSON(self, theJsonFile):
        """
        """
        pass

    def levelUp(self, theLevel=1):
        """
        >>> ats = Attributes()
        >>> hp = Attr('hp')
        >>> hp.Base = 10
        >>> hp.Delta = 3
        >>> ats.addAttr(hp)
        hp: 10/10
        >>> mp = Attr('mp')
        >>> mp.Base = 5
        >>> mp.Delta = 2
        >>> ats.addAttr(mp)
        mp: 5/5
        >>> ats.levelUp()
        True
        >>> hp.Base
        13
        >>> mp.Base
        7
        >>> ats.levelUp(2)
        True
        >>> hp.Base
        19
        >>> mp.Base
        11
        """
        for attr in self:
            attr.levelUp(theLevel)
        return True

    def __repr__(self):
        """
        >>> ats = Attributes()
        >>> ats.addAttr(Attr('hp'))
        hp: 0/0
        >>> ats.addAttr(Attr('mp'))
        mp: 0/0
        >>> ats
        hp: 0/0
        mp: 0/0
        """
        return '\n'.join([str(attr) for attr in self])
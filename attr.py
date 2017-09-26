from itero import StrItero
import json


class Attr(object):
    """Attr Class contains all data related with a board object attribute.
    """

    def __init__(self, theName):
        """Attr class initialization method.
        """
        self._name = theName
        self._desc = None
        self._base = 0
        self._now = 0
        self._delta = 0
        self._buffs = {}

    @classmethod
    def createAttr(cls, theAttrData):
        """Create an attribute from the passed data.

        Attribute data passed is a list with this format:

            * :class:`str` with attribute name. Index is 0.

            * :class:`int` with attribute base value. Index is 1.

            * :class:`int` with attribute delta value. Index is 2

            * :class:`dict` with buff name and buff values. Index is 3.

        Last entry with  buffs can be repeated as many times as required.

        Args:
            theAttrData (:class:`list`) : Attribute parameters

        Returns:
            Attr : New attribute instance.
        """
        assert type(theAttrData) in [list, tuple]
        assert len(theAttrData) >= 3, theAttrData
        assert len(theAttrData) <= 4, theAttrData
        _attrName = theAttrData[0]
        _attrBase = theAttrData[1]
        _attrDelta = theAttrData[2]
        _attrBuff = theAttrData[3] if len(theAttrData) == 4 else None
        _attr = cls(_attrName)
        _attr.setupAttr(_attrBase, _attrDelta, _attrBuff)
        return _attr

    @property
    def Name(self):
        """Gets _name attribute value.

        >>> at = Attr('new')
        >>> at.Name
        'new'
        """
        return self._name

    @Name.setter
    def Name(self, theValue):
        """Sets _name attribute value.

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
        """Gets _desc attribute value.

        Returns:
            str : _desc attribute, or empty string if _desc is None.

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
        """Sets _desc attribute value.
        """
        self._desc = theValue

    @property
    def Base(self):
        """Gets _base attribute value.

        >>> at = Attr('old')
        >>> at.Base
        0
        """
        return self._base

    @Base.setter
    def Base(self, theValue):
        """Sets _base attribute value.

        >>> at = Attr('old')
        >>> at.Base = 10
        >>> at.Base
        10
        """
        self._base = theValue

    @property
    def Delta(self):
        """Gets _delta attribute value.

        >>> at = Attr('old')
        >>> at.Delta
        0
        """
        return self._delta

    @Delta.setter
    def Delta(self, theValue):
        """Sets _delta attribute value.

        >>> at = Attr('old')
        >>> at.Delta = 1
        >>> at.Delta
        1
        """
        self._delta = theValue

    @property
    def Buffs(self):
        """Gets _buffs attribute value.

        >>> at = Attr('old')
        >>> at.Buffs
        {}
        """
        return self._buffs

    @property
    def Now(self):
        """Gets Now value which is function of Base, Buffs and _now attributes.

        >>> at = Attr('old')
        >>> at.Base = 5
        >>> at.Now
        5
        """
        return self.Base + sum(self.Buffs.values()) + self._now

    def dec(self, theValue):
        """Decrements _now attribute a given value.

        >>> at = Attr('new')
        >>> at.Base = 10
        >>> at.dec(1)
        >>> at.Now
        9
        """
        self._now -= theValue

    def inc(self, theValue):
        """Increments _now attribute a given value.

        >>> at = Attr('new')
        >>> at.Base = 10
        >>> at.inc(2)
        >>> at.Now
        12
        """
        self._now += theValue

    def addBuff(self, theName, theValue):
        """Adds a new value to Buffs attribute.

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
        """Deletes a value from Buffs attribute.

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
        """Levels up the attribute a given number of times.

        For every level the Base value in incremented a Delta value.

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
        """Setups instance with given Base, Delta and Buffs values.

        >>> at = Attr('new')
        >>> at, at.Delta, at.Buffs
        (new: 0/0, 0, {})
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

    def setupAttrFromJSON(self, theJSON):
        """Setups instance with values from a JSON variable.

        >>> at = Attr('new')
        >>> at, at.Delta, at.Buffs
        (new: 0/0, 0, {})
        >>> data = '{"base": 10, "delta": 1, "buffs": "None"}'
        >>> at.setupAttrFromJSON(data), at.Delta, at.Buffs
        (new: 10/10, 1, {})
        >>> data = '{"base": "None", "delta": 5, "buffs": {"one": 4}}'
        >>> at.setupAttrFromJSON(data), at.Delta, at.Buffs
        (new: 14/10, 5, {'one': 4})
        """
        dicta = json.loads(theJSON)
        return self.setupAttr(int(dicta['base']) if dicta['base'] != "None" else None,
                              int(dicta['delta']) if dicta['delta'] != "None" else None,
                              dicta['buffs'] if dicta['buffs'] != 'None' else None)

    def __repr__(self):
        """Instace string representation.

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
        """Builds the name used to identify an attribute.

        >>> ats = Attributes()
        >>> ats._buildAttrName('new')
        'NEW'
        """
        return '{0}'.format(theName.upper())

    def addAttr(self, theAttr):
        """Adds a new attribute.

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
        """Adds all attributes given in the passed list.

        >>> ats = Attributes()
        >>> ats.setupAttrs([Attr('hp'), Attr('mp')])
        >>> ats
        hp: 0/0
        mp: 0/0
        """
        for attrib in theAttrs:
            self.addAttr(attrib)

    def setupAttrsByName(self, theNames):
        """Adds all attributes in the list, which provides just the
        attribute name.

        >>> ats = Attributes()
        >>> ats.setupAttrsByName(['hp', 'mp'])
        >>> ats
        hp: 0/0
        mp: 0/0
        """
        for name in theNames:
            self.addAttr(Attr(name))

    def setupAttrsFromList(self, theList):
        """Setups attributes from teh given list.

        >>> ats = Attributes()
        >>> data = [("hp", 10, 2), ("mp", 5, 1, {'one': 2})]
        >>> ats.setupAttrsFromList(data)
        >>> ats
        hp: 10/10
        mp: 7/5
        >>> ats['HP'].Delta
        2
        >>> ats['mp'].Delta
        1
        """
        for entry in theList:
            self.addAttr(Attr.createAttr(entry))

    def setupAttrsFromJSON(self, theJSON):
        """Setups attributes from the given JSON variable.

        >>> ats = Attributes()
        >>> data = '[{"hp": {"base": 10, "delta": 2, "buffs": "none"}},\
                {"mp": {"base": 5, "delta": 1, "buffs": {"one": 2}}}]'
        >>> ats.setupAttrsFromJSON(data)
        >>> ats
        hp: 10/10
        mp: 7/5
        >>> ats['HP'].Delta
        2
        >>> ats['mp'].Delta
        1
        """
        lista = json.loads(theJSON)
        for entry in lista:
            k = list(entry.keys())[0]
            v = json.dumps(list(entry.values())[0])
            self.addAttr(Attr(k)).setupAttrFromJSON(v)

    def setupAttrsFromFile(self, theFile):
        """Setups instance from teh values in the given JSON file.
        """
        with open(theFile, 'r') as file:
            data = json.load(file)
        self.setupAttrsFromJSON(json.dumps(data))

    def levelUp(self, theLevel=1):
        """Levels up all attributes stored a given number of times.

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
        """Instance string representation.

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

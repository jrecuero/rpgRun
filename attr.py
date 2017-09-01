class Attr(object):
    """Attr Class contains all data related with a board object attribute.
    """

    def __init__(self, theName):
        """Attr class initialization method.
        """
        self._name = theName
        self._base = 0
        self._delta = 0
        self._buffs = {}

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, theValue):
        self._name = theValue

    @property
    def Base(self):
        return self._base

    @Base.setter
    def Base(self, theValue):
        self._base = theValue

    @property
    def Delta(self):
        return self._delta

    @Delta.setter
    def Delta(self, theValue):
        self._delta = theValue

    @property
    def Buffs(self):
        return self._buffs

    @property
    def Now(self):
        return self.Base + sum(self.Buffs.values())

    def addBuff(self, theName, theValue):
        self._buffs.apppend({theName: theValue})

    def delBuff(self, theName):
        del self.Buffs[theName]

    def levelUp(self, theLevel=1):
        for _ in range(abs(theLevel)):
            self.Base += self.Delta * int(theLevel / abs(theLevel))

    def __repr__(self):
        return '{0}: {1}/{2}'.format(self.Name, self.Now, self.Base)


class Attributes(object):
    """Attributes Class contains all attributes related with a board object.
    """

    def __init__(self):
        """Attribute class initialization method.
        """
        self._attrs = {}

    def _buildAttrName(self, theName):
        return '{0}'.format(theName.upper())

    def getAttr(self, theName):
        attrName = self._buildAttrName(theName)
        return self._attrs[attrName]

    def addAttr(self, theAttr):
        attrName = self._buildAttrName(theAttr.Name)
        self._attrs.update({attrName: theAttr})
        setattr(self, attrName, theAttr)

    def delAttr(self, theAttr):
        attrName = self._buildAttrName(theAttr.Name)
        del self._attrs[attrName]
        delattr(self, attrName)

    def traverse(self):
        for attr in self._attrs.values():
            yield attr

    def levelUp(self, theLevel):
        for attr in self.traverse():
            attr.levelUp(theLevel)

    def __repr__(self):
        return '\n'.join([str(attr) for attr in self.traverse()])

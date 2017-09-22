from bcell import BCell
from bobject import BObject
from action import Actions
from inventory import Inventory
from equipment import Equipment


@staticmethod
def isActor():
    """Returns if the instance is an Actor.
    """
    return False


BCell.isActor = isActor


class Actor(BObject):
    """Actor Class derives from BObject class and it provides some particular
    functions for any actor placed on the board.
    """

    LIFE = None

    def __init__(self, theX, theY, theName, **kwargs):
        """Actor class initialization method.
        """
        super(Actor, self).__init__(theX, theY, theName, **kwargs)
        self.Walkable = False
        self._actions = Actions()
        self._life = None
        self._inventory = Inventory(theHost=self)
        self._equipment = Equipment(theHost=self)

    @property
    def Actions(self):
        """Gets _actions attribute value.
        """
        return self._actions

    @property
    def Life(self):
        """
        """
        if self._life is not None:
            return self.Attrs[self._life].Now
        elif Actor.LIFE is not None:
            return self.Attrs[Actor.LIFE].Now
        raise NotImplementedError

    @Life.setter
    def Life(self, theValue):
        """
        """
        self._life = theValue

    @property
    def Inventory(self):
        """Gets _inventory attribute value.
        """
        return self._inventory

    @property
    def Equipment(self):
        """Gets _equipment attribute value.
        """
        return self._equipment

    def getEquipFromInventory(self):
        """Returns all equip items from the inventory.

        Returns:
            list[GEquip] : list with all equip items.
        """
        return [x for x in self.Inventory if x.isEquip()]

    def isActor(self):
        """Returns if the instance is an Actor.
        """
        return True

    def isInBoard(self):
        """Checks if the actor is in the board.
        """
        return self.isAlive()

    def isAlive(self):
        """Checks if the actor is alive.
        """
        try:
            return self.Life > 0
        except KeyError:
            return True


def __integration_doctest():
    """
    Test Inventory can hold GItem and GEquip.
    >>> from equipment import GEquip
    >>> from gitem import GItem
    >>> from attr import Attr
    >>> a = Actor(0, 0, 'me')
    >>> it = GItem(theName='box')
    >>> sw1 = GEquip(theName='sword', theAttrBuff={'hp': 5})
    >>> sw2 = GEquip(theName='great sword')
    >>> a.Inventory.append(it)
    >>> a.Inventory.append(sw1)
    >>> a.Inventory.append(sw2)
    >>> for x in a.Inventory:
    ...     print(x.Name)
    box
    sword
    great sword

    Test when adding equipment it buffs properly.
    >>> ahp = Attr('hp')
    >>> ahp.setupAttr(theBase=100)
    hp: 100/100
    >>> a.addAttr(ahp)
    hp: 100/100
    >>> a.HP
    100
    >>> a.Equipment.append(sw1)
    >>> a.HP
    105
    >>> for x in a.Equipment:
    ...     print(x.Name)
    sword
    >>> for x in a.getEquipFromInventory():
    ...     print(x.Name)
    sword
    great sword

    Test when removing equipment it debuffs properly.
    >>> a.Equipment.remove(sw1)
    True
    >>> a.HP
    100
    """
    pass

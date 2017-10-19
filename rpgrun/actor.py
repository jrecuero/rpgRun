from rpgrun.bcell import BCell
from rpgrun.bobject import BObject
from rpgrun.action import Actions
from rpgrun.inventory import Inventory
from rpgrun.equipment import Equipment


@staticmethod
def is_actor():
    """Returns if the instance is an Actor.
    """
    return False


BCell.is_actor = is_actor


class Actor(BObject):
    """Actor Class derives from BObject class and it provides some particular
    functions for any actor placed on the board.
    """

    LIFE = None

    def __init__(self, x, y, name, **kwargs):
        """Actor class initialization method.

        Args:
            x (int) : x-coordinate position.

            y (int) : y-coordinate position.

            name (str) : String with Actor name.
        """
        super(Actor, self).__init__(x, y, name, **kwargs)
        self.walkable = False
        self.actions = Actions()
        self._life = None
        self.inventory = Inventory(host=self)
        self.equipment = Equipment(host=self)

    @property
    def all_actions(self):
        """Gets all actions actor can execute.

        Returns:
            list : List with all actions actor can execute.
        """
        actions = self.actions.stream[:]
        for eq in self.equipment:
            actions.extend(eq.actions)
        return actions

    def get_life(self):
        """Gets property for _life attribute.

        Returns:
            int : Integer with the life value.
        """
        if self._life is not None:
            return self.attrs[self._life].now
        elif Actor.LIFE is not None:
            return self.attrs[Actor.LIFE].now
        raise NotImplementedError

    def set_life(self, value):
        """Sets property for _life attribute.

        Args:
            value (int) : Integer with the new life value.
        """
        self._life = value

    def get_equipment_from_inventory(self):
        """Returns all equip items from the inventory.

        Returns:
            list[GEquip] : list with all equip items.
        """
        return [x for x in self.inventory if x.is_equip()]

    def is_actor(self):
        """Returns if the instance is an Actor.

        Returns:
            bool : True for any Actor instance. False else.

        Example:
            >>> a = Actor(0, 0, 'me')
            >>> a.is_actor()
            True
        """
        return True

    def is_in_board(self):
        """Checks if the actor is in the board.

        Returns:
            bool : True is actor is still in the board.

        Example:
            >>> from attr import Attr
            >>> a = Actor(0, 0, 'me')
            >>> ahp = Attr('hp')
            >>> ahp.setup_attr(base=100)
            hp: 100/100
            >>> Actor.LIFE = 'hp'
            >>> a.is_in_board()
            True
        """
        return self.is_alive()

    def is_alive(self):
        """Checks if the actor is alive.

        Returns:
            bool : True if Actor is alive, with life greater than zero.

        Example:
            >>> from attr import Attr
            >>> a = Actor(0, 0, 'me')
            >>> ahp = Attr('hp')
            >>> ahp.setup_attr(base=100)
            hp: 100/100
            >>> a.set_life('hp')
            >>> a.is_alive()
            True
        """
        try:
            return self.get_life() > 0
        except KeyError:
            return True


def __integration_doctest():
    """
    Test Inventory can hold GItem and GEquip.

    >>> from rpgrun.equipment import GEquip
    >>> from rpgrun.gitem import GItem
    >>> from rpgrun.attr import Attr
    >>> a = Actor(0, 0, 'me')
    >>> it = GItem(name='box')
    >>> sw1 = GEquip(name='sword', attr_buff={'hp': 5})
    >>> sw2 = GEquip(name='great sword')
    >>> a.inventory.append(it)
    >>> a.inventory.append(sw1)
    >>> a.inventory.append(sw2)
    >>> for x in a.inventory:
    ...     print(x.name)
    box
    sword
    great sword

    Test when adding equipment it buffs properly.
    >>> ahp = Attr('hp')
    >>> ahp.setup_attr(base=100)
    hp: 100/100
    >>> a.add_attr(ahp)
    hp: 100/100
    >>> a.HP
    100
    >>> a.equipment.append(sw1)
    >>> a.HP
    105
    >>> for x in a.equipment:
    ...     print(x.name)
    sword
    >>> for x in a.get_equipment_from_inventory():
    ...     print(x.name)
    sword
    great sword

    Test when removing equipment it debuffs properly.
    >>> a.equipment.remove(sw1)
    True
    >>> a.HP
    100
    >>> a.set_life('HP')
    >>> a.get_life()
    100
    >>> a.set_life('hp')
    >>> a.get_life()
    100
    >>> amp = Attr('mp')
    >>> amp.setup_attr(base=50)
    mp: 50/50
    >>> a.add_attr(amp)
    mp: 50/50
    >>> a.set_life(None)
    >>> Actor.LIFE = 'mp'
    >>> a.get_life()
    50
    """
    pass

from bcell import BCell
from bobject import BObject
# from attr import Attr


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

    def __init__(self, theX, theY, theName, **kwargs):
        """Actor class initialization method.
        """
        super(Actor, self).__init__(theX, theY, theName, **kwargs)
        self.Walkable = False
        self._actions = []

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
            return self.HP > 0
        except KeyError:
            return True

    @property
    def Actions(self):
        """Gets _actions attribute value.
        """
        return self._actions

    @Actions.setter
    def Actions(self, theValue):
        """Sets _actions attribute value. It appends the given value to
        the _actions list.
        """
        self._actions.append(theValue)

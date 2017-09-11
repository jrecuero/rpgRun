from bcell import BCell
from bobject import BObject
# from attr import Attr


@staticmethod
def isActor():
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
        """
        """
        return self.isAlive()

    def isAlive(self):
        """
        """
        try:
            return self.HP > 0
        except KeyError:
            return True

    @property
    def Actions(self):
        return self._actions

    @Actions.setter
    def Actions(self, theValue):
        self._actions.append(theValue)

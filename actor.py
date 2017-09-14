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

    LIFE = None

    def __init__(self, theX, theY, theName, **kwargs):
        """Actor class initialization method.
        """
        super(Actor, self).__init__(theX, theY, theName, **kwargs)
        self.Walkable = False
        self._actions = []
        self._life = None

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

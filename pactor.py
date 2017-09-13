from bcell import BCell
from actor import Actor


@staticmethod
def isPlayer():
    """Returns if the instance is an PActor.
    """
    return False


BCell.isPlayer = isPlayer


class PActor(Actor):
    """PActor class derived from Actor class and it provides particular
    functionality for the player actor placed on the baord.
    """

    def __init__(self, theX, theY, theName, **kwargs):
        """PActor class initialization method.
        """
        super(PActor, self).__init__(theX, theY, theName, **kwargs)
        self.Static = False

    def isPlayer(self):
        """Returns if the instance is an PActor.
        """
        return True

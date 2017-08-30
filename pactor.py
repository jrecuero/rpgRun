from bcell import BCell
from actor import Actor


@staticmethod
def isPlayer():
    return False


BCell.isPlayer = isPlayer


class PActor(Actor):
    """PActor class derived from Actor class and it provides particular
    functionality for the player actor placed on the baord.
    """

    def __init__(self, theX, theY, theName):
        """PActor class initialization method.
        """
        super(PActor, self).__init__(theX, theY, theName)
        self.Static = False

    def isPlayer(self):
        """Returns if the instance is an PActor.
        """
        return True

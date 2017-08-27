from bcell import BCell
from actor import Actor


@staticmethod
def isPlayer():
    return False


BCell.isPlayer = isPlayer


class PActor(Actor):

    def __init__(self, theX, theY, theName):
        super(PActor, self).__init__(theX, theY, theName)
        self.Static = False

    def isPlayer(self):
        return True

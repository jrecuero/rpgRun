from bcell import BCell
from bobject import BObject


@staticmethod
def isActor():
    return False


BCell.isActor = isActor


class Actor(BObject):

    def __init__(self, theX, theY, theName):
        super(Actor, self).__init__(theX, theY, theName)
        self.Walkable = False

    def isActor(self):
        return True

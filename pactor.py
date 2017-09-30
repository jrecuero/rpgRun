from bcell import BCell
from actor import Actor


@staticmethod
def is_player():
    """Returns if the instance is an PActor.
    """
    return False


BCell.is_player = is_player


class PActor(Actor):
    """PActor class derived from Actor class and it provides particular
    functionality for the player actor placed on the baord.
    """

    def __init__(self, x, y, name, **kwargs):
        """PActor class initialization method.
        """
        super(PActor, self).__init__(x, y, name, **kwargs)
        self.static = False

    def is_player(self):
        """Returns if the instance is an PActor.
        """
        return True

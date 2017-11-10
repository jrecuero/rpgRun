from rpgrun.board.bcell import BCell
from rpgrun.game.attr import Attributes


@staticmethod
def is_object():
    """Returns if the instance is a BObject.
    """
    return False


BCell.is_object = is_object


class BObject(BCell):
    """BObject class derives from BCell and it implements particular
    functionality for cells in the OBJECT layer.
    """

    def __init__(self, theX, theY, theName, **kwargs):
        """BObject class initialization method.
        """
        super(BObject, self).__init__(theX, theY, theName, **kwargs)
        self.attrs = Attributes()
        self.walkable = False

    def __getattr__(self, attr):
        """Overwrite __getattr__ method allowing to access values inside attrs
        as regular instance attributes.

        >>> from attr import Attr
        >>> obj = BObject(0, 0, 'new')
        >>> obj.add_attr(Attr('HP'))
        HP: 0/0
        >>> obj.HP
        0
        """
        if 'attrs' in self.__dict__ and attr in self.__dict__['attrs']:
            return self.attrs[attr].now
        return AttributeError

    def __setattr__(self, attr, value):
        """Overwrite __setattr__ method so values from attrs can not be
        modified as instance attributes.
        """
        if 'attrs' in self.__dict__ and attr in self.__dict__['attrs']:
            raise AttributeError
        else:
            super(BObject, self).__setattr__(attr, value)

    def add_attr(self, attr):
        """Add a new attribute to the attrs attribute.

        >>> from attr import Attr
        >>> obj = BObject(0, 0, 'new')
        >>> obj.add_attr(Attr('HP'))
        HP: 0/0
        >>> obj.attrs
        HP: 0/0
        """
        return self.attrs.add_attr(attr)

    def is_object(self):
        """Returns if the instance is a BObject.

        >>> obj = BObject(0, 0, 'new')
        >>> obj.is_object()
        True
        """
        return True

    def is_in_board(self):
        """Returns if the object is still in the board.

        >>> obj = BObject(0, 0, 'new')
        >>> obj.is_in_board()
        True
        """
        return True

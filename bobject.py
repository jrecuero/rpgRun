from bcell import BCell
from attr import Attributes


@staticmethod
def isObject():
    """Returns if the instance is a BObject.
    """
    return False


BCell.isObject = isObject


class BObject(BCell):
    """BObject class derives from BCell and it implements particular
    functionality for cells in the OBJECT layer.
    """

    def __init__(self, theX, theY, theName, **kwargs):
        """BObject class initialization method.
        """
        super(BObject, self).__init__(theX, theY, theName, **kwargs)
        self._attrs = Attributes()
        self.Walkable = False

    def __getattr__(self, theAttr):
        """Overwrite __getattr__ method allowing to access values inside _attrs
        as regular instance attributes.

        >>> from attr import Attr
        >>> obj = BObject(0, 0, 'new')
        >>> obj.addAttr(Attr('HP'))
        HP: 0/0
        >>> obj.HP
        0
        """
        if '_attrs' in self.__dict__ and theAttr in self.__dict__['_attrs']:
            return self._attrs[theAttr].Now
        raise AttributeError

    def __setattr__(self, theAttr, theValue):
        """Overwrite __setattr__ method so values from _attrs can not be
        modified as instance attributes.
        """
        if '_attrs' in self.__dict__ and theAttr in self.__dict__['_attrs']:
            raise AttributeError
        else:
            super(BObject, self).__setattr__(theAttr, theValue)

    @property
    def Attrs(self):
        """Gets _attrs attribute value.
        """
        return self._attrs

    def addAttr(self, theAttr):
        """Add a new attribute to the Attrs attribute.

        >>> from attr import Attr
        >>> obj = BObject(0, 0, 'new')
        >>> obj.addAttr(Attr('HP'))
        HP: 0/0
        >>> obj.Attrs
        HP: 0/0
        """
        return self.Attrs.addAttr(theAttr)

    def isObject(self):
        """Returns if the instance is a BObject.

        >>> obj = BObject(0, 0, 'new')
        >>> obj.isObject()
        True
        """
        return True

    def isInBoard(self):
        """Returns if the object is still in the board.

        >>> obj = BObject(0, 0, 'new')
        >>> obj.isInBoard()
        True
        """
        return True

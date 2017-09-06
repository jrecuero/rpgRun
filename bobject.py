from bcell import BCell
from attr import Attributes


@staticmethod
def isObject():
    return False


BCell.isObject = isObject


class BObject(BCell):
    """BObject class derives from BCell and it implements particular
    functionality for cells in the OBJECT layer.
    """

    def __init__(self, theX, theY, theName):
        """BObject class initialization method.
        """
        super(BObject, self).__init__(theX, theY, theName)
        self._attrs = Attributes()
        self.Walkable = False

    def __getattr__(self, theAttr):
        """Overwrite __getattr__ method allowing to access values inside _attrs
        as regular instance attributes.
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
        """
        """
        return self._attrs

    def addAttr(self, theAttr):
        """
        """
        return self.Attrs.addAttr(theAttr)

    def isObject(self):
        """Returns if the instance is a BObject.
        """
        return True
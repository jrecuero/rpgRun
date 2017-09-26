import ids
from attr import Attributes


class GObject(object):
    """GObject class implements all required data for any object used
    inside the application that is not placed in the board.
    """

    def __init__(self, **kwargs):
        """
        """
        self._name = kwargs.get('theName', None)
        self._desc = kwargs.get('theDesc', None)
        self._attrs = Attributes()
        self._id = ids.new_id()

    @property
    def Id(self):
        """Gets _id attribute value.
        """
        return self._id

    @property
    def Name(self):
        """Gets _name attribute value.

        >>> g = GObject(theName='gobj')
        >>> g.Name
        'gobj'
        """
        return self._name

    @Name.setter
    def Name(self, theValue):
        """Sets _name attribute value.

        >>> g = GObject(theName='gobj')
        >>> g.Name
        'gobj'
        >>> g.Name = 'new gobj'
        >>> g.Name
        'new gobj'
        """
        self._name = theValue

    @property
    def Desc(self):
        """Gets _desc attribute value.

        Returns:
            str: _desc attribute or empty string if _desc is None.

        >>> g = GObject(theName='gobj')
        >>> g.Desc
        ''
        >>> g = GObject(theName='gobj', theDesc="this is a gobject")
        >>> g.Desc
        'this is a gobject'
        """
        return self._desc if self._desc is not None else ''

    @Desc.setter
    def Desc(self, theValue):
        """Sets _desc attribute value.

        >>> g = GObject(theName='gobj')
        >>> g.Desc
        ''
        >>> g.Desc = 'new gobj'
        >>> g.Desc
        'new gobj'
        """
        self._desc = theValue

    def __getattr__(self, theAttr):
        """Overwrite __getattr__ method allowing to access values inside _attrs
        as regular instance attributes.

        >>> from attr import Attr
        >>> g = GObject(theName='new')
        >>> g.addAttr(Attr('HP'))
        HP: 0/0
        >>> g.HP
        0
        """
        if '_attrs' in self.__dict__ and theAttr in self.__dict__['_attrs']:
            return self._attrs[theAttr].Now
        return AttributeError

    def __setattr__(self, theAttr, theValue):
        """Overwrite __setattr__ method so values from _attrs can not be
        modified as instance attributes.
        """
        if '_attrs' in self.__dict__ and theAttr in self.__dict__['_attrs']:
            raise AttributeError
        else:
            super(GObject, self).__setattr__(theAttr, theValue)

    @property
    def Attrs(self):
        """Gets _attrs attribute value.
        """
        return self._attrs

    def addAttr(self, theAttr):
        """Add a new attribute to the Attrs attribute.

        >>> from attr import Attr
        >>> g = GObject(theName='new')
        >>> g.addAttr(Attr('HP'))
        HP: 0/0
        >>> g.Attrs
        HP: 0/0
        """
        return self.Attrs.addAttr(theAttr)

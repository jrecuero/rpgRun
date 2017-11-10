import rpgrun.common.ids as ids
from rpgrun.game.attr import Attributes


class GObject(object):
    """GObject class implements all required data for any object used
    inside the application that is not placed in the board.
    """

    def __init__(self, **kwargs):
        """
        """
        self.name = kwargs.get('name', None)
        self._desc = kwargs.get('desc', '')
        self.attrs = Attributes()
        self.__id = ids.new_id()

    @property
    def id(self):
        """Gets __id attribute value.
        """
        return self.__id

    def __getattr__(self, theAttr):
        """Overwrite __getattr__ method allowing to access values inside attrs
        as regular instance attributes.

        >>> from rpgrun.game.attr import Attr
        >>> g = GObject(name='new')
        >>> g.add_attr(Attr('HP'))
        HP: 0/0
        >>> g.HP
        0
        """
        if 'attrs' in self.__dict__ and theAttr in self.__dict__['attrs']:
            return self.attrs[theAttr].now
        return AttributeError

    def __setattr__(self, theAttr, theValue):
        """Overwrite __setattr__ method so values from attrs can not be
        modified as instance attributes.
        """
        if 'attrs' in self.__dict__ and theAttr in self.__dict__['attrs']:
            raise AttributeError
        else:
            super(GObject, self).__setattr__(theAttr, theValue)

    def add_attr(self, theAttr):
        """Add a new attribute to the attrs attribute.

        >>> from rpgrun.game.attr import Attr
        >>> g = GObject(name='new')
        >>> g.add_attr(Attr('HP'))
        HP: 0/0
        >>> g.attrs
        HP: 0/0
        """
        return self.attrs.add_attr(theAttr)

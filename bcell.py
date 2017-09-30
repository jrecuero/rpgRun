import ids
from enum import Enum
from bpoint import BPoint


class BRender(Enum):
    """BRender class-enumeration keeps all possible render possibilities.
    """

    NONE = 0
    TEXT = 1
    GRAPH = 2
    DEFAULT = 1


class BSprite(object):
    """BSprite class contains a sprite to be renderer on the display.
    """

    def __init__(self, **kwargs):
        """BSprite class initialization method.

        Keyword Args:
            spr_graph (object) : sprite instance for graphical rendering.

            spr_text (str) : string to be used for text rendering.

            color (str) : string with the color for text rendering.

            width (int) : width size for text rendering.
        """
        self.graph = kwargs.get('spr_graph', None)
        self.text = kwargs.get('spr_text', None)
        self.color = kwargs.get('color', None)
        self.width = kwargs.get('width', None)

    def get(self, brender=BRender.DEFAULT):
        """Gets the sprite to render based on the render type.

        >>> sp = BSprite(spr_text='*')
        >>> sp.get(BRender.NONE)
        >>> sp.get(BRender.GRAPH)
        >>> sp.get(BRender.TEXT)
        '*'
        >>> sp = BSprite(spr_graph=True)
        >>> sp.get(BRender.NONE)
        >>> sp.get(BRender.GRAPH)
        True
        >>> sp.get(BRender.TEXT)
        """
        if brender == BRender.GRAPH:
            return self.graph
        elif brender == BRender.TEXT:
            return self.text
        elif brender == BRender.NONE:
            return None
        else:
            raise NotImplementedError

    def render(self, brender=BRender.DEFAULT):
        """Renders the sprite for the given render type.
        """
        if brender == BRender.GRAPH:
            raise NotImplementedError
        elif brender == BRender.TEXT:
            return '{0}{1}{2}'.format(self.color if self.color else '',
                                      self.text.center(self.width) if self.width else self.text,
                                      '\x1b[0m' if self.color else '')
            return self.text
        elif brender == BRender.NONE:
            raise NotImplementedError
        else:
            raise NotImplementedError

    def __repr__(self):
        """Returns the BSprite instance as a string.
        """
        st = 'Text[{0}] '.format(self.text if self.text else 'None')
        st += 'Graph[{0}]'.format('<GRAPH>' if self.graph else 'None')
        return st


class BCell(BPoint):
    """BCell class derives from BPoint class and it provides some additional
    functionality for any object placed on the board.
    """

    def __init__(self, x, y, name, **kwargs):
        """BCell class initialization method.

        >>> cell = BCell(0, 0, 'cell')
        >>> cell.sprite
        >>> cell = BCell(0, 0, 'cell', sprite='*')
        >>> cell.sprite
        Text[*] Graph[None]
        >>> cell = BCell(0, 0, 'cell', sprite=BSprite(spr_text='*'))
        >>> cell.sprite
        Text[*] Graph[None]
        >>> cell = BCell(0, 0, 'cell', sprite=BSprite(spr_graph=True))
        >>> cell.sprite
        Text[None] Graph[<GRAPH>]
        >>> cell = BCell(0, 0, 'cell', sprite=BSprite(spr_graph=True, spr_text='*'))
        >>> cell.sprite
        Text[*] Graph[<GRAPH>]
        """
        super(BCell, self).__init__(x, y)
        self.__id = ids.new_id()
        self.name = name
        self.desc = kwargs.get('desc', '')
        self.static = True
        self.walkable = True
        self.solid = True
        self.layer = None
        self.sprite = None
        self.set_sprite(kwargs.get('sprite', None))

    @property
    def id(self):
        """Gets __id attribute value.
        """
        return self.__id

    @property
    def row(self):
        """Gets _y attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.row
        2
        """
        return self.y

    @property
    def col(self):
        """Gets _x attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.col
        1
        """
        return self.x

    @property
    def klass(self):
        """
        >>> cell = BCell(0, 0, 'cell')
        >>> cell.klass
        <class 'bpoint.BPoint'>
        """
        return BPoint

    def set_sprite(self, value):
        """Sets sprite attribute value.

        It the value given is not a BSprite instance, but a string, it creates
        a text BSprite using the given value as the string.

        Args:
            value (:class:`str` or :class:`BSprite`) : New sprite to set

        Example:
            >>> cell = BCell(0, 0, 'cell', sprite='*')
            >>> cell.sprite
            Text[*] Graph[None]
            >>> cell = BCell(0, 0, 'cell')
            >>> cell.sprite
            >>> cell.set_sprite('*')
            >>> cell.sprite
            Text[*] Graph[None]
            >>> cell.set_sprite(BSprite(spr_graph=True))
            >>> cell.sprite
            Text[None] Graph[<GRAPH>]
            >>> cell.set_sprite(BSprite(spr_graph=True, spr_text='*'))
            >>> cell.sprite
            Text[*] Graph[<GRAPH>]
        """
        self.sprite = BSprite(spr_text=value) if isinstance(value, str) else value

    def get_point(self):
        """Gets a point instance to be used on mathematical operations.

        >>> cell = BCell(0, 0, 'cell')
        >>> cell.get_point()
        (0, 0)
        """
        return self.klass(self.x, self.y)

    def __eq__(self, other):
        """Overload method for the 'equal to' operation between BCell
        instances.

        Two BCell instances are equal if x and Y coordinates values are
        equal and name is the same.

        Args:
            other (BCell) : the other BCell instance to check if is equal.

        Returns:
            boolean : True if BCell instaces are equal, False else.

        >>> BCell(1, 1, "A") == BCell(1, 1, "A")
        True
        >>> BCell(1, 1, "A") == BCell(1, 0, "A")
        False
        >>> BCell(1, 1, "A") == BCell(0, 1, "A")
        False
        >>> BCell(1, 1, "A") in [BCell(0, 0, "A"), BCell(0, 1, "A"), BCell(1, 1, "A")]
        True
        >>> BCell(1, 0, "A") in [BCell(0, 0, "A"), BCell(0, 1, "A"), BCell(1, 1, "A")]
        False
        >>> BCell(1, 1, "A") == BCell(1, 1, "B")
        False
        >>> BCell(0, 0, "A") in [BCell(0, 0, "B"), BCell(0, 1, "A"), BCell(1, 1, "A")]
        False
        """
        if isinstance(other, BCell):
            return super(BCell, self).__eq__(other) and self.name == other.name
        return NotImplemented

    def render(self, brender=BRender.DEFAULT):
        """Render the cell.

        >>> cell = BCell(0, 0, 'cell', sprite=BSprite(spr_graph=True, spr_text='*'))
        >>> cell.render()
        '*'
        >>> cell.render(BRender.TEXT)
        '*'
        """
        return self.sprite.render(brender)

    def __repr__(self):
        """String representation for the BCell instance.

        Returns:
            str : string with the BCell instance representation.

        >>> str(BCell(0, 0, 'cell'))
        '(0, 0) : cell'
        """
        return '{0} : {1}'.format(super(BCell, self).__repr__(), self.name)

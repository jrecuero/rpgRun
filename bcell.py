import ids
from bpoint import BPoint
from brender import BRender
from bsprite import BSprite


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

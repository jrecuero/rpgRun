import itertools
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
        """
        self._graph = kwargs.get('theSprGraph', None)
        self._text = kwargs.get('theSprText', None)
        self._color = kwargs.get('theColor', None)
        self._width = kwargs.get('theWidth', None)

    @property
    def Graph(self):
        """Gets _graph attribute value.
        """
        return self._graph

    @Graph.setter
    def Graph(self, theValue):
        """Sets _graph attribute value.
        """
        self._graph = theValue

    @property
    def Text(self):
        """Gets _text attribute value.
        """
        return self._text

    @Text.setter
    def Text(self, theValue):
        """Sets _text attribute value.
        """
        self._text = theValue

    @property
    def Color(self):
        """Gets _color attribute value.
        """
        return self._color

    @Color.setter
    def Color(self, theValue):
        """Sets _color attribute value.
        """
        self._color = theValue

    @property
    def Width(self):
        """Get _width attribute value.
        """
        return self._width

    @Width.setter
    def Width(self, theValue):
        """Set _width attribute value.
        """
        self._width = theValue

    def get(self, theRender=BRender.DEFAULT):
        """Gets the sprite to render based on the render type.
        """
        if theRender == BRender.GRAPH:
            return self._graph
        elif theRender == BRender.TEXT:
            return self._text
        elif theRender == BRender.NONE:
            return None
        else:
            raise NotImplementedError

    def render(self, theRender=BRender.DEFAULT):
        """Renders the sprite for the given render type.
        """
        if theRender == BRender.GRAPH:
            raise NotImplementedError
        elif theRender == BRender.TEXT:
            return '{0}{1}{2}'.format(self.Color if self.Color else '',
                                      self._text.center(self.Width) if self.Width else self._text,
                                      '\x1b[0m' if self.Color else '')
            return self._text
        elif theRender == BRender.NONE:
            raise NotImplementedError
        else:
            raise NotImplementedError

    def __repr__(self):
        """Returns the BSprite instance as a string.
        """
        st = 'Text[{0}] '.format(self._text if self._text else 'None')
        st += 'Graph[{0}]'.format('<GRAPH>' if self._graph else 'None')
        return st


class BCell(BPoint):
    """BCell class derives from BPoint class and it provides some additional
    functionality for any object placed on the board.
    """

    __newId = itertools.count(1)

    def __init__(self, theX, theY, theName, **kwargs):
        """BCell class initialization method.

        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Sprite
        >>> cell = BCell(0, 0, 'cell', theSprite='*')
        >>> cell.Sprite
        Text[*] Graph[None]
        >>> cell = BCell(0, 0, 'cell', theSprite=BSprite(theSprText='*'))
        >>> cell.Sprite
        Text[*] Graph[None]
        >>> cell = BCell(0, 0, 'cell', theSprite=BSprite(theSprGraph=True))
        >>> cell.Sprite
        Text[None] Graph[<GRAPH>]
        >>> cell = BCell(0, 0, 'cell', theSprite=BSprite(theSprGraph=True, theSprText='*'))
        >>> cell.Sprite
        Text[*] Graph[<GRAPH>]
        """
        super(BCell, self).__init__(theX, theY)
        self._id = next(BCell.__newId)
        self._name = theName
        self._desc = None
        self._static = True
        self._walkable = True
        self._solid = True
        self._layer = None
        self.Sprite = kwargs.get('theSprite', None)

    @property
    def Id(self):
        """Gets _id attribute value.
        """
        return self._id

    @property
    def Name(self):
        """Gets _name attribute value.
        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Name
        'cell'
        """
        return self._name

    @property
    def Desc(self):
        """Gets _desc attribute value.

        Returns:
            str: _desc attribute or empty string if _desc is None.

        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Desc
        ''
        >>> cell.Desc = 'new cell'
        >>> cell.Desc
        'new cell'
        """
        return self._desc if self._desc is not None else ''

    @Desc.setter
    def Desc(self, theValue):
        """Sets _desc attribute value.
        """
        self._desc = theValue

    @Name.setter
    def Name(self, theValue):
        """Sets _name attribute value.

        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Name
        'cell'
        >>> cell.Name = 'new cell'
        >>> cell.Name
        'new cell'
        """
        self._name = theValue

    @property
    def Row(self):
        """Gets _y attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Row
        2
        """
        return self.Y

    @property
    def Col(self):
        """Gets _x attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Col
        1
        """
        return self.X

    @property
    def Static(self):
        """Gets _static attribute value.
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Static
        True
        """
        return self._static

    @Static.setter
    def Static(self, theValue):
        """Sets _static attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Static
        True
        >>> cell.Static = False
        >>> cell.Static
        False
        """
        self._static = theValue

    @property
    def Walkable(self):
        """Gets _walkable attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Walkable
        True
        """
        return self._walkable

    @Walkable.setter
    def Walkable(self, theValue):
        """Sets _walkable attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Walkable
        True
        >>> cell.Walkable = False
        >>> cell.Walkable
        False
        """
        self._walkable = theValue

    @property
    def Solid(self):
        """Gets _solid attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Solid
        True
        """
        return self._solid

    @Solid.setter
    def Solid(self, theValue):
        """Set _solid attribute value.

        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Solid
        True
        >>> cell.Solid = False
        >>> cell.Solid
        False
        """
        self._solid = theValue

    @property
    def Sprite(self):
        """Gets _sprite attribute value.

        >>> cell = BCell(0, 0, 'cell', theSprite='*')
        >>> cell.Sprite
        Text[*] Graph[None]
        """
        return self._sprite

    @Sprite.setter
    def Sprite(self, theValue):
        """Sets _sprite attribute value.

        It the value given is not a BSprite instance, but a string, it creates
        a text BSprite using the given value as the string.

        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Sprite
        >>> cell.Sprite = '*'
        Text[*] Graph[None]
        >>> cell.Sprite = BSprite(theSprGraph=True)
        Text[None] Graph[<GRAPH>]
        >>> cell.Sprite = BSprite(theSprGraph=True, theSprText='*')
        Text[*] Graph[<GRAPH>]
        """
        self._sprite = BSprite(theSprText=theValue) if isinstance(theValue, str) else theValue

    @property
    def Layer(self):
        """Gets _layer attribute value.

        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Layer
        >>> cell.Layer = True
        >>> cell.Layer
        True
        """
        return self._layer

    @Layer.setter
    def Layer(self, theValue):
        """Sets _layer attribute value.
        """
        self._layer = theValue

    def render(self, theRender=BRender.DEFAULT):
        """Render the cell.

        >>> cell = BCell(0, 0, 'cell', theSprite=BSprite(theSprGraph=True, theSprText='*'))
        >>> cell.render()
        '*'
        >>> cell.render(BRender.TEXT)
        '*'
        """
        return self.Sprite.render(theRender)

    def __repr__(self):
        """String representation for the BCell instance.

        Returns:
            str : string with the BCell instance representation.

        >>> str(BCell(0, 0, 'cell'))
        '(0, 0) : cell'
        """
        return '{0} : {1}'.format(super(BCell, self).__repr__(), self.Name)

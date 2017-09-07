import itertools
from enum import Enum
from bpoint import BPoint


class BRender(Enum):

    NONE = 0
    TEXT = 1
    GRAPH = 2
    DEFAULT = 1


class BSprite(object):

    def __init__(self, **kwargs):
        self._graph = kwargs.get('theSprGraph', None)
        self._text = kwargs.get('theSprText', None)

    @property
    def Graph(self):
        return self._graph

    @Graph.setter
    def Graph(self, theValue):
        self._graph = theValue

    @property
    def Text(self):
        return self._text

    @Text.setter
    def Text(self, theValue):
        self._text = theValue

    def get(self, theRender=BRender.DEFAULT):
        if theRender == BRender.GRAPH:
            return self._graph
        elif theRender == BRender.TEXT:
            return self._text
        elif theRender == BRender.NONE:
            return None
        else:
            raise NotImplementedError

    def __repr__(self):
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
        self.Sprite = kwargs.get('theSprite', None)

    @property
    def Id(self):
        """
        """
        return self._id

    @property
    def Name(self):
        """
        >>> cell = BCell(0, 0, 'cell')
        >>> cell.Name
        'cell'
        """
        return self._name

    @property
    def Desc(self):
        """
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
        """
        """
        self._desc = theValue

    @Name.setter
    def Name(self, theValue):
        """
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
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Row
        2
        """
        return self.Y

    @property
    def Col(self):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Col
        1
        """
        return self.X

    @property
    def Static(self):
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Static
        True
        """
        return self._static

    @Static.setter
    def Static(self, theValue):
        """
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
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Walkable
        True
        """
        return self._walkable

    @Walkable.setter
    def Walkable(self, theValue):
        """
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
        """
        >>> cell = BCell(1, 2, 'cell')
        >>> cell.Solid
        True
        """
        return self._solid

    @Solid.setter
    def Solid(self, theValue):
        """
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
        """
        >>> cell = BCell(0, 0, 'cell', theSprite='*')
        >>> cell.Sprite
        Text[*] Graph[None]
        """
        return self._sprite

    @Sprite.setter
    def Sprite(self, theValue):
        """
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

    def render(self, theRender=BRender.DEFAULT):
        """Render the cell.

        >>> cell = BCell(0, 0, 'cell', theSprite=BSprite(theSprGraph=True, theSprText='*'))
        >>> cell.render()
        '*'
        >>> cell.render(BRender.TEXT)
        '*'
        >>> cell.render(BRender.GRAPH)
        True
        """
        return self.Sprite.get(theRender)

    def __repr__(self):
        """String representation for the BCell instance.

        Returns:
            str : string with the BCell instance representation.

        >>> str(BCell(0, 0, 'cell'))
        '(0, 0) : cell'
        """
        return '{0} : {1}'.format(super(BCell, self).__repr__(), self.Name)

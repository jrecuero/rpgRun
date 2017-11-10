from rpgrun.board.brender import BRender


class BSprite(object):
    """BSprite class contains a sprite to be renderer on the display.
    """

    def __init__(self, **kwargs):
        """BSprite class initialization method.

        Keyword Args:
            sprite (object) : sprite instance for rendering.
        """
        self.sprite = kwargs.get('sprite', None)
        self._selected = False
        self.enabled = True
        self.hidden = False

    @property
    def selected(self):
        """Gets attribute _selected value.

        Returns:
            bool : Value for _selected attribute.

        Example:
            >>> sp = BSprite(sprite=True)
            >>> sp.selected
            False
            >>> sp.selected = True
            >>> sp.selected
            True
        """
        return self._selected

    @selected.setter
    def selected(self, value):
        """Sets attribute _selected value. It sets the same attribute for the
        graph instance.

        Args:
            value (bool) : New value for _selected attribute.
        """
        self._selected = value

    def get(self, brender=BRender.DEFAULT):
        """Gets the sprite to render based on the render type.
        """
        raise NotImplementedError

    def render(self, brender=BRender.DEFAULT):
        """Renders the sprite for the given render type.
        """
        raise NotImplementedError

    def __repr__(self):
        """Returns the BSprite instance as a string.
        """
        raise NotImplementedError


class TextSprite(BSprite):
    """TextSprite class contains a sprite to be renderer on the display.
    """

    def __init__(self, **kwargs):
        """TextSprite class initialization method.

        Keyword Args:
            color (str) : string with the color for text rendering.
            width (int) : width size for text rendering.
        """
        super(TextSprite, self).__init__(**kwargs)
        self.color = kwargs.get('color', None)
        self.width = kwargs.get('width', None)

    def get(self, brender=BRender.DEFAULT):
        """Gets the sprite to render based on the render type.

        Example:
            >>> sp = TextSprite(sprite='*')
            >>> sp.get(BRender.NONE)
            >>> sp.get(BRender.GRAPH)
            >>> sp.get(BRender.TEXT)
            '*'
        """
        if not self.enabled or self.hidden or brender is not BRender.TEXT:
            return None
        return self.sprite

    def render(self, brender=BRender.DEFAULT):
        """Renders the sprite for the given render type.
        """
        if not self.enabled or self.hidden or brender is not BRender.TEXT:
            return None
        return '{0}{1}{2}'.format(self.color if self.color else '',
                                  self.sprite.center(self.width) if self.width else self.sprite,
                                  '\x1b[0m' if self.color else '')

    def __repr__(self):
        """Returns the BSprite instance as a string.
        """
        return '<TEXT> {0}'.format(self.sprite)


class GraphSprite(BSprite):

    def __init__(self, **kwargs):
        """BSprite class initialization method.
        """
        super(GraphSprite, self).__init__(**kwargs)

    @BSprite.selected.setter
    def selected(self, value):
        """Sets attribute _selected value. It sets the same attribute for the
        graph instance.

        Args:
            value (bool) : New value for _selected attribute.
        """
        BSprite.selected.fset(self, value)
        if hasattr(self.sprite, 'selected'):
            self.sprite.selected = value

    def get(self, brender=BRender.DEFAULT):
        """Gets the sprite to render based on the render type.

        Example:
            >>> sp = GraphSprite(sprite=True)
            >>> sp.get(BRender.NONE)
            >>> sp.get(BRender.GRAPH)
            True
            >>> sp.get(BRender.TEXT)
        """
        if not self.enabled or self.hidden or brender is not BRender.GRAPH:
            return None
        return self.sprite

    def render(self, brender=BRender.DEFAULT):
        """Renders the sprite for the given render type.
        """
        if not self.enabled or self.hidden or brender is not BRender.GRAPH:
            return None
        return self.sprite

    def __repr__(self):
        """Returns the BSprite instance as a string.
        """
        return '<GRAPH> {0}'.format(self.sprite)

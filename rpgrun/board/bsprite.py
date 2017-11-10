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
        self._enabled = True
        self._hidden = False
        self._in_focus = True

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

    @property
    def enabled(self):
        """Gets attribute _enabled value.

        Returns:
            bool : Value for _enabled attribute.

        Example:
            >>> sp = BSprite(sprite=True)
            >>> sp.enabled
            True
            >>> sp.enabled = False
            >>> sp.enabled
            False
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """Sets attribute _enabled value. It sets the same attribute for the
        graph instance.

        Args:
            value (bool) : New value for _enabled attribute.
        """
        self._enabled = value

    @property
    def hidden(self):
        """Gets attribute _hidden value.

        Returns:
            bool : Value for _hidden attribute.

        Example:
            >>> sp = BSprite(sprite=True)
            >>> sp.hidden
            False
            >>> sp.hidden = True
            >>> sp.hidden
            True
        """
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        """Sets attribute _hidden value. It sets the same attribute for the
        graph instance.

        Args:
            value (bool) : New value for _hidden attribute.
        """
        self._hidden = value

    @property
    def in_focus(self):
        """Gets attribute _in_focus value.

        Returns:
            bool : Value for _in_focus attribute.

        Example:
            >>> sp = BSprite(sprite=True)
            >>> sp.in_focus
            True
            >>> sp.in_focus = False
            >>> sp.in_focus
            False
        """
        return self._in_focus

    @in_focus.setter
    def in_focus(self, value):
        """Sets attribute _in_focus value. It sets the same attribute for the
        graph instance.

        Args:
            value (bool) : New value for _in_focus attribute.
        """
        self._in_focus = value

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

    @BSprite.enabled.setter
    def enabled(self, value):
        """Sets attribute _enabled value. It sets the same attribute for the
        graph instance.

        Args:
            value (bool) : New value for _enabled attribute.
        """
        BSprite.enabled.fset(self, value)
        if hasattr(self.sprite, 'enabled'):
            self.sprite.enabled = value

    @BSprite.hidden.setter
    def hidden(self, value):
        """Sets attribute _hidden value. It sets the same attribute for the
        graph instance.

        Args:
            value (bool) : New value for _hidden attribute.
        """
        BSprite.hidden.fset(self, value)
        if hasattr(self.sprite, 'hidden'):
            self.sprite.hidden = value

    @BSprite.in_focus.setter
    def in_focus(self, value):
        """Sets attribute _in_focus value. It sets the same attribute for the
        graph instance.

        Args:
            value (bool) : New value for _in_focus attribute.
        """
        BSprite.in_focus.fset(self, value)
        if hasattr(self.sprite, 'in_focus'):
            self.sprite.in_focus = value

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

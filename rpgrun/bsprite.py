from rpgrun.brender import BRender


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
        self._selected = False

    @property
    def selected(self):
        """Gets attribute _selected value.

        Returns:
            bool : Value for _selected attribute.

        Example:
            >>> sp = BSprite(spr_graph=True)
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
        if self.graph and hasattr(self.graph, 'selected'):
            self.graph.selected = value

    def get(self, brender=BRender.DEFAULT):
        """Gets the sprite to render based on the render type.

        Example:
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
        if brender is BRender.GRAPH:
            return self.graph
        elif brender is BRender.TEXT:
            return '{0}{1}{2}'.format(self.color if self.color else '',
                                      self.text.center(self.width) if self.width else self.text,
                                      '\x1b[0m' if self.color else '')
            return self.text
        elif brender is BRender.NONE:
            raise NotImplementedError
        else:
            raise NotImplementedError

    def __repr__(self):
        """Returns the BSprite instance as a string.
        """
        st = 'Text[{0}] '.format(self.text if self.text else 'None')
        st += 'Graph[{0}]'.format('<GRAPH>' if self.graph else 'None')
        return st

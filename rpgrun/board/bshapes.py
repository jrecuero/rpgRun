import abc
from rpgrun.board.bpoint import BPoint


class Shape(abc.ABC):
    """Shape class is an abstract class that provides an interface to be
    implemented for any concrete shape class.
    """

    def __init__(self, center, width, height):
        """Shape class initialization method.

        Args:
            center (BPoint) : Point to the center of shape.
            width (int) : Shape width dimension (x-axis).
            height (int) : Shape height dimension (y-axis).
        """
        self._center = center
        self._width = width
        self._height = height

    @property
    def center(self):
        """Gets _center attribute value.
        """
        return self._center

    @center.setter
    def center(self, value):
        """Sets _center attribute value.
        """
        if isinstance(value, BPoint):
            self._center = value
        else:
            raise NotImplementedError

    @property
    def width(self):
        """Gets _width attribute value.
        """
        return self._width

    @width.setter
    def width(self, value):
        """Set _width attribute value.
        """
        self._width = value

    @property
    def height(self):
        """Gets _height attribute value.
        """
        return self._height

    @height.setter
    def height(self, value):
        """Set _height attribute value.
        """
        self._height = value

    @abc.abstractmethod
    def get_corners(other):
        """Gets all shape corners.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_rects(self):
        """Get a rectangle corners that contains the shape.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def is_inside(self, other):
        """Checks if the given point is inside the shape.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_all_points_inside(self):
        """Returns all points contained in the shape.
        """
        raise NotImplementedError


class Quad(Shape):
    """Quad class derived from Shape class and implements a Square or
    Rectangle shape.
    """

    def __init__(self, center, width, height):
        """Quad class initialization method.

        Args:
            center (BPoint) : Point to the center of quad.
            width (int) : Quad width dimension (x-axis).
            height (int) : Quad height dimension (y-axis).

        >>> q = Quad(BPoint(0, 0), 10, 10)
        >>> q.center, q.width, q.height
        ((0, 0), 10, 10)
        >>> q.center = BPoint(1, 1)
        >>> q.center
        (1, 1)
        >>> q.width = 20
        >>> q.height = 15
        >>> q.width, q.height
        (20, 15)
        """
        super(Quad, self).__init__(center, width, height)

    def get_corners(self):
        """Gets all shape corners.

        >>> q = Quad(BPoint(10, 10), 10, 10)
        >>> q.get_corners()
        ((5, 15), (15, 15), (5, 5), (15, 5))
        """
        top_left = self.center.xy_translate(-self.width / 2, self.height / 2)
        top_right = self.center.xy_translate(self.width / 2, self.height / 2)
        botton_left = self.center.xy_translate(-self.width / 2, -self.height / 2)
        bottom_right = self.center.xy_translate(self.width / 2, -self.height / 2)
        return (top_left, top_right, botton_left, bottom_right)

    def get_rects(self):
        """Get a rectangle corners that contains the shape.

        >>> q = Quad(BPoint(10, 10), 10, 10)
        >>> q.get_rects()
        [((5, 15), (15, 15), (5, 5), (15, 5))]
        """
        return [self.get_corners(), ]

    def is_inside(self, other):
        """Checks if the given point is inside the shape.

        >>> q = Quad(BPoint(10, 10), 4, 4)
        >>> q.is_inside(BPoint(11, 11)), q.is_inside(BPoint(9, 9))
        (True, True)
        >>> q.is_inside(BPoint(13, 11)), q.is_inside(BPoint(10, 5))
        (False, False)
        """
        top_left, top_right, botton_left, bottom_right = self.get_corners()
        return (top_left.x <= other.x <= top_right.x) and\
               (bottom_right.y <= other.y <= top_right.y)

    def get_all_points_inside(self):
        """Returns all points contained in the shape.

        >>> q = Quad(BPoint(10, 10), 2, 2)
        >>> q.get_all_points_inside()
        [(9, 9), (9, 10), (9, 11), (10, 9), (10, 10), (10, 11), (11, 9), (11, 10), (11, 11)]
        """
        all_points = []
        top_left, top_right, botton_left, bottom_right = self.get_corners()
        for x in range(top_left.x, top_right.x + 1):
            for y in range(bottom_right.y, top_right.y + 1):
                all_points.append(BPoint(x, y))
        return all_points


class Rectangle(Quad):
    """Rectanle class derived from Quad class, it is basically a Quad
    but the hook point is not the center, but the bottom-left corner.
    """

    def __init__(self, corner, width, height):
        """Rectangle class initialization method.

        Args:
            corner (BPoint) : Point to the bottom-left of the rectangle..
            width (int) : Rectangle width dimension (x-axis).
            height (int) : Rectangle height dimension (y-axis).

        >>> q = Rectangle(BPoint(0, 0), 2, 2)
        >>> q.center, q.width, q.height
        ((1, 1), 2, 2)
        >>> q.get_corners()
        ((0, 2), (2, 2), (0, 0), (2, 0))
        >>> q.get_rects()
        [((0, 2), (2, 2), (0, 0), (2, 0))]
        >>> q.is_inside(BPoint(3, 3)), q.is_inside(BPoint(1, 1))
        (False, True)
        >>> q.get_all_points_inside()
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        """
        center = BPoint(corner.x + int(width / 2), corner.y + int(height / 2))
        super(Rectangle, self).__init__(center, width, height)

    @Quad.center.setter
    def center(self, value):
        """Sets _center attribute value. Rectangle can not update center.

        >>> q = Rectangle(BPoint(0, 0), 2, 2)
        >>> try:
        ...     q.center = BPoint(1, 1)
        ... except NotImplementedError:
        ...     'NotImplemented'
        'NotImplemented'
        """
        raise NotImplementedError

    @Quad.width.setter
    def width(self, value):
        """Sets _width attribute value. Rectangle can not update width.
        >>> try:
        ...     q.width = 20
        ... except NotImplementedError:
        ...     'NotImplemented'
        'NotImplemented'
        """
        raise NotImplementedError

    @Quad.height.setter
    def height(self, value):
        """Sets _height attribute value. Rectangle can not update height.
        >>> try:
        ...     q.height = 15
        ... except NotImplementedError:
        ...     'NotImplemented'
        'NotImplemented'
        """
        raise NotImplementedError


class Rhomboid(Shape):
    """Rhomboid class derives from Shape class and it implements a
    Rhomboid shape.
    """

    def __init__(self, center, width, height):
        """Rhomboid class initialization method.

        Args:
            center (BPoint) : Point to the center of rombhoid.
            width (int) : Rombhoid width dimension (x-axis).
            height (int) : Rombhoid height dimension (y-axis).

        >>> r = Rhomboid(BPoint(0, 0), 10, 10)
        >>> r.center, r.width, r.height
        ((0, 0), 10, 10)
        >>> r.center = BPoint(1, 1)
        >>> r.center
        (1, 1)
        """
        if width == height:
            super(Rhomboid, self).__init__(center, width, height)
        else:
            raise NotImplementedError

    @Shape.width.setter
    def width(self, value):
        """Set _width attribute value. Rhomboid have same width and height

        >>> r = Rhomboid(BPoint(0, 0), 10, 10)
        >>> r.width, r.height
        (10, 10)
        >>> r.width = 20
        >>> r.width, r.height
        (20, 20)
        """
        self._width = value
        self._height = value

    @Shape.height.setter
    def height(self, value):
        """Set _height attribute value. Rhomboid have same width and height

        >>> r = Rhomboid(BPoint(0, 0), 10, 10)
        >>> r.width, r.height
        (10, 10)
        >>> r.height = 15
        >>> r.width, r.height
        (15, 15)
        """
        self._height = value
        self._width = value

    def get_corners(self):
        """Gets all shape corners.

        >>> r = Rhomboid(BPoint(10, 10), 4, 4)
        >>> r.get_corners()
        ((10, 12), (10, 8), (8, 10), (12, 10))
        """
        top = self.center.y_translate(self.height / 2)
        bottom = self.center.y_translate(-self.height / 2)
        left = self.center.x_translate(-self.width / 2)
        right = self.center.x_translate(self.width / 2)
        return (top, bottom, left, right)

    def get_rects(self):
        """Get a rectangle corners that contains the shape.

        >>> r = Rhomboid(BPoint(10, 10), 10, 10)
        >>> r.get_rects()
        [((5, 15), (15, 15), (5, 5), (15, 5))]
        """
        top_left = self.center.xy_translate(-self.width / 2, self.height / 2)
        top_right = self.center.xy_translate(self.width / 2, self.height / 2)
        botton_left = self.center.xy_translate(-self.width / 2, -self.height / 2)
        bottom_right = self.center.xy_translate(self.width / 2, -self.height / 2)
        return [(top_left, top_right, botton_left, bottom_right), ]

    def is_inside(self, other):
        """Checks if the given point is inside the shape.

        >>> r = Rhomboid(BPoint(5, 5), 6, 6)
        >>> r.is_inside(BPoint(6, 5)), r.is_inside(BPoint(6, 6)), r.is_inside(BPoint(6, 7)), r.is_inside(BPoint(6, 8))
        (True, True, True, False)
        >>> r.is_inside(BPoint(7, 5)), r.is_inside(BPoint(7, 6)), r.is_inside(BPoint(7, 7)), r.is_inside(BPoint(7, 8))
        (True, True, False, False)
        >>> r.is_inside(BPoint(8, 5)), r.is_inside(BPoint(8, 6)), r.is_inside(BPoint(8, 7)), r.is_inside(BPoint(8, 8))
        (True, False, False, False)
        >>> r.is_inside(BPoint(6, 4)), r.is_inside(BPoint(6, 3)), r.is_inside(BPoint(6, 2))
        (True, True, False)
        >>> r.is_inside(BPoint(7, 4)), r.is_inside(BPoint(7, 3)), r.is_inside(BPoint(7, 2))
        (True, False, False)
        >>> r.is_inside(BPoint(4, 5)), r.is_inside(BPoint(4, 6)), r.is_inside(BPoint(4, 7)), r.is_inside(BPoint(4, 8))
        (True, True, True, False)
        >>> r.is_inside(BPoint(3, 5)), r.is_inside(BPoint(3, 6)), r.is_inside(BPoint(3, 7)), r.is_inside(BPoint(3, 8))
        (True, True, False, False)
        """
        top, bottom, left, right = self.get_corners()
        if other in [top, bottom, left, right]:
            return True
        else:
            half_width = int(self.width / 2)
            half_height = int(self.height / 2)
            p = other.xy_translate(-self.center.x, -self.center.y)
            return (abs(p.x) < half_width) and (abs(p.y) < half_height) and\
                   (abs(p.y) <= (half_width - abs(p.x)))

    def get_all_points_inside(self):
        """Returns all points contained in the shape.

        >>> r = Rhomboid(BPoint(10, 10), 4, 4)
        >>> r.get_all_points_inside()
        [(8, 10), (9, 9), (9, 10), (9, 11), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (11, 9), (11, 10), (11, 11), (12, 10)]
        """
        all_points = []
        top_left, top_right, botton_left, bottom_right = self.get_rects()[0]
        for x in range(top_left.x, top_right.x + 1):
            for y in range(bottom_right.y, top_right.y + 1):
                bp = BPoint(x, y)
                if self.is_inside(bp):
                    all_points.append(bp)
        return all_points


class Star(Rhomboid):
    """Star class derives from Rhomboid class and it implements a Star shape.

    A start shape only have point in the along the center X-coordinate and the
    center Y-coordinate.
    """

    def __init__(self, center, width, height):
        """Star class initialization method.

        Args:
            center (BPoint) : Point to the center of star.
            width (int) : Star width dimension (x-axis).
            height (int) : Star height dimension (y-axis).

        >>> r = Star(BPoint(0, 0), 10, 10)
        >>> r.center, r.width, r.height
        ((0, 0), 10, 10)
        """
        super(Star, self).__init__(center, width, height)

    def get_rects(self):
        """get a rectangle corners that contains the shape.

        >>> s = Star(BPoint(10, 10), 4, 4)
        >>> s.get_rects()
        [((10, 12), (10, 12), (10, 8), (10, 8)), ((8, 10), (8, 10), (12, 10), (12, 10))]
        """
        top, bottom, left, right = self.get_corners()
        return [(top, top, bottom, bottom), (left, left, right, right)]

    def is_inside(self, other):
        """Checks if the given point is inside the shape.

        >>> s = Star(BPoint(10, 10), 4, 4)
        >>> s.is_inside(BPoint(10, 11)), s.is_inside(BPoint(10, 12)), s.is_inside(BPoint(10, 13))
        (True, True, False)
        >>> s.is_inside(BPoint(10, 9)), s.is_inside(BPoint(10, 8)), s.is_inside(BPoint(10, 7))
        (True, True, False)
        >>> s.is_inside(BPoint(9, 10)), s.is_inside(BPoint(8, 10)), s.is_inside(BPoint(7, 10))
        (True, True, False)
        >>> s.is_inside(BPoint(11, 10)), s.is_inside(BPoint(12, 10)), s.is_inside(BPoint(13, 10))
        (True, True, False)
        """
        top, bottom, left, right = self.get_corners()
        return ((other.x == self.center.x) and (bottom.y <= other.y <= top.y)) or\
               ((other.y == self.center.y) and (left.x <= other.x <= right.x))

    def get_all_points_inside(self):
        """Returns all points contained in the shape.

        >>> s = Star(BPoint(10, 10), 2, 2)
        >>> s.get_all_points_inside()
        [(9, 10), (11, 10), (10, 9), (10, 11), (10, 10)]
        """
        top, bottom, left, right = self.get_corners()
        all_points = []
        for x in [val for val in range(left.x, right.x + 1) if val != self.center.x]:
            all_points.append(BPoint(x, self.center.y))
        for y in [val for val in range(bottom.y, top.y + 1) if val != self.center.y]:
            all_points.append(BPoint(self.center.x, y))
        all_points.append(BPoint(self.center.x, self.center.y))
        return all_points

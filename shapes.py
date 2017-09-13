from bpoint import BPoint
import abc


class Shape(abc.ABC):
    """Shape class is an abstract class that provides an interface to be
    implemented for any concrete shape class.
    """

    def __init__(self, theCenter, theWidth, theHeight):
        """Shape class initialization method.

        Args:
            theCenter (BPoint) : Point to the center of shape.
            theWidth (int) : Shape width dimension (x-axis).
            theHeight (int) : Shape height dimension (y-axis).
        """
        self._center = theCenter
        self._width = theWidth
        self._height = theHeight

    @property
    def Center(self):
        """Gets _center attribute value.
        """
        return self._center

    @Center.setter
    def Center(self, theValue):
        """Sets _center attribute value.
        """
        if isinstance(theValue, BPoint):
            self._center = theValue
        else:
            raise NotImplementedError

    @property
    def Width(self):
        """Gets _width attribute value.
        """
        return self._width

    @Width.setter
    def Width(self, theValue):
        """Set _width attribute value.
        """
        self._width = theValue

    @property
    def Height(self):
        """Gets _height attribute value.
        """
        return self._height

    @Height.setter
    def Height(self, theValue):
        """Set _height attribute value.
        """
        self._height = theValue

    @abc.abstractmethod
    def getCorners(theOther):
        """Gets all shape corners.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def getRects(self):
        """Get a rectangle corners that contains the shape.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def isInside(self, theOther):
        """Checks if the given point is inside the shape.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def getAllInsidePoints(self):
        """Returns all points contained in the shape.
        """
        raise NotImplementedError


class Quad(Shape):
    """Quad class derived from Shape class and implements a Square or
    Rectangle shape.
    """

    def __init__(self, theCenter, theWidth, theHeight):
        """Quad class initialization method.

        Args:
            theCenter (BPoint) : Point to the center of quad.
            theWidth (int) : Quad width dimension (x-axis).
            theHeight (int) : Quad height dimension (y-axis).

        >>> q = Quad(BPoint(0, 0), 10, 10)
        >>> q.Center, q.Width, q.Height
        ((0, 0), 10, 10)
        >>> q.Center = BPoint(1, 1)
        >>> q.Center
        (1, 1)
        >>> q.Width = 20
        >>> q.Height = 15
        >>> q.Width, q.Height
        (20, 15)
        """
        super(Quad, self).__init__(theCenter, theWidth, theHeight)

    def getCorners(self):
        """Gets all shape corners.

        >>> q = Quad(BPoint(10, 10), 10, 10)
        >>> q.getCorners()
        ((5, 15), (15, 15), (5, 5), (15, 5))
        """
        topLeft = self.Center.xyTranslate(-self.Width / 2, self.Height / 2)
        topRight = self.Center.xyTranslate(self.Width / 2, self.Height / 2)
        bottomLeft = self.Center.xyTranslate(-self.Width / 2, -self.Height / 2)
        bottomRight = self.Center.xyTranslate(self.Width / 2, -self.Height / 2)
        return (topLeft, topRight, bottomLeft, bottomRight)

    def getRects(self):
        """Get a rectangle corners that contains the shape.

        >>> q = Quad(BPoint(10, 10), 10, 10)
        >>> q.getRects()
        [((5, 15), (15, 15), (5, 5), (15, 5))]
        """
        return [self.getCorners(), ]

    def isInside(self, theOther):
        """Checks if the given point is inside the shape.

        >>> q = Quad(BPoint(10, 10), 4, 4)
        >>> q.isInside(BPoint(11, 11)), q.isInside(BPoint(9, 9))
        (True, True)
        >>> q.isInside(BPoint(13, 11)), q.isInside(BPoint(10, 5))
        (False, False)
        """
        topLeft, topRight, bottomLeft, bottomRight = self.getCorners()
        return (topLeft.X <= theOther.X <= topRight.X) and\
               (bottomRight.Y <= theOther.Y <= topRight.Y)

    def getAllInsidePoints(self):
        """Returns all points contained in the shape.

        >>> q = Quad(BPoint(10, 10), 2, 2)
        >>> q.getAllInsidePoints()
        [(9, 9), (9, 10), (9, 11), (10, 9), (10, 10), (10, 11), (11, 9), (11, 10), (11, 11)]
        """
        allPoints = []
        topLeft, topRight, bottomLeft, bottomRight = self.getCorners()
        for x in range(topLeft.X, topRight.X + 1):
            for y in range(bottomRight.Y, topRight.Y + 1):
                allPoints.append(BPoint(x, y))
        return allPoints


class Rectangle(Quad):
    """Rectanle class derived from Quad class, it is basically a Quad
    but the hook point is not the Center, but the bottom-left corner.
    """

    def __init__(self, theCorner, theWidth, theHeight):
        """Rectangle class initialization method.

        Args:
            theCorner (BPoint) : Point to the bottom-left of the rectangle..
            theWidth (int) : Rectangle width dimension (x-axis).
            theHeight (int) : Rectangle height dimension (y-axis).

        >>> q = Rectangle(BPoint(0, 0), 2, 2)
        >>> q.Center, q.Width, q.Height
        ((1, 1), 2, 2)
        >>> q.getCorners()
        ((0, 2), (2, 2), (0, 0), (2, 0))
        >>> q.getRects()
        [((0, 2), (2, 2), (0, 0), (2, 0))]
        >>> q.isInside(BPoint(3, 3)), q.isInside(BPoint(1, 1))
        (False, True)
        >>> q.getAllInsidePoints()
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        """
        center = BPoint(theCorner.X + int(theWidth / 2), theCorner.Y + int(theHeight / 2))
        super(Rectangle, self).__init__(center, theWidth, theHeight)

    @Quad.Center.setter
    def Center(self, theValue):
        """Sets _center attribute value. Rectangle can not update Center.

        >>> q = Rectangle(BPoint(0, 0), 2, 2)
        >>> try:
        ...     q.Center = BPoint(1, 1)
        ... except NotImplementedError:
        ...     'NotImplemented'
        'NotImplemented'
        """
        raise NotImplementedError

    @Quad.Width.setter
    def Width(self, theValue):
        """Sets _width attribute value. Rectangle can not update Width.
        >>> try:
        ...     q.Width = 20
        ... except NotImplementedError:
        ...     'NotImplemented'
        'NotImplemented'
        """
        raise NotImplementedError

    @Quad.Height.setter
    def Height(self, theValue):
        """Sets _height attribute value. Rectangle can not update Height.
        >>> try:
        ...     q.Height = 15
        ... except NotImplementedError:
        ...     'NotImplemented'
        'NotImplemented'
        """
        raise NotImplementedError


class Rhomboid(Shape):
    """Rhomboid class derives from Shape class and it implements a
    Rhomboid shape.
    """

    def __init__(self, theCenter, theWidth, theHeight):
        """Rhomboid class initialization method.

        Args:
            theCenter (BPoint) : Point to the center of rombhoid.
            theWidth (int) : Rombhoid width dimension (x-axis).
            theHeight (int) : Rombhoid height dimension (y-axis).

        >>> r = Rhomboid(BPoint(0, 0), 10, 10)
        >>> r.Center, r.Width, r.Height
        ((0, 0), 10, 10)
        >>> r.Center = BPoint(1, 1)
        >>> r.Center
        (1, 1)
        """
        if theWidth == theHeight:
            super(Rhomboid, self).__init__(theCenter, theWidth, theHeight)
        else:
            raise NotImplementedError

    @Shape.Width.setter
    def Width(self, theValue):
        """Set _width attribute value. Rhomboid have same Width and Height

        >>> r = Rhomboid(BPoint(0, 0), 10, 10)
        >>> r.Width, r.Height
        (10, 10)
        >>> r.Width = 20
        >>> r.Width, r.Height
        (20, 20)
        """
        self._width = theValue
        self._height = theValue

    @Shape.Height.setter
    def Height(self, theValue):
        """Set _height attribute value. Rhomboid have same Width and Height

        >>> r = Rhomboid(BPoint(0, 0), 10, 10)
        >>> r.Width, r.Height
        (10, 10)
        >>> r.Height = 15
        >>> r.Width, r.Height
        (15, 15)
        """
        self._height = theValue
        self._width = theValue

    def getCorners(self):
        """Gets all shape corners.

        >>> r = Rhomboid(BPoint(10, 10), 4, 4)
        >>> r.getCorners()
        ((10, 12), (10, 8), (8, 10), (12, 10))
        """
        top = self.Center.yTranslate(self.Height / 2)
        bottom = self.Center.yTranslate(-self.Height / 2)
        left = self.Center.xTranslate(-self.Width / 2)
        right = self.Center.xTranslate(self.Width / 2)
        return (top, bottom, left, right)

    def getRects(self):
        """Get a rectangle corners that contains the shape.

        >>> r = Rhomboid(BPoint(10, 10), 10, 10)
        >>> r.getRects()
        [((5, 15), (15, 15), (5, 5), (15, 5))]
        """
        topLeft = self.Center.xyTranslate(-self.Width / 2, self.Height / 2)
        topRight = self.Center.xyTranslate(self.Width / 2, self.Height / 2)
        bottomLeft = self.Center.xyTranslate(-self.Width / 2, -self.Height / 2)
        bottomRight = self.Center.xyTranslate(self.Width / 2, -self.Height / 2)
        return [(topLeft, topRight, bottomLeft, bottomRight), ]

    def isInside(self, theOther):
        """Checks if the given point is inside the shape.

        >>> r = Rhomboid(BPoint(5, 5), 6, 6)
        >>> r.isInside(BPoint(6, 5)), r.isInside(BPoint(6, 6)), r.isInside(BPoint(6, 7)), r.isInside(BPoint(6, 8))
        (True, True, True, False)
        >>> r.isInside(BPoint(7, 5)), r.isInside(BPoint(7, 6)), r.isInside(BPoint(7, 7)), r.isInside(BPoint(7, 8))
        (True, True, False, False)
        >>> r.isInside(BPoint(8, 5)), r.isInside(BPoint(8, 6)), r.isInside(BPoint(8, 7)), r.isInside(BPoint(8, 8))
        (True, False, False, False)
        >>> r.isInside(BPoint(6, 4)), r.isInside(BPoint(6, 3)), r.isInside(BPoint(6, 2))
        (True, True, False)
        >>> r.isInside(BPoint(7, 4)), r.isInside(BPoint(7, 3)), r.isInside(BPoint(7, 2))
        (True, False, False)
        >>> r.isInside(BPoint(4, 5)), r.isInside(BPoint(4, 6)), r.isInside(BPoint(4, 7)), r.isInside(BPoint(4, 8))
        (True, True, True, False)
        >>> r.isInside(BPoint(3, 5)), r.isInside(BPoint(3, 6)), r.isInside(BPoint(3, 7)), r.isInside(BPoint(3, 8))
        (True, True, False, False)
        """
        top, bottom, left, right = self.getCorners()
        if theOther in [top, bottom, left, right]:
            return True
        else:
            halfWidth = int(self.Width / 2)
            halfHeight = int(self.Height / 2)
            p = theOther.xyTranslate(-self.Center.X, -self.Center.Y)
            return (abs(p.X) < halfWidth) and (abs(p.Y) < halfHeight) and\
                   (abs(p.Y) <= (halfWidth - abs(p.X)))

    def getAllInsidePoints(self):
        """Returns all points contained in the shape.

        >>> r = Rhomboid(BPoint(10, 10), 4, 4)
        >>> r.getAllInsidePoints()
        [(8, 10), (9, 9), (9, 10), (9, 11), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (11, 9), (11, 10), (11, 11), (12, 10)]
        """
        allPoints = []
        topLeft, topRight, bottomLeft, bottomRight = self.getRects()[0]
        for x in range(topLeft.X, topRight.X + 1):
            for y in range(bottomRight.Y, topRight.Y + 1):
                bp = BPoint(x, y)
                if self.isInside(bp):
                    allPoints.append(bp)
        return allPoints


class Star(Rhomboid):
    """Star class derives from Rhomboid class and it implements a Star shape.

    A start shape only have point in the along the center X-coordinate and the
    center Y-coordinate.
    """

    def __init__(self, theCenter, theWidth, theHeight):
        """Star class initialization method.

        Args:
            theCenter (BPoint) : Point to the center of star.
            theWidth (int) : Star width dimension (x-axis).
            theHeight (int) : Star height dimension (y-axis).

        >>> r = Star(BPoint(0, 0), 10, 10)
        >>> r.Center, r.Width, r.Height
        ((0, 0), 10, 10)
        """
        super(Star, self).__init__(theCenter, theWidth, theHeight)

    def getRects(self):
        """get a rectangle corners that contains the shape.

        >>> s = Star(BPoint(10, 10), 4, 4)
        >>> s.getRects()
        [((10, 12), (10, 12), (10, 8), (10, 8)), ((8, 10), (8, 10), (12, 10), (12, 10))]
        """
        top, bottom, left, right = self.getCorners()
        return [(top, top, bottom, bottom), (left, left, right, right)]

    def isInside(self, theOther):
        """Checks if the given point is inside the shape.

        >>> s = Star(BPoint(10, 10), 4, 4)
        >>> s.isInside(BPoint(10, 11)), s.isInside(BPoint(10, 12)), s.isInside(BPoint(10, 13))
        (True, True, False)
        >>> s.isInside(BPoint(10, 9)), s.isInside(BPoint(10, 8)), s.isInside(BPoint(10, 7))
        (True, True, False)
        >>> s.isInside(BPoint(9, 10)), s.isInside(BPoint(8, 10)), s.isInside(BPoint(7, 10))
        (True, True, False)
        >>> s.isInside(BPoint(11, 10)), s.isInside(BPoint(12, 10)), s.isInside(BPoint(13, 10))
        (True, True, False)
        """
        top, bottom, left, right = self.getCorners()
        return ((theOther.X == self.Center.X) and (bottom.Y <= theOther.Y <= top.Y)) or\
               ((theOther.Y == self.Center.Y) and (left.X <= theOther.X <= right.X))

    def getAllInsidePoints(self):
        """Returns all points contained in the shape.

        >>> s = Star(BPoint(10, 10), 2, 2)
        >>> s.getAllInsidePoints()
        [(9, 10), (11, 10), (10, 9), (10, 11), (10, 10)]
        """
        top, bottom, left, right = self.getCorners()
        allPoints = []
        for x in [val for val in range(left.X, right.X + 1) if val != self.Center.X]:
            allPoints.append(BPoint(x, self.Center.Y))
        for y in [val for val in range(bottom.Y, top.Y + 1) if val != self.Center.Y]:
            allPoints.append(BPoint(self.Center.X, y))
        allPoints.append(BPoint(self.Center.X, self.Center.Y))
        return allPoints

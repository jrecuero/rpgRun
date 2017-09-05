from bpoint import BPoint
import abc


class Shape(abc.ABC):
    """Shape class is an abstract class that provides an interface to be
    implemented for any concrete shape class.
    """

    def __init__(self, theCenter, theWidth, theHeight):
        """Shape class initialization method.
        """
        if isinstance(theCenter, BPoint):
            self._center = theCenter
            self._width = theWidth
            self._height = theHeight
        else:
            raise NotImplementedError

    @property
    def Center(self):
        """
        """
        return self._center

    @Center.setter
    def Center(self, theValue):
        """
        """
        if isinstance(theValue, BPoint):
            self._center = theValue
        else:
            raise NotImplementedError

    @property
    def Width(self):
        """
        """
        return self._width

    @Width.setter
    def Width(self, theValue):
        """
        """
        self._width = theValue

    @property
    def Height(self):
        """
        """
        return self._height

    @Height.setter
    def Height(self, theValue):
        """
        """
        self._height = theValue

    @abc.abstractmethod
    def getCorners(theOther):
        """
        """
        raise NotImplementedError

    @abc.abstractmethod
    def getRects(self):
        """
        """
        raise NotImplementedError

    @abc.abstractmethod
    def isInside(self, theOther):
        """
        """
        raise NotImplementedError

    @abc.abstractmethod
    def getAllInsidePoints(self):
        """
        """
        raise NotImplementedError


class Quad(Shape):
    """Quad class derived from Shape class and implements a Square or
    Rectangle shape.
    """

    def __init__(self, theCenter, theWidth, theHeight):
        """Quad class initialization method.

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
        """
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
        """
        >>> q = Quad(BPoint(10, 10), 10, 10)
        >>> q.getRects()
        [((5, 15), (15, 15), (5, 5), (15, 5))]
        """
        return [self.getCorners(), ]

    def isInside(self, theOther):
        """
        >>> q = Quad(BPoint(10, 10), 4, 4)
        >>> q.isInside(BPoint(11, 11)), q.isInside(BPoint(9, 9))
        (True, True)
        >>> q.isInside(BPoint(13, 11)), q.isInside(BPoint(10, 5))
        (False, False)
        """
        topLeft, topRight, bottomLeft, bottomRight = self.getCorners()
        return (topLeft.X <= theOther.X <= topRight.X) and\
               (bottomRight.Y <= theOther.Y <= topRight.X)

    def getAllInsidePoints(self):
        """
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


class Rhomboid(Shape):
    """Rhomboid class derives from Shape class and it implements a
    Rhomboid shape.
    """

    def __init__(self, theCenter, theWidth, theHeight):
        """Rhomboid class initialization method.

        >>> r = Rhomboid(BPoint(0, 0), 10, 10)
        >>> r.Center, r.Width, r.Height
        ((0, 0), 10, 10)
        >>> r.Center = BPoint(1, 1)
        >>> r.Center
        (1, 1)
        >>> r.Width = 20
        >>> r.Width, r.Height
        (20, 20)
        >>> r.Height = 15
        >>> r.Width, r.Height
        (15, 15)
        """
        if theWidth == theHeight:
            super(Rhomboid, self).__init__(theCenter, theWidth, theHeight)
        else:
            raise NotImplementedError

    @Shape.Width.setter
    def Width(self, theValue):
        """
        """
        self._width = theValue
        self._height = theValue

    @Shape.Height.setter
    def Height(self, theValue):
        """
        """
        self._height = theValue
        self._width = theValue

    def getCorners(self):
        """
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
        """
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
        """
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
        """
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
        """
        super(Star, self).__init__(theCenter, theWidth, theHeight)

    def getRects(self):
        """
        >>> s = Star(BPoint(10, 10), 4, 4)
        >>> s.getRects()
        [((10, 12), (10, 12), (10, 8), (10, 8)), ((8, 10), (8, 10), (12, 10), (12, 10))]
        """
        top, bottom, left, right = self.getCorners()
        return [(top, top, bottom, bottom), (left, left, right, right)]

    def isInside(self, theOther):
        """
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
        """
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

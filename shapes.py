from bpoint import Bpoint
import abc


class Shape(abc.ABC):

    def __init__(self, theCenter, theWidth, theHeight):
        if isinstance(theCenter, Bpoint):
            self._center = theCenter
            self._width = theWidth
            self._height = theHeight
        else:
            raise NotImplemented

    @property
    def Center(self):
        return self._center

    @Center.setter
    def Center(self, theValue):
        if isinstance(theValue, Bpoint):
            self._center = theValue
        else:
            raise NotImplemented

    @property
    def Width(self):
        return self._width

    @Width.setter
    def Width(self, theValue):
        self._width = theValue

    @property
    def Height(self):
        return self._height

    @Height.setter
    def Height(self, theValue):
        self._height = theValue

    @abc.abstractmethod
    def getCorners(theOther):
        pass

    @abc.abstractmethod
    def isInside(theOther):
        pass


class Quad(Shape):

    def __init__(self, theCenter, theWidth, theHeight):
        """
        >>> q = Quad(Bpoint(0, 0), 10, 10)
        >>> q.Center, q.Width, q.Height
        ((0, 0), 10, 10)
        >>> q.Center = Bpoint(1, 1)
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
        >>> q = Quad(Bpoint(10, 10), 10, 10)
        >>> q.getCorners()
        ((5, 15), (15, 15), (5, 5), (15, 5))
        """
        topLeft = self.Center.xyTranslate(-self.Width / 2, self.Height / 2)
        topRight = self.Center.xyTranslate(self.Width / 2, self.Height / 2)
        bottomLeft = self.Center.xyTranslate(-self.Width / 2, -self.Height / 2)
        bottomRigth = self.Center.xyTranslate(self.Width / 2, -self.Height / 2)
        return (topLeft, topRight, bottomLeft, bottomRigth)

    def isInside(self, theOther):
        """
        >>> q = Quad(Bpoint(10, 10), 4, 4)
        >>> q.isInside(Bpoint(11, 11)), q.isInside(Bpoint(9, 9))
        (True, True)
        >>> q.isInside(Bpoint(13, 11)), q.isInside(Bpoint(10, 5))
        (False, False)
        """
        topLeft, topRight, bottomLeft, bottomRigth = self.getCorners()
        return (topLeft.X <= theOther.X <= topRight.X) and\
               (bottomRigth.Y <= theOther.Y <= topRight.X)


class Rhomboid(Shape):

    def __init__(self, theCenter, theWidth, theHeight):
        """
        >>> r = Rhomboid(Bpoint(0, 0), 10, 10)
        >>> r.Center, r.Width, r.Height
        ((0, 0), 10, 10)
        >>> r.Center = Bpoint(1, 1)
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
            raise NotImplemented

    @Shape.Width.setter
    def Width(self, theValue):
        self._width = theValue
        self._height = theValue

    @Shape.Height.setter
    def Height(self, theValue):
        self._height = theValue
        self._width = theValue

    def getCorners(self):
        """
        >>> r = Rhomboid(Bpoint(10, 10), 4, 4)
        >>> r.getCorners()
        ((10, 12), (10, 8), (8, 10), (12, 10))
        """
        top = self.Center.yTranslate(self.Height / 2)
        bottom = self.Center.yTranslate(-self.Height / 2)
        left = self.Center.xTranslate(-self.Width / 2)
        right = self.Center.xTranslate(self.Width / 2)
        return (top, bottom, left, right)

    def isInside(self, theOther):
        """
        >>> r = Rhomboid(Bpoint(5, 5), 6, 6)
        >>> r.isInside(Bpoint(6, 5)), r.isInside(Bpoint(6, 6)), r.isInside(Bpoint(6, 7)), r.isInside(Bpoint(6, 8))
        (True, True, True, False)
        >>> r.isInside(Bpoint(7, 5)), r.isInside(Bpoint(7, 6)), r.isInside(Bpoint(7, 7)), r.isInside(Bpoint(7, 8))
        (True, True, False, False)
        >>> r.isInside(Bpoint(8, 5)), r.isInside(Bpoint(8, 6)), r.isInside(Bpoint(8, 7)), r.isInside(Bpoint(8, 8))
        (True, False, False, False)
        >>> r.isInside(Bpoint(6, 4)), r.isInside(Bpoint(6, 3)), r.isInside(Bpoint(6, 2))
        (True, True, False)
        >>> r.isInside(Bpoint(7, 4)), r.isInside(Bpoint(7, 3)), r.isInside(Bpoint(7, 2))
        (True, False, False)
        >>> r.isInside(Bpoint(4, 5)), r.isInside(Bpoint(4, 6)), r.isInside(Bpoint(4, 7)), r.isInside(Bpoint(4, 8))
        (True, True, True, False)
        >>> r.isInside(Bpoint(3, 5)), r.isInside(Bpoint(3, 6)), r.isInside(Bpoint(3, 7)), r.isInside(Bpoint(3, 8))
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


class Star(Rhomboid):

    def __init__(self, theCenter, theWidth, theHeight):
        super(Star, self).__init__(theCenter, theWidth, theHeight)

    def isInside(self, theOther):
        top, bottom, left, right = self.getCorners()
        return ((theOther.X == self.Center.X) and (top.Y <= theOther.Y < bottom.Y)) or\
               ((theOther.Y == self.Center.Y) and (right.X <= theOther.X < left.X))

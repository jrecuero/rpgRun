import math


class Point(object):

    def __init__(self, theX, theY):
        self._x = int(theX)
        self._y = int(theY)

    @property
    def X(self):
        return self._x

    @X.setter
    def X(self, theValue):
        self._x = int(theValue)

    @property
    def Y(self):
        return self._y

    @Y.setter
    def Y(self, theValue):
        self._y = int(theValue)

    def isXpositive(self):
        """
        >>> p = Point(1, 1)
        >>> p.isXpositive()
        True
        >>> p = Point(-1, 1)
        >>> p.isXpositive()
        False
        """
        return self.X > 0

    def isXnegative(self):
        """
        >>> p = Point(1, 0)
        >>> p.isXnegative()
        False
        >>> p = Point(-1, 0)
        >>> p.isXnegative()
        True
        """
        return self.X < 0

    def isXzero(self):
        """
        >>> p = Point(0, 1)
        >>> p.isXzero()
        True
        >>> p = Point(1, 0)
        >>> p.isXzero()
        False
        """
        return self.X == 0

    def isYpositive(self):
        """
        >>> p = Point(0, 1)
        >>> p.isYpositive()
        True
        >>> p = Point(0, -1)
        >>> p.isYpositive()
        False
        """
        return self.Y > 0

    def isYnegative(self):
        """
        >>> p = Point(0, 1)
        >>> p.isYnegative()
        False
        >>> p = Point(0, -1)
        >>> p.isYnegative()
        True
        """
        return self.Y < 0

    def isYzero(self):
        """
        >>> p = Point(1, 0)
        >>> p.isYzero()
        True
        >>> p = Point(0, 1)
        >>> p.isYzero()
        False
        """
        return self.Y == 0

    def __repr__(self):
        """
        >>> str(Point(0, 0))
        '(0, 0)'
        """
        return '({0}, {1})'.format(self.X, self.Y)

    def __eq__(self, theOther):
        """
        >>> Point(1, 1) == Point(1, 1)
        True
        >>> Point(1, 1) == Point(1, 0)
        False
        >>> Point(1, 1) == Point(0, 1)
        False
        >>> Point(1, 1) in [Point(0, 0), Point(0, 1), Point(1, 1)]
        True
        >>> Point(1, 0) in [Point(0, 0), Point(0, 1), Point(1, 1)]
        False
        """
        if isinstance(theOther, Point):
            return self.isXeq(theOther) and self.isYeq(theOther)
        return NotImplemented

    def __neq__(self, theOther):
        """
        >>> Point(1, 1) != Point(1, 1)
        False
        >>> Point(1, 1) != Point(1, 0)
        True
        >>> Point(1, 1) != Point(0, 1)
        True
        """
        if isinstance(theOther, Point):
            return not self.__eq__(theOther)
        return NotImplemented

    def isYgreater(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.isYgreater(Point(0, 0))
        True
        >>> p.isYgreater(Point(0, 2))
        False
        """
        if isinstance(theOther, Point):
            return self.Y > theOther.Y
        return NotImplemented

    def isYlower(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.isYlower(Point(0, 0))
        False
        >>> p.isYlower(Point(0, 2))
        True
        """
        if isinstance(theOther, Point):
            return self.Y < theOther.Y
        return NotImplemented

    def isYeq(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.isYeq(Point(0, 1))
        True
        >>> p.isYeq(Point(0, 0))
        False
        """
        if isinstance(theOther, Point):
            return self.Y == theOther.Y
        return NotImplemented

    def isXgreater(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.isXgreater(Point(0, 0))
        True
        >>> p.isXgreater(Point(2, 0))
        False
        """
        if isinstance(theOther, Point):
            return self.X > theOther.X
        return NotImplemented

    def isXlower(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.isXlower(Point(0, 0))
        False
        >>> p.isXlower(Point(2, 0))
        True
        """
        if isinstance(theOther, Point):
            return self.X < theOther.X
        return NotImplemented

    def isXeq(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.isXeq(Point(0, 0))
        False
        >>> p.isXeq(Point(1, 0))
        True
        """
        if isinstance(theOther, Point):
            return self.X == theOther.X
        return NotImplemented

    def __add__(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p + Point(1, 2)
        (2, 3)
        >>> Point(3, 5) + p
        (4, 6)
        """
        if isinstance(theOther, Point):
            klass = self.__class__
            return klass(self.X + theOther.X, self.Y + theOther.Y)
        return NotImplemented

    def __sub__(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p - Point(2, 0)
        (-1, 1)
        >>> Point(10, 10) - p
        (9, 9)
        """
        if isinstance(theOther, Point):
            klass = self.__class__
            return klass(self.X - theOther.X, self.Y - theOther.Y)
        return NotImplemented

    def distance(self, theOther):
        """
        >>> p = Point(0, 0)
        >>> p.distance(Point(2, 2))
        2.8284271247461903
        """
        if isinstance(theOther, Point):
            return math.hypot(theOther.X - self.X, theOther.Y - self.Y)
        return NotImplemented

    def intDistance(self, theOther):
        """
        >>> p = Point(0, 0)
        >>> p.intDistance(Point(2, 2))
        2
        """
        if isinstance(theOther, Point):
            return int(self.distance(theOther))
        return NotImplemented

    def pointDistance(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.pointDistance(Point(2, 3))
        (1, 2)
        """
        if isinstance(theOther, Point):
            return theOther - self
        return NotImplemented

    def xDistance(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.xDistance(Point(2, 1))
        1
        """
        if isinstance(theOther, Point):
            return theOther.X - self.X
        return NotImplemented

    def yDistance(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.yDistance(Point(2, 1))
        0
        """
        if isinstance(theOther, Point):
            return theOther.Y - self.Y
        return NotImplemented

    def translate(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.translate(Point(2, 3))
        (3, 4)
        """
        if isinstance(theOther, Point):
            return self + theOther
        return NotImplemented

    def xTranslate(self, theX):
        """
        >>> p = Point(0, 0)
        >>> p.xTranslate(10)
        (10, 0)
        """
        return self + Point(int(theX), 0)

    def yTranslate(self, theY):
        """
        >>> p = Point(0, 0)
        >>> p.yTranslate(5)
        (0, 5)
        """
        return self + Point(0, int(theY))

    def xyTranslate(self, theX, theY):
        """
        >>> p = Point(0, 0)
        >>> p.xyTranslate(1, 5)
        (1, 5)
        """
        return self + Point(int(theX), int(theY))

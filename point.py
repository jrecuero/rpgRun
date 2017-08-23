import math


class Range(object):

    def __init__(self, theMin, theMax):
        self._min = int(theMin)
        self._max = int(theMax)

    @property
    def Min(self):
        return self._min

    @Min.setter
    def Min(self, theValue):
        self._min = int(theValue)

    @property
    def Max(self):
        return self._max

    @Max.setter
    def Max(self, theValue):
        self._max = int(theValue)


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

    def _isPositive(self, theAttr):
        return theAttr > 0

    def _isNegative(self, theAttr):
        return theAttr < 0

    def _isZero(self, theAttr):
        return theAttr == 0

    def isXpositive(self):
        """
        >>> p = Point(1, 1)
        >>> p.isXpositive()
        True
        >>> p = Point(-1, 1)
        >>> p.isXpositive()
        False
        """
        return self._isPositive(self.X)

    def isXnegative(self):
        """
        >>> p = Point(1, 0)
        >>> p.isXnegative()
        False
        >>> p = Point(-1, 0)
        >>> p.isXnegative()
        True
        """
        return self._isNegative(self.X)

    def isXzero(self):
        """
        >>> p = Point(0, 1)
        >>> p.isXzero()
        True
        >>> p = Point(1, 0)
        >>> p.isXzero()
        False
        """
        return self._isZero(self.X)

    def isYpositive(self):
        """
        >>> p = Point(0, 1)
        >>> p.isYpositive()
        True
        >>> p = Point(0, -1)
        >>> p.isYpositive()
        False
        """
        return self._isPositive(self.Y)

    def isYnegative(self):
        """
        >>> p = Point(0, 1)
        >>> p.isYnegative()
        False
        >>> p = Point(0, -1)
        >>> p.isYnegative()
        True
        """
        return self._isNegative(self.Y)

    def isYzero(self):
        """
        >>> p = Point(1, 0)
        >>> p.isYzero()
        True
        >>> p = Point(0, 1)
        >>> p.isYzero()
        False
        """
        return self._isZero(self.Y)

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

    def _isGreater(self, theAttr, theOtherAttr):
        return theAttr > theOtherAttr

    def _isLower(self, theAttr, theOtherAttr):
        return theAttr < theOtherAttr

    def _isEq(self, theAttr, theOtherAttr):
        return theAttr == theOtherAttr

    def isYgreater(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.isYgreater(Point(0, 0))
        True
        >>> p.isYgreater(Point(0, 2))
        False
        """
        if isinstance(theOther, Point):
            return self._isGreater(self.Y, theOther.Y)
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
            return self._isLower(self.Y, theOther.Y)
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
            return self._isEq(self.Y, theOther.Y)
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
            return self._isGreater(self.X, theOther.X)
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
            return self._isLower(self.X, theOther.X)
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
            return self._isEq(self.X, theOther.X)
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

    def _distance(self, theAttr, theOtherAttr):
        return theAttr - theOtherAttr

    def xDistance(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.xDistance(Point(2, 1))
        1
        """
        if isinstance(theOther, Point):
            return self._distance(theOther.X, self.X)
        return NotImplemented

    def yDistance(self, theOther):
        """
        >>> p = Point(1, 1)
        >>> p.yDistance(Point(2, 1))
        0
        """
        if isinstance(theOther, Point):
            return self._distance(theOther.Y, self.Y)
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

    def _move(self, theAttr, theValue):
        return theAttr + int(theValue)

    def xMove(self, theX=1):
        """
        >>> p = Point(1, 1)
        >>> p.xMove(1)
        (2, 1)
        >>> p.xMove()
        (3, 1)
        >>> p.xMove(2).xMove()
        (6, 1)
        """
        self.X = self._move(self.X, theX)
        return self

    def yMove(self, theY=1):
        """
        >>> p = Point(1, 1)
        >>> p.yMove(1)
        (1, 2)
        >>> p.yMove()
        (1, 3)
        >>> p.yMove(2).yMove()
        (1, 6)
        """
        self.Y = self._move(self.Y, theY)
        return self

    def xyMove(self, theX=1, theY=1):
        """
        >>> p = Point(1, 1)
        >>> p.xyMove(1, 1)
        (2, 2)
        >>> p.xyMove(1).xyMove(0, 2).xyMove()
        (4, 6)
        """
        self.xMove(theX)
        self.yMove(theY)
        return self

    def _moveWithinRange(self, theAttr, theRange, theValue, theUpTo):
        value = theAttr + int(theValue)
        if theRange.Min <= value <= theRange.Max:
            theAttr = value
        elif theUpTo and theRange.Min > value:
            theAttr = theRange.Min
        elif theUpTo and theRange.Max < value:
            theAttr = theRange.Max
        return theAttr

    def xMoveWithinRange(self, theRange, theX=1, theUpTo=False):
        """
        >>> p = Point(1, 1)
        >>> p.xMoveWithinRange(Range(0, 10))
        (2, 1)
        >>> p.xMoveWithinRange(Range(0, 10), 5)
        (7, 1)
        >>> p.xMoveWithinRange(Range(0, 10), 5)
        (7, 1)
        >>> p.xMoveWithinRange(Range(0, 10), 5, True)
        (10, 1)
        """
        if isinstance(theRange, Range):
            self.X = self._moveWithinRange(self.X, theRange, theX, theUpTo)
            return self
        else:
            raise NotImplemented

    def yMoveWithinRange(self, theRange, theY=1, theUpTo=False):
        """
        >>> p = Point(1, 1)
        >>> p.yMoveWithinRange(Range(0, 10))
        (1, 2)
        >>> p.yMoveWithinRange(Range(0, 10), 2)
        (1, 4)
        >>> p.yMoveWithinRange(Range(0, 10), 10)
        (1, 4)
        >>> p.yMoveWithinRange(Range(0, 10), 10, True)
        (1, 10)
        """
        if isinstance(theRange, Range):
            self.Y = self._moveWithinRange(self.Y, theRange, theY, theUpTo)
            return self
        else:
            raise NotImplemented

    def xyMoveWithinRange(self, theRangeX, theRangeY, theX=1, theY=1, theUpTo=False):
        """
        >>> p = Point(1, 1)
        >>> p.xyMoveWithinRange(Range(0, 10), Range(0, 7))
        (2, 2)
        >>> p.xyMoveWithinRange(Range(0, 10), Range(0, 7), 2, 1)
        (4, 3)
        >>> p.xyMoveWithinRange(Range(0, 10), Range(0, 7), 1, 5)
        (5, 3)
        >>> p.xyMoveWithinRange(Range(0, 10), Range(0, 7), 10, 1)
        (5, 4)
        >>> p.xyMoveWithinRange(Range(0, 10), Range(0, 7), 10, 10, True)
        (10, 7)
        """
        if isinstance(theRangeX, Range) and isinstance(theRangeY, Range):
            self.xMoveWithinRange(theRangeX, theX, theUpTo)
            self.yMoveWithinRange(theRangeY, theY, theUpTo)
            return self
        else:
            raise NotImplemented

    def xMoveWithCollision(self, theCollisions, theX=1, theRangeX=None, theUpTo=False):
        """
        >>> p = Point(1, 1)
        >>> p.xMoveWithCollision([Point(0, 0)])
        (2, 1)
        >>> p.xMoveWithCollision([Point(0, 0)], 2)
        (4, 1)
        >>> p.xMoveWithCollision([Point(0, 0), Point(6, 1)], 2)
        (4, 1)
        >>> p.xMoveWithCollision([Point(0, 0), Point(6, 1)], 2, None, True)
        (5, 1)
        >>> p.xMoveWithCollision([Point(0, 0), Point(9, 1), Point(10, 1)], 5, None, True)
        (8, 1)
        >>> p.xMoveWithCollision([Point(0, 0)], 10, Range(0, 10))
        (8, 1)
        >>> p.xMoveWithCollision([Point(0, 0)], 10, Range(0, 10), True)
        (10, 1)
        """
        if type(theCollisions) in (list, tuple) and theCollisions:
            backupX = self.X
            moveX = self._move(self.X, theX)
            if theRangeX:
                limit = theX if theRangeX.Min <= moveX < theRangeX.Max else None
                if limit is None and theUpTo:
                    if theRangeX.Min > moveX:
                        limit = self.X - theRangeX.Min
                    elif theRangeX.Max < moveX:
                        limit = theRangeX.Max - self.X
                elif limit is None and not theUpTo:
                    return self
            else:
                limit = theX
            for inc in range(limit):
                self.xMove()
                for p in theCollisions:
                    if self == p:
                        if theUpTo:
                            self.xMove(-1)
                        else:
                            self.X = backupX
                        return self
            return self
        else:
            raise NotImplemented

    def yMoveWithCollision(self, theCollisions, theY=1, theRangeY=None, theUpTo=False):
        """
        >>> p = Point(1, 1)
        >>> p.yMoveWithCollision([Point(0, 0)])
        (1, 2)
        >>> p.yMoveWithCollision([Point(0, 0)], 2)
        (1, 4)
        >>> p.yMoveWithCollision([Point(0, 0), Point(1, 6)], 2)
        (1, 4)
        >>> p.yMoveWithCollision([Point(0, 0), Point(1, 6)], 2, None, True)
        (1, 5)
        >>> p.yMoveWithCollision([Point(0, 0), Point(1, 9), Point(1, 10)], 5, None, True)
        (1, 8)
        >>> p.yMoveWithCollision([Point(0, 0)], 10, Range(0, 10))
        (1, 8)
        >>> p.yMoveWithCollision([Point(0, 0)], 10, Range(0, 10), True)
        (1, 10)
        """
        if type(theCollisions) in (list, tuple) and theCollisions:
            backupY = self.Y
            moveY = self._move(self.Y, theY)
            if theRangeY:
                limit = theY if theRangeY.Min <= moveY < theRangeY.Max else None
                if limit is None and theUpTo:
                    if theRangeY.Min > moveY:
                        limit = self.Y - theRangeY.Min
                    elif theRangeY.Max < moveY:
                        limit = theRangeY.Max - self.Y
                elif limit is None and not theUpTo:
                    return self
            else:
                limit = theY
            for inc in range(limit):
                self.yMove()
                for p in theCollisions:
                    if self == p:
                        if theUpTo:
                            self.yMove(-1)
                        else:
                            self.Y = backupY
                        return self
            return self
        else:
            raise NotImplemented
import math


class Point(object):

    def __init__(self, theX, theY):
        self._x = theX
        self._y = theY

    @property
    def X(self):
        return self._x

    @X.setter
    def X(self, theValue):
        self._x = theValue

    @property
    def Y(self):
        return self._y

    @Y.setter
    def Y(self, theValue):
        self._y = theValue

    def isXpositive(self):
        return self.X > 0

    def isXnegative(self):
        return self.X < 0

    def isXzero(self):
        return self.X == 0

    def isYpositive(self):
        return self.Y > 0

    def isYnegative(self):
        return self.Y < 0

    def isYzero(self):
        return self.Y == 0

    def __repr__(self):
        return '({0}, {1})'.format(self.X, self.Y)

    def __eq__(self, theOther):
        if isinstance(theOther, Point):
            return self.isXeq(theOther) and self.isYeq(theOther)
        return NotImplemented

    def __neq__(self, theOther):
        if isinstance(theOther, Point):
            return not self.__eq__(theOther)
        return NotImplemented

    def isYgreater(self, theOther):
        if isinstance(theOther, Point):
            return self.Y > theOther.Y
        return NotImplemented

    def isYlower(self, theOther):
        if isinstance(theOther, Point):
            return self.Y < theOther.Y
        return NotImplemented

    def isYeq(self, theOther):
        if isinstance(theOther, Point):
            return self.Y == theOther.Y
        return NotImplemented

    def isXgreater(self, theOther):
        if isinstance(theOther, Point):
            return self.X > theOther.X
        return NotImplemented

    def isXlower(self, theOther):
        if isinstance(theOther, Point):
            return self.X < theOther.X
        return NotImplemented

    def isXeq(self, theOther):
        if isinstance(theOther, Point):
            return self.X == theOther.X
        return NotImplemented

    def __add__(self, theOther):
        if isinstance(theOther, Point):
            klass = self.__class__
            return klass(self.X + theOther.X, self.Y + theOther.Y)
        return NotImplemented

    def __sub__(self, theOther):
        if isinstance(theOther, Point):
            klass = self.__class__
            return klass(self.X - theOther.X, self.Y - theOther.Y)
        return NotImplemented

    def distance(self, theOther):
        if isinstance(theOther, Point):
            return math.hypot(theOther.X - self.X, theOther.Y - self.Y)
        return NotImplemented

    def intDistance(self, theOther):
        if isinstance(theOther, Point):
            return int(self.distance(theOther))
        return NotImplemented

    def pointDistance(self, theOther):
        if isinstance(theOther, Point):
            return theOther - self
        return NotImplemented

    def xDistance(self, theOther):
        if isinstance(theOther, Point):
            return theOther.X - self.X
        return NotImplemented

    def yDistance(self, theOther):
        if isinstance(theOther, Point):
            return theOther.Y - self.Y
        return NotImplemented

    def translate(self, theOther):
        return self + theOther

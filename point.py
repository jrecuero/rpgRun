import math
from range import Range


class Point(object):
    """Point class represent a basic 2D point representation.

    X-axis is the horizontal axe, it has positive values to the right and
    negative values to the left.

    Y-axis is the vertical axe, it has positive values up and negative values
    down.

    Translate operations returns a new point with the final translation. The
    original point (self) is unchanged.

    Move operations update the original point (self) with given values for
    X and Y coordinates.
    """

    def __init__(self, theX, theY):
        """Point class initialization method.

        Args:
            theX (int) : X-axis coordinate.
            theY (int) : Y-axis coordinate.
        """
        self._x = int(theX)
        self._y = int(theY)

    @property
    def X(self):
        """Property that returns the _x attribute.

        Returns:
            int : X-axis coordinate attribute.

        >>> p = Point(1, 0)
        >>> p.X
        1
        """
        return self._x

    @X.setter
    def X(self, theValue):
        """Property that sets a new value for the _x attribute.

        Args:
            theValue (int) : new value for the X-axis coordinate attribute.

        >>> p = Point(1, 0)
        >>> p.X
        1
        >>> p.X = 2
        >>> p.X
        2
        """
        self._x = int(theValue)

    @property
    def Y(self):
        """Property that returns the _y attribute.

        Returns:
            int : Y-axis coordinate attribute.

        >>> p = Point(1, 2)
        >>> p.Y
        2
        """
        return self._y

    @Y.setter
    def Y(self, theValue):
        """Property that sets a new value for the _y attribute.

        Args:
            theValue (int) : new value for the Y-axis coordinate attribute.

        >>> p = Point(1, 2)
        >>> p.Y
        2
        >>> p.Y = 10
        >>> p.Y
        10
        """
        self._y = int(theValue)

    @property
    def Klass(self):
        """Gets the class to be used for arithmetical operations.

        >>> p = Point(1, 1)
        >>> p.Klass
        <class 'point.Point'>
        """
        return self.__class__

    def _isPositive(self, theValue):
        """Checks if the value passed is in the positive axe.

        Args:
            theValue (int) : value to check.

        Returns:
            boolean : True is value is in the positive axe, False else.

        >>> p = Point(0, 0)
        >>> p._isPositive(1)
        True
        >>> p._isPositive(-1)
        False
        """
        return theValue > 0

    def _isNegative(self, theValue):
        """Checks if the value passed is in the negative axe.

        Args:
            theValue (int) : value to check.

        Returns:
            boolean : True is value is in the negative axe, False else.

        >>> p = Point(0, 0)
        >>> p._isNegative(1)
        False
        >>> p._isNegative(-1)
        True
        """
        return theValue < 0

    def _isZero(self, theValue):
        """Checks if the value passed is in the axe origin.

        Args:
            theValue (int) : value to check.

        Returns:
            boolean : True is value is in the axe origin, False else.

        >>> p = Point(0, 0)
        >>> p._isZero(0)
        True
        >>> p._isZero(1)
        False
        >>> p._isZero(-1)
        False
        """
        return theValue == 0

    def isXpositive(self):
        """Check if the point is in the positive X-axe.

        Returns:
            boolean : True if point is in the positive X-axe, False else.

        >>> p = Point(1, 1)
        >>> p.isXpositive()
        True
        >>> p = Point(-1, 1)
        >>> p.isXpositive()
        False
        """
        return self._isPositive(self.X)

    def isXnegative(self):
        """Check if the point is in the negative X-axe.

        Returns:
            boolean : True if point is in the negative X-axe, False else.

        >>> p = Point(1, 0)
        >>> p.isXnegative()
        False
        >>> p = Point(-1, 0)
        >>> p.isXnegative()
        True
        """
        return self._isNegative(self.X)

    def isXzero(self):
        """Check if the point is the X-axe origin.

        Returns:
            boolean : True if point is in the X-axe origin, False else.

        >>> p = Point(0, 1)
        >>> p.isXzero()
        True
        >>> p = Point(1, 0)
        >>> p.isXzero()
        False
        """
        return self._isZero(self.X)

    def isYpositive(self):
        """Check if the point is in the positive Y-axe.

        Returns:
            boolean : True if point is in the positive Y-axe, False else.

        >>> p = Point(0, 1)
        >>> p.isYpositive()
        True
        >>> p = Point(0, -1)
        >>> p.isYpositive()
        False
        """
        return self._isPositive(self.Y)

    def isYnegative(self):
        """Check if the point is in the negative Y-axe.

        Returns:
            boolean : True if point is in the negative Y-axe, False else.

        >>> p = Point(0, 1)
        >>> p.isYnegative()
        False
        >>> p = Point(0, -1)
        >>> p.isYnegative()
        True
        """
        return self._isNegative(self.Y)

    def isYzero(self):
        """Check if the point is the Y-axe origin.

        Returns:
            boolean : True if point is in the Y-axe origin, False else.

        >>> p = Point(1, 0)
        >>> p.isYzero()
        True
        >>> p = Point(0, 1)
        >>> p.isYzero()
        False
        """
        return self._isZero(self.Y)

    def __repr__(self):
        """String representation for the Point instance.

        Returns:
            str : string with the Point instance representation.

        >>> str(Point(0, 0))
        '(0, 0)'
        """
        return '({0}, {1})'.format(self.X, self.Y)

    def __eq__(self, theOther):
        """Overload method for the 'equal to' operation between Point
        instances.

        Two Point instances are equal if X and Y coordinates values are
        equal.

        Args:
            theOther (Point) : the other Point instance to check if is equal.

        Returns:
            boolean : True if Point instaces are equal, False else.

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
        """Overload method for the 'not equal to' operation between Point
        instances.

        Two Point instances are not equal if X or Y coordinates values are
        not equal.

        Args:
            theOther (Point) : the other Point instance to check if is not
            equal.

        Returns:
            boolean : True if Point instaces are not equal, False else.

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

    def _isGreater(self, theValue, theOtherValue):
        """Checks if one value is greater than other.

        >>> p = Point(1, 1)
        >>> p._isGreater(2, 1)
        True
        >>> p._isGreater(1, 2)
        False
        >>> p._isGreater(1, 1)
        False
        """
        return theValue > theOtherValue

    def _isLower(self, theValue, theOtherValue):
        """Checks if one value is lower than other

        >>> p = Point(1, 1)
        >>> p._isLower(2, 1)
        False
        >>> p._isLower(1, 2)
        True
        >>> p._isLower(1, 1)
        False
        """
        return theValue < theOtherValue

    def _isEq(self, theValue, theOtherValue):
        """Checks if two values are equal.

        >>> p = Point(1, 1)
        >>> p._isEq(2, 1)
        False
        >>> p._isEq(1, 2)
        False
        >>> p._isEq(1, 1)
        True
        """
        return theValue == theOtherValue

    def isYgreater(self, theOther):
        """Checks if point Y-coordinate is greater than the one from the
        given point.

        >>> p = Point(1, 1)
        >>> p.isYgreater(Point(0, 0))
        True
        >>> p.isYgreater(Point(0, 2))
        False
        """
        if isinstance(theOther, Point):
            return self._isGreater(self.Y, theOther.Y)
        raise NotImplementedError

    def isYlower(self, theOther):
        """Checks if point Y-coordinate is lower than the one from the
        given point.

        >>> p = Point(1, 1)
        >>> p.isYlower(Point(0, 0))
        False
        >>> p.isYlower(Point(0, 2))
        True
        """
        if isinstance(theOther, Point):
            return self._isLower(self.Y, theOther.Y)
        raise NotImplementedError

    def isYeq(self, theOther):
        """Checks if point Y-coordinate is equal than the one from the
        given point.

        >>> p = Point(1, 1)
        >>> p.isYeq(Point(0, 1))
        True
        >>> p.isYeq(Point(0, 0))
        False
        """
        if isinstance(theOther, Point):
            return self._isEq(self.Y, theOther.Y)
        raise NotImplementedError

    def isXgreater(self, theOther):
        """Checks if point X-coordinate is greated than the one form the
        given point.

        >>> p = Point(1, 1)
        >>> p.isXgreater(Point(0, 0))
        True
        >>> p.isXgreater(Point(2, 0))
        False
        """
        if isinstance(theOther, Point):
            return self._isGreater(self.X, theOther.X)
        raise NotImplementedError

    def isXlower(self, theOther):
        """Checks if point X-coordinate is lower than the one form the
        given point.

        >>> p = Point(1, 1)
        >>> p.isXlower(Point(0, 0))
        False
        >>> p.isXlower(Point(2, 0))
        True
        """
        if isinstance(theOther, Point):
            return self._isLower(self.X, theOther.X)
        raise NotImplementedError

    def isXeq(self, theOther):
        """Checks if point X-coordinate is equal than the one form the
        given point.

        >>> p = Point(1, 1)
        >>> p.isXeq(Point(0, 0))
        False
        >>> p.isXeq(Point(1, 0))
        True
        """
        if isinstance(theOther, Point):
            return self._isEq(self.X, theOther.X)
        raise NotImplementedError

    def __add__(self, theOther):
        """Overload addition operation between two Point instances.

        >>> p = Point(1, 1)
        >>> p + Point(1, 2)
        (2, 3)
        >>> Point(3, 5) + p
        (4, 6)
        """
        if isinstance(theOther, Point):
            return self.Klass(self.X + theOther.X, self.Y + theOther.Y)
        return NotImplemented

    def __sub__(self, theOther):
        """Overload substract operation between two Point instances.

        >>> p = Point(1, 1)
        >>> p - Point(2, 0)
        (-1, 1)
        >>> Point(10, 10) - p
        (9, 9)
        """
        if isinstance(theOther, Point):
            return self.Klass(self.X - theOther.X, self.Y - theOther.Y)
        return NotImplemented

    def distance(self, theOther):
        """Returns the distance between the point and the given point.

        Args:
            theOther (Point) : second point to check the distance.

        Returns:
            float : distance between two points.

        >>> p = Point(0, 0)
        >>> p.distance(Point(2, 2))
        2.8284271247461903
        """
        if isinstance(theOther, Point):
            return math.hypot(theOther.X - self.X, theOther.Y - self.Y)
        raise NotImplementedError

    def intDistance(self, theOther):
        """Returns the distance between the point and the given point as an
        integer value.

        Args:
            theOther (Point) : second point to check the distance.

        Returns:
            int : distance between two points.

        >>> p = Point(0, 0)
        >>> p.intDistance(Point(2, 2))
        2
        """
        if isinstance(theOther, Point):
            return int(self.distance(theOther))
        raise NotImplementedError

    def pointDistance(self, theOther):
        """Returns the distance between the point and the given point as a
        Point instance.

        Args:
            theOther (Point) : second point to check the distance.

        Returns:
            Point : distance between two points as a Point.

        >>> p = Point(1, 1)
        >>> p.pointDistance(Point(2, 3))
        (1, 2)
        """
        if isinstance(theOther, Point):
            return theOther - self
        raise NotImplementedError

    def _distance(self, theAttr, theOtherAttr):
        """Retuns the distance (difference) between two values.
        """
        return theAttr - theOtherAttr

    def xDistance(self, theOther):
        """Returns the X-coordinate distance between two points.

        >>> p = Point(1, 1)
        >>> p.xDistance(Point(2, 1))
        1
        """
        if isinstance(theOther, Point):
            return self._distance(theOther.X, self.X)
        raise NotImplementedError

    def yDistance(self, theOther):
        """Returns the Y-coordinate distance between two points.

        >>> p = Point(1, 1)
        >>> p.yDistance(Point(2, 1))
        0
        """
        if isinstance(theOther, Point):
            return self._distance(theOther.Y, self.Y)
        raise NotImplementedError

    def translate(self, theOther):
        """Returns a new translated point by the given point.

        It basically moves the point adding X-coordinates and Y-coordinates.

        Args:
            theOther (Point) : other point used for translation.

        Returns:
            Point : New  point with the translation.

        >>> p = Point(1, 1)
        >>> p.translate(Point(2, 3))
        (3, 4)
        """
        if isinstance(theOther, Point):
            return self + theOther
        raise NotImplementedError

    def xTranslate(self, theX):
        """Returns a new translated point by the given X-coordinate.

        Args:
            theX (int) : X-coordinate value to translate.

        Returns:
            Point : New  point with the translation.

        >>> p = Point(0, 0)
        >>> p.xTranslate(10)
        (10, 0)
        """
        return self + self.Klass(int(theX), 0)

    def yTranslate(self, theY):
        """Returns a new translated point by the given Y-coordinate.

        Args:
            theY (int) : Y-coordinate value to translate.

        Returns:
            Point : New  point with the translation.

        >>> p = Point(0, 0)
        >>> p.yTranslate(5)
        (0, 5)
        """
        return self + self.Klass(0, int(theY))

    def xyTranslate(self, theX, theY):
        """Returns a new translated point by the given X-coordinate and
        Y-coordinate.

        Args:
            theX (int) : X-coordinate value to translate.
            theY (int) : Y-coordinate value to translate.

        Returns:
            Point : New  point with the translation.

        >>> p = Point(0, 0)
        >>> p.xyTranslate(1, 5)
        (1, 5)
        """
        return self + self.Klass(int(theX), int(theY))

    def _move(self, theAttr, theValue):
        """Add a value to other. Used in move operations.

        This methow allows to make generic operations on X-axis and Y-axis.
        """
        return theAttr + int(theValue)

    def xMove(self, theX=1):
        """Updates X-coordinate a given value.

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
        """Updates Y-coordinate a given value.

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
        """Updates X-coordinate and Y-coordinates with given values.

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
        """Move a coordinate a given value but only in the given range.

        This method is used to make generic X-axis and Y-axis operations.
        """
        value = theAttr + int(theValue)
        if theRange.Min <= value <= theRange.Max:
            theAttr = value
        elif theUpTo and theRange.Min > value:
            theAttr = theRange.Min
        elif theUpTo and theRange.Max < value:
            theAttr = theRange.Max
        return theAttr

    def xMoveWithinRange(self, theRange, theX=1, theUpTo=False):
        """Updates X-coordinate a given value but only in the given ranges.

        Args:
            theRange (Range) : range values the X-coordinate can move.

            theX (int) : value to increase the X-coordinate (default = 1).

            theUpTo (boolean) : when flag is True the movement is the closest
            to the final position. False means the movement is not done if it
            is out of range.

        Returns:
            Point : Point instace after the X-coordinate movement.

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
            raise NotImplementedError

    def yMoveWithinRange(self, theRange, theY=1, theUpTo=False):
        """Updates Y-coordinate a given value but only in the given ranges.

        Args:
            theRange (Range) : range values the Y-coordinate can move.

            theY (int) : value to increase the Y-coordinate (default = 1).

            theUpTo (boolean) : when flag is True the movement is the closest
            to the final position. False means the movement is not done if it
            is out of range.

        Returns:
            Point : Point instace after the Y-coordinate movement.

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
            raise NotImplementedError

    def xyMoveWithinRange(self, theRangeX, theRangeY, theX=1, theY=1, theUpTo=False):
        """Updates X-coordiante and Y-coordinate a given value but only in the
        given ranges.

        Args:
            theRangeX (Range) : range values the X-coordinate can move.
            theRangeY (Range) : range values the Y-coordinate can move.

            theX (int) : value to increase the X-coordinate (default = 1).
            theY (int) : value to increase the Y-coordinate (default = 1).

            theUpTo (boolean) : when flag is True the movement is the closest
            to the final position. False means the movement is not done if it
            is out of range.

        Returns:
            Point : Point instace after the Y-coordinate movement.

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
            raise NotImplementedError

    def _moveWithCollision(self, theAttrName, theCollisions, theValue, theRange, theUpTo):
        """Generic method that moves positional attribute X or Y to a given
        position.

        Method checks against a list of possible positions and a range with
        the minimum and maximum values.

        There is a flag that is used to move to the closest position to
        destination or just don't move at all.

        Args:
            theAttrName (str) : String with the name of the positional
            attribute to update. It could be 'X' or 'Y'.

            theCollisions (list/tuple) : list or tuple of Points with
            possible collisions. These points will block the movement.

            theValue (int) : movement value.

            theRange (Range) : range instance with the minimum and
            maximum final position values.

            theUpTo (bool) : boolean that flags if returning initial
            position if the final one is not possible if False, or
            move to the closest position to the destination if True.

        Returns:

            Point : point instance with the final movement position.
        """
        if type(theCollisions) in (list, tuple) and theCollisions:
            # Keep the initial attribute value, just is case we have to roll
            # over it, if it can not move to the final position.
            backupValue = getattr(self, theAttrName)
            # Get the final position, so it is checked against the range of
            # possible values. If the result is out of limits, check if should
            # move up to the closest position or not. If we can not move up to
            # the closest, return the initial position.
            moveValue = self._move(backupValue, theValue)
            if theRange:
                limit = theValue if theRange.Min <= moveValue < theRange.Max else None
                if limit is None and theUpTo:
                    if theRange.Min > moveValue:
                        limit = backupValue - theRange.Min
                    elif theRange.Max < moveValue:
                        limit = theRange.Max - backupValue
                elif limit is None and not theUpTo:
                    return self
            else:
                limit = theValue
            # Move one step at a time, until a collision is found, at that time
            # back down one position is up to close is defined or return the
            # original value if not.
            for inc in range(limit):
                setattr(self, theAttrName, self._move(getattr(self, theAttrName), 1))
                for p in theCollisions:
                    if self == p:
                        if theUpTo:
                            setattr(self, theAttrName, self._move(getattr(self, theAttrName), -1))
                        else:
                            setattr(self, theAttrName, backupValue)
                        return self
            return self
        else:
            raise NotImplementedError

    def xMoveWithCollision(self, theCollisions, theX=1, theRangeX=None, theUpTo=False):
        """Updates X-coordinate a given value in the given range and avoiding any
        collision with given Point instances.

        Args:
            theCollisions (list/tuple) : list or tuple of Points with
            possible collisions. These points will block the movement.

            theX (int) : x-coordinate movement value.

            theRangeX (Range) : range instance with the minimum and
            maximum final position values.

            theUpTo (bool) : boolean that flags if returning initial
            position if the final one is not possible if False, or
            move to the closest position to the destination if True.

        Returns:

            Point : point instance with the final movement position.

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
        return self._moveWithCollision('X', theCollisions, theX, theRangeX, theUpTo)

    def yMoveWithCollision(self, theCollisions, theY=1, theRangeY=None, theUpTo=False):
        """Updates Y-coordinate a given value in the given range and avoiding any
        collision with given Point instances.

        Args:
            theCollisions (list/tuple) : list or tuple of Points with
            possible collisions. These points will block the movement.

            theX (int) : Y-coordinate movement value.

            theRangeX (Range) : range instance with the minimum and
            maximum final position values.

            theUpTo (bool) : boolean that flags if returning initial
            position if the final one is not possible if False, or
            move to the closest position to the destination if True.

        Returns:

            Point : point instance with the final movement position.

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
        return self._moveWithCollision('Y', theCollisions, theY, theRangeY, theUpTo)

    def _isValidMove(self, theAttrName, theCollisions, theValue, theRange):
        """Generic method that checks in the positional movement is a valid one
        without collisions.

        Method checks against a list of possible positions and a range with
        the minimum and maximum values.

        Args:
            theAttrName (str) : String with the name of the positional
            attribute to update. It could be 'X' or 'Y'.

            theCollisions (list/tuple) : list or tuple of Points with
            possible collisions. These points will block the movement.

            theValue (int) : movement value.

            theRange (Range) : range instance with the minimum and
            maximum final position values.

        Returns:

            boolean : True if movement is possible, False else
        """
        trav = Point(self.X, self.Y)
        if type(theCollisions) in (list, tuple) and theCollisions:
            moveValue = trav._move(getattr(trav, theAttrName), theValue)
            if theRange:
                limit = theValue if theRange.Min <= moveValue < theRange.Max else None
                if limit is None:
                    return False
            else:
                limit = theValue
            # Move one step at a time, until a collision is found.
            for inc in range(limit):
                setattr(trav, theAttrName, trav._move(getattr(trav, theAttrName), 1))
                for p in theCollisions:
                    if trav == p:
                        return False
            return True
        else:
            raise NotImplementedError

    def xIsValidMove(self, theCollisions, theX=1, theRangeX=None):
        """Check if X-coordinate movement is valid.

        Args:
            theCollisions (list/tuple) : list or tuple of Points with
            possible collisions. These points will block the movement.

            theX (int) : x-coordinate movement value.

            theRangeX (Range) : range instance with the minimum and
            maximum final position values.

        Returns:

            boolean : True if movement is possible, False else

        >>> p = Point(1, 1)
        >>> p.xIsValidMove([Point(0, 0)])
        True
        >>> p.xIsValidMove([Point(0, 0)], 2)
        True
        >>> p.xIsValidMove([Point(0, 0), Point(6, 1)], 2)
        True
        >>> p.xIsValidMove([Point(0, 0), Point(6, 1)], 6)
        False
        >>> p.xIsValidMove([Point(0, 0), Point(6, 1)], 2, None)
        True
        >>> p.xIsValidMove([Point(0, 0), Point(6, 1)], 7, None)
        False
        >>> p.xIsValidMove([Point(0, 0)], 10, Range(0, 10))
        False
        """
        return self._isValidMove('X', theCollisions, theX, theRangeX)

    def yIsValidMove(self, theCollisions, theY=1, theRangeY=None):
        """Check if Y-coordinate movement is valid.

        Args:
            theCollisions (list/tuple) : list or tuple of Points with
            possible collisions. These points will block the movement.

            theY (int) : Y-coordinate movement value.

            theRangeY (Range) : range instance with the minimum and
            maximum final position values.

        Returns:

            boolean : True if movement is possible, False else

        >>> p = Point(1, 1)
        >>> p.yIsValidMove([Point(0, 0)])
        True
        >>> p.yIsValidMove([Point(0, 0)], 2)
        True
        >>> p.yIsValidMove([Point(0, 0), Point(1, 6)], 2)
        True
        >>> p.yIsValidMove([Point(0, 0), Point(1, 6)], 6)
        False
        >>> p.yIsValidMove([Point(0, 0), Point(1, 6)], 2, None)
        True
        >>> p.yIsValidMove([Point(0, 0), Point(1, 6)], 7, None)
        False
        >>> p.yIsValidMove([Point(0, 0)], 10, Range(0, 10))
        False
        """
        return self._isValidMove('Y', theCollisions, theY, theRangeY)

    def isCollision(self, theTranslate, theCollisions):
        """Checks if the point translated with the given Point has any
        collision.

        Args:
            theTranslate (Point) : translation point

            theCollisions (list/tuple) : list or tuple of Points with
            possible collisions. These points will block the movement.

        Returns:
            boolean : True if there is any collision, False else.

        >>> p = Point(1, 1)
        >>> p.isCollision(Point(1, 1), [Point(0, 0)])
        False
        >>> p.isCollision(Point(1, 1), [Point(2, 2)])
        True
        >>> p.isCollision(Point(1, 1), [Point(1, 0), Point(2, 2)])
        True
        """
        newPoint = self.translate(theTranslate)
        for p in theCollisions:
            if newPoint == p:
                return True
        return False

from point import Point
from enum import Enum


class Location(Enum):
    """Location Class Enumeration provides all possible location where a cell
    can be moved on the board.
    """

    FRONT = (1, 0)
    BACK = (2, 0)
    LEFT = (3, 0)
    RIGHT = (4, 0)
    FRONT_LEFT = (1, 3)
    FRONT_RIGHT = (1, 4)
    BACK_LEFT = (2, 3)
    BACK_RIGHT = (2, 4)

    def __init__(self, theX, theY):
        """Location class initialization method.
        """
        self._x = theX
        self._y = theY
        self.__front = 1
        self.__back = 2
        self.__left = 3
        self.__right = 4

    def isFront(self):
        """Checks if the location contains FRONT.

        >>> Location.FRONT.isFront()
        True
        >>> Location.FRONT_LEFT.isFront()
        True
        >>> Location.FRONT_RIGHT.isFront()
        True
        >>> Location.BACK.isFront()
        False
        """
        return self.__front in self.value

    def isBack(self):
        """Checks if the location contains BACK.

        >>> Location.BACK.isBack()
        True
        >>> Location.BACK_LEFT.isBack()
        True
        >>> Location.BACK_RIGHT.isBack()
        True
        >>> Location.RIGHT.isBack()
        False
        """
        return self.__back in self.value

    def isLeft(self):
        """Checks if the location contains LEFT.

        >>> Location.LEFT.isLeft()
        True
        >>> Location.FRONT_LEFT.isLeft()
        True
        >>> Location.BACK_LEFT.isLeft()
        True
        >>> Location.RIGHT.isLeft()
        False
        """
        return self.__left in self.value

    def isRight(self):
        """Checks if the location contains RIGHT.

        >>> Location.RIGHT.isRight()
        True
        >>> Location.FRONT_RIGHT.isRight()
        True
        >>> Location.BACK_RIGHT.isRight()
        True
        >>> Location.FRONT.isRight()
        False
        """
        return self.__right in self.value

    @staticmethod
    def userMoves():
        """Returns all possible location when user is prompted to move.

        >>> Location.userMoves()
        [<Location.FRONT: (1, 0)>, <Location.RIGHT: (4, 0)>, <Location.LEFT: (3, 0)>]
        """
        return [Location.FRONT, Location.RIGHT, Location.LEFT]

    @staticmethod
    def get(theBpointA, theBpointB):
        """Checks the location from the first point to the second point.

        >>> Location.get(BPoint(1, 2), BPoint(1, 1))
        <Location.FRONT: (1, 0)>
        >>> Location.get(BPoint(1, 0), BPoint(1, 1))
        <Location.BACK: (2, 0)>
        >>> Location.get(BPoint(0, 1), BPoint(1, 1))
        <Location.LEFT: (3, 0)>
        >>> Location.get(BPoint(2, 1), BPoint(1, 1))
        <Location.RIGHT: (4, 0)>
        >>> Location.get(BPoint(0, 2), BPoint(1, 1))
        <Location.FRONT_LEFT: (1, 3)>
        >>> Location.get(BPoint(2, 2), BPoint(1, 1))
        <Location.FRONT_RIGHT: (1, 4)>
        >>> Location.get(BPoint(0, 0), BPoint(1, 1))
        <Location.BACK_LEFT: (2, 3)>
        >>> Location.get(BPoint(2, 0), BPoint(1, 1))
        <Location.BACK_RIGHT: (2, 4)>
        """
        if isinstance(theBpointA, BPoint) and isinstance(theBpointB, BPoint):
            if theBpointA.isJustFront(theBpointB):
                return Location.FRONT
            elif theBpointA.isJustBack(theBpointB):
                return Location.BACK
            elif theBpointA.isFrontRight(theBpointB):
                return Location.FRONT_RIGHT
            elif theBpointA.isFrontLeft(theBpointB):
                return Location.FRONT_LEFT
            elif theBpointA.isJustRight(theBpointB):
                return Location.RIGHT
            elif theBpointA.isJustLeft(theBpointB):
                return Location.LEFT
            elif theBpointA.isBackLeft(theBpointB):
                return Location.BACK_LEFT
            elif theBpointA.isBackRight(theBpointB):
                return Location.BACK_RIGHT
        return NotImplemented


class BPoint(Point):
    """BPoint class derived from Point class and it adds some required
    functinality for a point on a board.
    """

    def __init__(self, theX, theY):
        """BPoint class initialization method.
        """
        super(BPoint, self).__init__(theX, theY)
        self._moveCb = {Location.FRONT: self.moveToFront,
                        Location.BACK: self.moveToBack,
                        Location.LEFT: self.moveToLeft,
                        Location.RIGHT: self.moveToRight,
                        Location.FRONT_LEFT: None,
                        Location.FRONT_RIGHT: None,
                        Location.BACK_LEFT: None,
                        Location.BACK_RIGHT: None}

    def isFront(self, theOther):
        """Checks if the point is in front of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.isFront(BPoint(0, 0))
        True
        >>> bp.isFront(BPoint(2, 0))
        True
        >>> bp.isFront(BPoint(0, 2))
        False
        """
        return self.isYgreater(theOther)

    def isBack(self, theOther):
        """Checks if the point is in the back of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.isBack(BPoint(0, 0))
        False
        >>> bp.isBack(BPoint(2, 0))
        False
        >>> bp.isBack(BPoint(0, 2))
        True
        """
        return self.isYlower(theOther)

    def isLeft(self, theOther):
        """Checks if the point is to the left of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.isLeft(BPoint(0, 0))
        False
        >>> bp.isLeft(BPoint(2, 0))
        True
        >>> bp.isLeft(BPoint(0, 2))
        False
        """
        return self.isXlower(theOther)

    def isRight(self, theOther):
        """Checks if the point is to the right of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.isRight(BPoint(0, 0))
        True
        >>> bp.isRight(BPoint(2, 0))
        False
        >>> bp.isRight(BPoint(0, 2))
        True
        """
        return self.isXgreater(theOther)

    def isFrontLeft(self, theOther):
        """Checks if the point is to the front-left of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.isFrontLeft(BPoint(0, 0))
        False
        >>> bp.isFrontLeft(BPoint(2, 0))
        True
        """
        return self.isFront(theOther) and self.isLeft(theOther)

    def isFrontRight(self, theOther):
        """Checks if the point is to the front-right of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.isFrontRight(BPoint(0, 0))
        True
        >>> bp.isFrontRight(BPoint(2, 0))
        False
        """
        return self.isFront(theOther) and self.isRight(theOther)

    def isBackLeft(self, theOther):
        """Checks if the point is to the back-left of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.isBackLeft(BPoint(0, 0))
        False
        >>> bp.isBackLeft(BPoint(2, 2))
        True
        """
        return self.isBack(theOther) and self.isLeft(theOther)

    def isBackRight(self, theOther):
        """Checks if the point is to the back-right of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.isBackRight(BPoint(0, 0))
        False
        >>> bp.isBackRight(BPoint(0, 2))
        True
        """
        return self.isBack(theOther) and self.isRight(theOther)

    def isJustFront(self, theOther):
        """Checks if the point is just in front of the given point (same Y).

        >>> bp = BPoint(1, 1)
        >>> bp.isJustFront(BPoint(0, 0))
        False
        >>> bp.isJustFront(BPoint(1, 0))
        True
        """
        return self.isFront(theOther) and self.isXeq(theOther)

    def isJustBack(self, theOther):
        """Checks if the point is just in back of the given point (same Y).

        >>> bp = BPoint(1, 1)
        >>> bp.isJustBack(BPoint(0, 0))
        False
        >>> bp.isJustBack(BPoint(1, 2))
        True
        """
        return self.isBack(theOther) and self.isXeq(theOther)

    def isJustLeft(self, theOther):
        """Checks if the point is just to the left of the given point (same X).

        >>> bp = BPoint(1, 1)
        >>> bp.isJustLeft(BPoint(0, 0))
        False
        >>> bp.isJustLeft(BPoint(2, 1))
        True
        """
        return self.isLeft(theOther) and self.isYeq(theOther)

    def isJustRight(self, theOther):
        """Checks if the point is just to the right of the given point (same X).

        >>> bp = BPoint(1, 1)
        >>> bp.isJustRight(BPoint(0, 0))
        False
        >>> bp.isJustRight(BPoint(0, 1))
        True
        """
        return self.isRight(theOther) and self.isYeq(theOther)

    def moveToFront(self, theMove=1):
        """Moves point to the front a given number of positions.

        >>> bp = BPoint(1, 1)
        >>> bp.moveToFront()
        (1, 2)
        >>> bp.moveToFront(5)
        (1, 7)
        """
        return self.yMove(theMove)

    def moveToBack(self, theMove=1):
        """Moves point to the back a given number of positions.

        >>> bp = BPoint(1, 10)
        >>> bp.moveToBack()
        (1, 9)
        >>> bp.moveToBack(5)
        (1, 4)
        """
        return self.yMove(-theMove)

    def moveToRight(self, theMove=1):
        """Moves point to the right a given number of positions.

        >>> bp = BPoint(1, 1)
        >>> bp.moveToRight()
        (2, 1)
        >>> bp.moveToRight(5)
        (7, 1)
        """
        return self.xMove(theMove)

    def moveToLeft(self, theMove=1):
        """Moves point to the left a given number of positions.

        >>> bp = BPoint(10, 1)
        >>> bp.moveToLeft()
        (9, 1)
        >>> bp.moveToLeft(5)
        (4, 1)
        """
        return self.xMove(-theMove)

    def moveTo(self, theDirection=Location.FRONT, theMove=1):
        """Moves the BPoint the given value to the given location.

        >>> bp = BPoint(1, 1)
        >>> bp.moveTo()
        (1, 2)
        >>> bp.moveTo(Location.RIGHT)
        (2, 2)
        >>> bp.moveTo(Location.FRONT, 2)
        (2, 4)
        >>> bp.moveTo(Location.LEFT, 1)
        (1, 4)
        >>> bp.moveTo(Location.FRONT_RIGHT, 10)
        (1, 4)
        >>> bp.moveTo(Location.FRONT_LEFT, 10)
        (1, 4)
        >>> bp.moveTo(Location.BACK_RIGHT, 10)
        (1, 4)
        >>> bp.moveTo(Location.BACK_LEFT, 10)
        (1, 4)
        """
        assert isinstance(theDirection, Location)
        cb = self._moveCb[theDirection]
        if cb is None:
            return self
        else:
            return cb(theMove)

from point import Point
from enum import Enum


class Location(Enum):

    FRONT = (1, 0)
    BACK = (2, 0)
    LEFT = (3, 0)
    RIGHT = (4, 0)
    FRONT_LEFT = (1, 3)
    FRONT_RIGHT = (1, 4)
    BACK_LEFT = (2, 3)
    BACK_RIGHT = (2, 4)

    def __init__(self, theX, theY):
        self._x = theX
        self._y = theY
        self.__front = 1
        self.__back = 2
        self.__left = 3
        self.__right = 4

    def isFront(self):
        """
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
        """
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
        """
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
        """
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
    def get(theBpointA, theBpointB):
        """
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

    def __init__(self, theX, theY):
        super(BPoint, self).__init__(theX, theY)

    def isFront(self, theOther):
        """
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
        """
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
        """
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
        """
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
        """
        >>> bp = BPoint(1, 1)
        >>> bp.isFrontLeft(BPoint(0, 0))
        False
        >>> bp.isFrontLeft(BPoint(2, 0))
        True
        """
        return self.isFront(theOther) and self.isLeft(theOther)

    def isFrontRight(self, theOther):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.isFrontRight(BPoint(0, 0))
        True
        >>> bp.isFrontRight(BPoint(2, 0))
        False
        """
        return self.isFront(theOther) and self.isRight(theOther)

    def isBackLeft(self, theOther):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.isBackLeft(BPoint(0, 0))
        False
        >>> bp.isBackLeft(BPoint(2, 2))
        True
        """
        return self.isBack(theOther) and self.isLeft(theOther)

    def isBackRight(self, theOther):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.isBackRight(BPoint(0, 0))
        False
        >>> bp.isBackRight(BPoint(0, 2))
        True
        """
        return self.isBack(theOther) and self.isRight(theOther)

    def isJustFront(self, theOther):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.isJustFront(BPoint(0, 0))
        False
        >>> bp.isJustFront(BPoint(1, 0))
        True
        """
        return self.isFront(theOther) and self.isXeq(theOther)

    def isJustBack(self, theOther):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.isJustBack(BPoint(0, 0))
        False
        >>> bp.isJustBack(BPoint(1, 2))
        True
        """
        return self.isBack(theOther) and self.isXeq(theOther)

    def isJustLeft(self, theOther):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.isJustLeft(BPoint(0, 0))
        False
        >>> bp.isJustLeft(BPoint(2, 1))
        True
        """
        return self.isLeft(theOther) and self.isYeq(theOther)

    def isJustRight(self, theOther):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.isJustRight(BPoint(0, 0))
        False
        >>> bp.isJustRight(BPoint(0, 1))
        True
        """
        return self.isRight(theOther) and self.isYeq(theOther)

    def moveToFront(self, theMove=1):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.moveToFront()
        (1, 2)
        >>> bp.moveToFront(5)
        (1, 7)
        """
        return self.yMove(theMove)

    def moveToBack(self, theMove=1):
        """
        >>> bp = BPoint(1, 10)
        >>> bp.moveToBack()
        (1, 9)
        >>> bp.moveToBack(5)
        (1, 4)
        """
        return self.yMove(-theMove)

    def moveToRight(self, theMove=1):
        """
        >>> bp = BPoint(1, 1)
        >>> bp.moveToRight()
        (2, 1)
        >>> bp.moveToRight(5)
        (7, 1)
        """
        return self.xMove(theMove)

    def moveToLeft(self, theMove=1):
        """
        >>> bp = BPoint(10, 1)
        >>> bp.moveToLeft()
        (9, 1)
        >>> bp.moveToLeft(5)
        (4, 1)
        """
        return self.xMove(-theMove)

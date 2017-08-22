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

    def isFront(self):
        return self.FRONT in self.value

    def isBack(self):
        return self.BACK in self.value

    def isLeft(self):
        return self.LEFT in self.value

    def isRight(self):
        return self.RIGHT in self.value

    @staticmethod
    def get(theBpointA, theBpointB):
        if isinstance(theBpointA, Bpoint) and isinstance(theBpointB, Bpoint):
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


class Bpoint(Point):

    def __init__(self, theX, theY):
        super(Bpoint, self).__init__(theX, theY)

    def isFront(self, theOther):
        return self.isYgreater(theOther)

    def isBack(self, theOther):
        return self.isYlower(theOther)

    def isLeft(self, theOther):
        return self.isXlower(theOther)

    def isRight(self, theOther):
        return self.isXgreater(theOther)

    def isFrontLeft(self, theOther):
        return self.isFront(theOther) and self.isLeft(theOther)

    def isFrontRight(self, theOther):
        return self.isFront(theOther) and self.isRight(theOther)

    def isBackLeft(self, theOther):
        return self.isBack(theOther) and self.isLeft(theOther)

    def isBackRight(self, theOther):
        return self.isBack(theOther) and self.isRight(theOther)

    def isJustFront(self, theOther):
        return self.isFront(theOther) and self.isXeq(theOther)

    def isJustBack(self, theOther):
        return self.isBack(theOther) and self.isXeq(theOther)

    def isJustLeft(self, theOther):
        return self.isLeft(theOther) and self.isYeq(theOther)

    def isJustRight(self, theOther):
        return self.isRight(theOther) and self.isYeq(theOther)

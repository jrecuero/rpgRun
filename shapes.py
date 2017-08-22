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
        super(Quad, self).__init__(theCenter, theWidth, theHeight)

    def getCorners(self):
        topLeft = self.Center.translate(-self.Width / 2, self.Height / 2)
        topRight = self.Center.translate(self.Width / 2, self.Height / 2)
        bottomLeft = self.Center.translate(-self.Width / 2, -self.Height / 2)
        bottomRigth = self.Center.translate(self.Width / 2, -self.Height / 2)
        return (topLeft, topRight, bottomLeft, bottomRigth)

    def isInside(self, theOther):
        topLeft, topRight, bottomLeft, bottomRigth = self.getCorners()
        return (topLeft.X <= theOther.X <= topRight.X) and\
               (bottomRigth.Y <= theOther.Y <= topRight.X)


class Rhomboid(Shape):

    def __init__(self, theCenter, theWidth, theHeight):
        if theWidth == theHeight:
            super(Rhomboid, self).__init__(theCenter, theWidth, theHeight)
        else:
            raise NotImplemented

    def getCorners(self):
        top = self.Center.translate(0, self.Height / 2)
        bottom = self.Center.translate(0, -self.Height / 2)
        left = self.Center.translate(-self.Width / 2, 0)
        right = self.Center.translate(self.Width / 2, 0)
        return (top, bottom, left, right)

    def isInside(self, theOther):
        top, bottom, left, right = self.getCorners()
        if theOther in [top, bottom, left, right]:
            return True
        else:
            p = theOther.translate(-self.Center.X, -self.Center.Y)
            return (abs(p.X) < self.Width) and (abs(p.Y) < self.Height) and\
                   ((self.Width - abs(p.X)) <= abs(p.Y))


class Star(Rhomboid):

    def __init__(self, theCenter, theWidth, theHeight):
        super(Star, self).__init__(theCenter, theWidth, theHeight)

    def isInside(self, theOther):
        top, bottom, left, right = self.getCorners()
        return ((theOther.X == self.Center.X) and (top.Y <= theOther.Y < bottom.Y)) or\
               ((theOther.Y == self.Center.Y) and (right.X <= theOther.X < left.X))

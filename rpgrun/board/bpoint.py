from enum import Enum
from rpgrun.board.point import Point


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

    def __init__(self, x, y):
        """Location class initialization method.
        """
        self._x = x
        self._y = y
        self.__front = 1
        self.__back = 2
        self.__left = 3
        self.__right = 4

    def is_front(self):
        """Checks if the location contains FRONT.

        >>> Location.FRONT.is_front()
        True
        >>> Location.FRONT_LEFT.is_front()
        True
        >>> Location.FRONT_RIGHT.is_front()
        True
        >>> Location.BACK.is_front()
        False
        """
        return self.__front in self.value

    def is_back(self):
        """Checks if the location contains BACK.

        >>> Location.BACK.is_back()
        True
        >>> Location.BACK_LEFT.is_back()
        True
        >>> Location.BACK_RIGHT.is_back()
        True
        >>> Location.RIGHT.is_back()
        False
        """
        return self.__back in self.value

    def is_left(self):
        """Checks if the location contains LEFT.

        >>> Location.LEFT.is_left()
        True
        >>> Location.FRONT_LEFT.is_left()
        True
        >>> Location.BACK_LEFT.is_left()
        True
        >>> Location.RIGHT.is_left()
        False
        """
        return self.__left in self.value

    def is_right(self):
        """Checks if the location contains RIGHT.

        >>> Location.RIGHT.is_right()
        True
        >>> Location.FRONT_RIGHT.is_right()
        True
        >>> Location.BACK_RIGHT.is_right()
        True
        >>> Location.FRONT.is_right()
        False
        """
        return self.__right in self.value

    @staticmethod
    def user_moves():
        """Returns all possible location when user is prompted to move.

        >>> Location.user_moves()
        [<Location.FRONT: (1, 0)>, <Location.RIGHT: (4, 0)>, <Location.LEFT: (3, 0)>]
        """
        return [Location.FRONT, Location.RIGHT, Location.LEFT]

    @staticmethod
    def get(bpoint_a, bpoint_b):
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
        if isinstance(bpoint_a, BPoint) and isinstance(bpoint_b, BPoint):
            if bpoint_a.is_just_front(bpoint_b):
                return Location.FRONT
            elif bpoint_a.is_just_back(bpoint_b):
                return Location.BACK
            elif bpoint_a.is_front_right(bpoint_b):
                return Location.FRONT_RIGHT
            elif bpoint_a.is_front_left(bpoint_b):
                return Location.FRONT_LEFT
            elif bpoint_a.is_just_right(bpoint_b):
                return Location.RIGHT
            elif bpoint_a.is_just_left(bpoint_b):
                return Location.LEFT
            elif bpoint_a.is_back_left(bpoint_b):
                return Location.BACK_LEFT
            elif bpoint_a.is_back_right(bpoint_b):
                return Location.BACK_RIGHT
        return NotImplemented


class BPoint(Point):
    """BPoint class derived from Point class and it adds some required
    functinality for a point on a board.
    """

    def __init__(self, x, y):
        """BPoint class initialization method.
        """
        super(BPoint, self).__init__(x, y)
        self._moveCb = {Location.FRONT: self.move_to_front,
                        Location.BACK: self.move_to_back,
                        Location.LEFT: self.move_to_left,
                        Location.RIGHT: self.move_to_right,
                        Location.FRONT_LEFT: None,
                        Location.FRONT_RIGHT: None,
                        Location.BACK_LEFT: None,
                        Location.BACK_RIGHT: None}

    def is_front(self, other):
        """Checks if the point is in front of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.is_front(BPoint(0, 0))
        True
        >>> bp.is_front(BPoint(2, 0))
        True
        >>> bp.is_front(BPoint(0, 2))
        False
        """
        return self.is_y_greater(other)

    def is_back(self, other):
        """Checks if the point is in the back of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.is_back(BPoint(0, 0))
        False
        >>> bp.is_back(BPoint(2, 0))
        False
        >>> bp.is_back(BPoint(0, 2))
        True
        """
        return self.is_y_lower(other)

    def is_left(self, other):
        """Checks if the point is to the left of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.is_left(BPoint(0, 0))
        False
        >>> bp.is_left(BPoint(2, 0))
        True
        >>> bp.is_left(BPoint(0, 2))
        False
        """
        return self.is_x_lower(other)

    def is_right(self, other):
        """Checks if the point is to the right of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.is_right(BPoint(0, 0))
        True
        >>> bp.is_right(BPoint(2, 0))
        False
        >>> bp.is_right(BPoint(0, 2))
        True
        """
        return self.is_x_greater(other)

    def is_front_left(self, other):
        """Checks if the point is to the front-left of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.is_front_left(BPoint(0, 0))
        False
        >>> bp.is_front_left(BPoint(2, 0))
        True
        """
        return self.is_front(other) and self.is_left(other)

    def is_front_right(self, other):
        """Checks if the point is to the front-right of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.is_front_right(BPoint(0, 0))
        True
        >>> bp.is_front_right(BPoint(2, 0))
        False
        """
        return self.is_front(other) and self.is_right(other)

    def is_back_left(self, other):
        """Checks if the point is to the back-left of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.is_back_left(BPoint(0, 0))
        False
        >>> bp.is_back_left(BPoint(2, 2))
        True
        """
        return self.is_back(other) and self.is_left(other)

    def is_back_right(self, other):
        """Checks if the point is to the back-right of the given point.

        >>> bp = BPoint(1, 1)
        >>> bp.is_back_right(BPoint(0, 0))
        False
        >>> bp.is_back_right(BPoint(0, 2))
        True
        """
        return self.is_back(other) and self.is_right(other)

    def is_just_front(self, other):
        """Checks if the point is just in front of the given point (same Y).

        >>> bp = BPoint(1, 1)
        >>> bp.is_just_front(BPoint(0, 0))
        False
        >>> bp.is_just_front(BPoint(1, 0))
        True
        """
        return self.is_front(other) and self.is_x_eq(other)

    def is_just_back(self, other):
        """Checks if the point is just in back of the given point (same Y).

        >>> bp = BPoint(1, 1)
        >>> bp.is_just_back(BPoint(0, 0))
        False
        >>> bp.is_just_back(BPoint(1, 2))
        True
        """
        return self.is_back(other) and self.is_x_eq(other)

    def is_just_left(self, other):
        """Checks if the point is just to the left of the given point (same X).

        >>> bp = BPoint(1, 1)
        >>> bp.is_just_left(BPoint(0, 0))
        False
        >>> bp.is_just_left(BPoint(2, 1))
        True
        """
        return self.is_left(other) and self.is_y_eq(other)

    def is_just_right(self, other):
        """Checks if the point is just to the right of the given point (same X).

        >>> bp = BPoint(1, 1)
        >>> bp.is_just_right(BPoint(0, 0))
        False
        >>> bp.is_just_right(BPoint(0, 1))
        True
        """
        return self.is_right(other) and self.is_y_eq(other)

    def move_to_front(self, move_val=1):
        """Moves point to the front a given number of positions.

        >>> bp = BPoint(1, 1)
        >>> bp.move_to_front()
        (1, 2)
        >>> bp.move_to_front(5)
        (1, 7)
        """
        return self.y_move(move_val)

    def move_to_back(self, move_val=1):
        """Moves point to the back a given number of positions.

        >>> bp = BPoint(1, 10)
        >>> bp.move_to_back()
        (1, 9)
        >>> bp.move_to_back(5)
        (1, 4)
        """
        return self.y_move(-move_val)

    def move_to_right(self, move_val=1):
        """Moves point to the right a given number of positions.

        >>> bp = BPoint(1, 1)
        >>> bp.move_to_right()
        (2, 1)
        >>> bp.move_to_right(5)
        (7, 1)
        """
        return self.x_move(move_val)

    def move_to_left(self, move_val=1):
        """Moves point to the left a given number of positions.

        >>> bp = BPoint(10, 1)
        >>> bp.move_to_left()
        (9, 1)
        >>> bp.move_to_left(5)
        (4, 1)
        """
        return self.x_move(-move_val)

    def move_to(self, direction=Location.FRONT, move_val=1):
        """Moves the BPoint the given value to the given location.

        >>> bp = BPoint(1, 1)
        >>> bp.move_to()
        (1, 2)
        >>> bp.move_to(Location.RIGHT)
        (2, 2)
        >>> bp.move_to(Location.FRONT, 2)
        (2, 4)
        >>> bp.move_to(Location.LEFT, 1)
        (1, 4)
        >>> bp.move_to(Location.FRONT_RIGHT, 10)
        (1, 4)
        >>> bp.move_to(Location.FRONT_LEFT, 10)
        (1, 4)
        >>> bp.move_to(Location.BACK_RIGHT, 10)
        (1, 4)
        >>> bp.move_to(Location.BACK_LEFT, 10)
        (1, 4)
        """
        assert isinstance(direction, Location)
        cb = self._moveCb[direction]
        if cb is None:
            return self
        else:
            return cb(move_val)

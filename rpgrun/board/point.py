import math

from rpgrun.common.range import Range


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

    def __init__(self, x, y):
        """Point class initialization method.

        Args:
            x (int) : X-axis coordinate.
            y (int) : Y-axis coordinate.
        """
        self._x = int(x)
        self._y = int(y)

    @property
    def x(self):
        """Property for _x attribute.

        :getter: Gets _x attribute value.
        :setter: Sets _x attribute value.

        Returns:
            int : X-axis coordinate attribute.

        Example:
            >>> p = Point(1, 0)
            >>> p.x
            1
            >>> p.x = 2
            >>> p.x
            2
        """
        return self._x

    @x.setter
    def x(self, value):
        """Set property for _x attribute.

        Args:
            value (int) : new value for the X-axis coordinate attribute.
        """
        self._x = int(value)

    @property
    def y(self):
        """Property for _y attribute.

        :getter: Gets _y attribute value.
        :setter: Sets _y attribute value.

        Returns:
            int : Y-axis coordinate attribute.

        Example:
            >>> p = Point(1, 2)
            >>> p.y
            2
            >>> p.y = 10
            >>> p.y
            10
        """
        return self._y

    @y.setter
    def y(self, value):
        """Set property for _y attribute.

        Args:
            value (int) : new value for the Y-axis coordinate attribute.
        """
        self._y = int(value)

    @property
    def klass(self):
        """Gets the class to be used for arithmetical operations.

        Returns:
            object : class for the Point instance.

        Example:
            >>> p = Point(1, 1)
            >>> p.klass     #doctest: +ELLIPSIS
            <class '...point.Point'>
        """
        return self.__class__

    def _is_positive(self, value):
        """Checks if the value passed is in the positive axe.

        Args:
            value (int) : value to check.

        Returns:
            bool : True is value is in the positive axe, False else.

        Example:
            >>> p = Point(0, 0)
            >>> p._is_positive(1)
            True
            >>> p._is_positive(-1)
            False
        """
        return value > 0

    def _is_negative(self, value):
        """Checks if the value passed is in the negative axe.

        Args:
            value (int) : value to check.

        Returns:
            bool : True is value is in the negative axe, False else.

        Example:k
            >>> p = Point(0, 0)
            >>> p._is_negative(1)
            False
            >>> p._is_negative(-1)
            True
        """
        return value < 0

    def _is_zero(self, value):
        """Checks if the value passed is in the axe origin.

        Args:
            value (int) : value to check.

        Returns:
            bool : True is value is in the axe origin, False else.

        Example:
            >>> p = Point(0, 0)
            >>> p._is_zero(0)
            True
            >>> p._is_zero(1)
            False
            >>> p._is_zero(-1)
            False
        """
        return value == 0

    def is_x_positive(self):
        """Check if the point is in the positive X-axe.

        Returns:
            bool : True if point is in the positive X-axe, False else.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_x_positive()
            True
            >>> p = Point(-1, 1)
            >>> p.is_x_positive()
            False
        """
        return self._is_positive(self.x)

    def is_x_negative(self):
        """Check if the point is in the negative X-axe.

        Returns:
            bool : True if point is in the negative X-axe, False else.

        Example:
            >>> p = Point(1, 0)
            >>> p.is_x_negative()
            False
            >>> p = Point(-1, 0)
            >>> p.is_x_negative()
            True
        """
        return self._is_negative(self.x)

    def is_x_zero(self):
        """Check if the point is the X-axe origin.

        Returns:
            bool : True if point is in the X-axe origin, False else.

        Example:
            >>> p = Point(0, 1)
            >>> p.is_x_zero()
            True
            >>> p = Point(1, 0)
            >>> p.is_x_zero()
            False
        """
        return self._is_zero(self.x)

    def is_y_positive(self):
        """Check if the point is in the positive Y-axe.

        Returns:
            bool : True if point is in the positive Y-axe, False else.

        Example:
            >>> p = Point(0, 1)
            >>> p.is_y_positive()
            True
            >>> p = Point(0, -1)
            >>> p.is_y_positive()
            False
        """
        return self._is_positive(self.y)

    def is_y_negative(self):
        """Check if the point is in the negative Y-axe.

        Returns:
            bool : True if point is in the negative Y-axe, False else.

        Example:
            >>> p = Point(0, 1)
            >>> p.is_y_negative()
            False
            >>> p = Point(0, -1)
            >>> p.is_y_negative()
            True
        """
        return self._is_negative(self.y)

    def is_y_zero(self):
        """Check if the point is the Y-axe origin.

        Returns:
            bool : True if point is in the Y-axe origin, False else.

        Example:
            >>> p = Point(1, 0)
            >>> p.is_y_zero()
            True
            >>> p = Point(0, 1)
            >>> p.is_y_zero()
            False
        """
        return self._is_zero(self.y)

    def __repr__(self):
        """String representation for the Point instance.

        Returns:
            str : string with the Point instance representation.

        Example:
            >>> str(Point(0, 0))
            '(0, 0)'
        """
        return '({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        """Overload method for the 'equal to' operation between Point
        instances.

        Two Point instances are equal if X and Y coordinates values are
        equal.

        Args:
            other (Point) : the other Point instance to check if is equal.

        Returns:
            bool : True if Point instaces are equal, False else.

        Example:
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
        if isinstance(other, Point):
            return self.is_x_eq(other) and self.is_y_eq(other)
        return NotImplemented

    def __neq__(self, other):
        """Overload method for the 'not equal to' operation between Point
        instances.

        Two Point instances are not equal if X or Y coordinates values are
        not equal.

        Args:
            other (Point) : the other Point instance to check if is not
            equal.

        Returns:
            bool : True if Point instaces are not equal, False else.

        Example:
            >>> Point(1, 1) != Point(1, 1)
            False
            >>> Point(1, 1) != Point(1, 0)
            True
            >>> Point(1, 1) != Point(0, 1)
            True
        """
        if isinstance(other, Point):
            return not self.__eq__(other)
        return NotImplemented

    def _is_greater(self, value, other):
        """Checks if one value is greater than other.

        Args:
            value (int) : value to check if greater than the second.
            other (int) : other value to check.

        Returns:
            bool : True if first value is greater.

        Example:
            >>> p = Point(1, 1)
            >>> p._is_greater(2, 1)
            True
            >>> p._is_greater(1, 2)
            False
            >>> p._is_greater(1, 1)
            False
        """
        return value > other

    def is_lower(self, value, other):
        """Checks if one value is lower than other

        Args:
            value (int) : value to check if lower than the second.
            other (int) : other value to check.

        Returns:
            bool : True if first value is lower.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_lower(2, 1)
            False
            >>> p.is_lower(1, 2)
            True
            >>> p.is_lower(1, 1)
            False
        """
        return value < other

    def _is_eq(self, value, other):
        """Checks if two values are equal.

        Args:
            value (int) : value to check if equal than the second.
            other (int) : other value to check.

        Returns:
            bool : True if first value is equal.

        Example:
            >>> p = Point(1, 1)
            >>> p._is_eq(2, 1)
            False
            >>> p._is_eq(1, 2)
            False
            >>> p._is_eq(1, 1)
            True
        """
        return value == other

    def is_y_greater(self, other):
        """Checks if point Y-coordinate is greater than the one from the
        given point.

        Args:
            other (Point) : other point to check if Y-coordinate is greater.

        Returns:
            bool : True if point Y-coordinate is greater than the given Point.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_y_greater(Point(0, 0))
            True
            >>> p.is_y_greater(Point(0, 2))
            False

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self._is_greater(self.y, other.y)
        raise NotImplementedError

    def is_y_lower(self, other):
        """Checks if point Y-coordinate is lower than the one from the
        given point.

        Args:
            other (Point) : other point to check if Y-coordinate is lower.

        Returns:
            bool : True if point Y-coordinate is lower than the given Point.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_y_lower(Point(0, 0))
            False
            >>> p.is_y_lower(Point(0, 2))
            True

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self.is_lower(self.y, other.y)
        raise NotImplementedError

    def is_y_eq(self, other):
        """Checks if point Y-coordinate is equal than the one from the
        given point.

        Args:
            other (Point) : other point to check if Y-coordinate is equal.

        Returns:
            bool : True if point Y-coordinate is equal than the given Point.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_y_eq(Point(0, 1))
            True
            >>> p.is_y_eq(Point(0, 0))
            False

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self._is_eq(self.y, other.y)
        raise NotImplementedError

    def is_x_greater(self, other):
        """Checks if point X-coordinate is greated than the one form the
        given point.

        Args:
            other (Point) : other point to check if X-coordinate is greater.

        Returns:
            bool : True if point X-coordinate is greater than the given Point.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_x_greater(Point(0, 0))
            True
            >>> p.is_x_greater(Point(2, 0))
            False

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self._is_greater(self.x, other.x)
        raise NotImplementedError

    def is_x_lower(self, other):
        """Checks if point X-coordinate is lower than the one form the
        given point.

        Args:
            other (Point) : other point to check if X-coordinate is lower.

        Returns:
            bool : True if point X-coordinate is lower than the given Point.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_x_lower(Point(0, 0))
            False
            >>> p.is_x_lower(Point(2, 0))
            True

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self.is_lower(self.x, other.x)
        raise NotImplementedError

    def is_x_eq(self, other):
        """Checks if point X-coordinate is equal than the one form the
        given point.

        Args:
            other (Point) : other point to check if X-coordinate is equal.

        Returns:
            bool : True if point X-coordinate is equal than the given Point.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_x_eq(Point(0, 0))
            False
            >>> p.is_x_eq(Point(1, 0))
            True

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self._is_eq(self.x, other.x)
        raise NotImplementedError

    def __add__(self, other):
        """Overload addition operation between two Point instances.

        Args:
            other (Point) : the other point for the addition.

        Returns:
            Point : new Point with both Point addition.

        Example:
            >>> p = Point(1, 1)
            >>> p + Point(1, 2)
            (2, 3)
            >>> Point(3, 5) + p
            (4, 6)
        """
        if isinstance(other, Point):
            return self.klass(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Overload substract operation between two Point instances.

        Args:
            other (Point) : the other point for the substraction.

        Returns:
            Point : new Point with both Point substraction.

        Example:
            >>> p = Point(1, 1)
            >>> p - Point(2, 0)
            (-1, 1)
            >>> Point(10, 10) - p
            (9, 9)
        """
        if isinstance(other, Point):
            return self.klass(self.x - other.x, self.y - other.y)
        return NotImplemented

    def distance(self, other):
        """Returns the distance between the point and the given point.

        Args:
            other (Point) : second point to check the distance.

        Returns:
            float : distance between two points.

        Example:
            >>> p = Point(0, 0)
            >>> p.distance(Point(2, 2))
            2.8284271247461903

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return math.hypot(other.x - self.x, other.y - self.y)
        raise NotImplementedError

    def distance_as_int(self, other):
        """Returns the distance between the point and the given point as an
        integer value.

        Args:
            other (Point) : second point to check the distance.

        Returns:
            int : distance between two points.

        Example:
            >>> p = Point(0, 0)
            >>> p.distance_as_int(Point(2, 2))
            2

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return int(self.distance(other))
        raise NotImplementedError

    def distannce_as_point(self, other):
        """Returns the distance between the point and the given point as a
        Point instance.

        Args:
            other (Point) : second point to check the distance.

        Returns:
            Point : distance between two points as a Point.

        Example:
            >>> p = Point(1, 1)
            >>> p.distannce_as_point(Point(2, 3))
            (1, 2)

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return other - self
        raise NotImplementedError

    def _distance(self, attr, other):
        """Retuns the distance (difference) between two values.

        Args:
            attr (Point) : first instance for checking distance.
            other (Point) : second instance for checking distance.

        Returns:
            Point : distance between both instances.
        """
        return attr - other

    def x_distance(self, other):
        """Returns the X-coordinate distance between two points.

        Args:
            other (Point) : X-coordinate distance will be returned to this Point.

        Returns:
            Point : new Point instance with the X-coord distance.

        Example:
            >>> p = Point(1, 1)
            >>> p.x_distance(Point(2, 1))
            1

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self._distance(other.x, self.x)
        raise NotImplementedError

    def y_distance(self, other):
        """Returns the Y-coordinate distance between two points.

        Args:
            other (Point) : Y-coordinate distance will be returned to this Point.

        Returns:
            Point : new Point instance with the Y-coord distance.

        Example:
            >>> p = Point(1, 1)
            >>> p.y_distance(Point(2, 1))
            0

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self._distance(other.y, self.y)
        raise NotImplementedError

    def translate(self, other):
        """Returns a new translated point by the given point.

        It basically moves the point adding X-coordinates and Y-coordinates.

        Args:
            other (Point) : other point used for translation.

        Returns:
            Point : New  point with the translation.

        Example:
            >>> p = Point(1, 1)
            >>> p.translate(Point(2, 3))
            (3, 4)

        Raises:
            NotImplementedError
        """
        if isinstance(other, Point):
            return self + other
        raise NotImplementedError

    def x_translate(self, x):
        """Returns a new translated point by the given X-coordinate.

        Args:
            x (int) : X-coordinate value to translate.

        Returns:
            Point : New Point with the translation.

        Example:
            >>> p = Point(0, 0)
            >>> p.x_translate(10)
            (10, 0)
        """
        return self + self.klass(int(x), 0)

    def y_translate(self, y):
        """Returns a new translated point by the given Y-coordinate.

        Args:
            y (int) : Y-coordinate value to translate.

        Returns:
            Point : New Point with the translation.

        Example:
            >>> p = Point(0, 0)
            >>> p.y_translate(5)
            (0, 5)
        """
        return self + self.klass(0, int(y))

    def xy_translate(self, x, y):
        """Returns a new translated point by the given X-coordinate and
        Y-coordinate.

        Args:
            x (int) : X-coordinate value to translate.
            y (int) : Y-coordinate value to translate.

        Returns:
            Point : New Point with the translation.

        Example:
            >>> p = Point(0, 0)
            >>> p.xy_translate(1, 5)
            (1, 5)
        """
        return self + self.klass(int(x), int(y))

    def _move(self, attr, value):
        """Add a value to other. Used in move operations.

        This methow allows to make generic operations on X-axis and Y-axis.

        Args:
            attr (int) : first attribute to be moved.
            value (int) : value to move the attribute

        Returns:
            int : result of the movement.
        """
        return attr + int(value)

    def x_move(self, x=1):
        """Updates X-coordinate a given value.

        Args:
            x (int) : distance to move the X-coordinate (Default=1)

        Returns:
            Point : self point moved the given X-coordinate distance.

        Example:
            >>> p = Point(1, 1)
            >>> p.x_move(1)
            (2, 1)
            >>> p.x_move()
            (3, 1)
            >>> p.x_move(2).x_move()
            (6, 1)
        """
        self.x = self._move(self.x, x)
        return self

    def y_move(self, y=1):
        """Updates Y-coordinate a given value.

        Args:
            x (int) : distance to move the Y-coordinate (Default=1)

        Returns:
            Point : self point moved the given Y-coordinate distance.

        Example:
            >>> p = Point(1, 1)
            >>> p.y_move(1)
            (1, 2)
            >>> p.y_move()
            (1, 3)
            >>> p.y_move(2).y_move()
            (1, 6)
        """
        self.y = self._move(self.y, y)
        return self

    def xy_move(self, x=1, y=1):
        """Updates X-coordinate and Y-coordinates with given values.

        Args:
            x (int) : distance to move the Y-coordinate (Default=1)
            y (int) : distance to move the Y-coordinate (Default=1)

        Returns:
            Point : self point moved the given X-coordinate and\
            Y-coordinate distance.

        Example:
            >>> p = Point(1, 1)
            >>> p.xy_move(1, 1)
            (2, 2)
            >>> p.xy_move(1).xy_move(0, 2).xy_move()
            (4, 6)
        """
        self.x_move(x)
        self.y_move(y)
        return self

    def _move_within_range(self, attr, range_, value, upto_flag):
        """Move a coordinate a given value but only in the given range.

        This method is used to make generic X-axis and Y-axis operations.

        Args:
            attr (int) : attribute to move.

            range_ (Range) : range values the X-coordinate can move.

            value (int) : value to increase.

            upto_flag (bool) : when flag is True the movement is the closest\
            to the final position. False means the movement is not done if it\
            is out of range.

        Returns:
            int : attribute value already moved.
        """
        value = attr + int(value)
        if range_.get_min() <= value <= range_.get_max():
            attr = value
        elif upto_flag and range_.get_min() > value:
            attr = range_.get_min()
        elif upto_flag and range_.get_max() < value:
            attr = range_.get_max()
        return attr

    def x_move_within_range(self, range_, x=1, upto_flag=False):
        """Updates X-coordinate a given value but only in the given ranges.

        Args:
            range_ (Range) : range values the X-coordinate can move.

            x (int) : value to increase the X-coordinate (default = 1).

            upto_flag (bool) : when flag is True the movement is the closest\
            to the final position. False means the movement is not done if it\
            is out of range.

        Returns:
            Point : Point instace after the X-coordinate movement.

        Example:
            >>> p = Point(1, 1)
            >>> p.x_move_within_range(Range(0, 10))
            (2, 1)
            >>> p.x_move_within_range(Range(0, 10), 5)
            (7, 1)
            >>> p.x_move_within_range(Range(0, 10), 5)
            (7, 1)
            >>> p.x_move_within_range(Range(0, 10), 5, True)
            (10, 1)

        Raises:
            NotImplementedError
        """
        if isinstance(range_, Range):
            self.x = self._move_within_range(self.x, range_, x, upto_flag)
            return self
        else:
            raise NotImplementedError

    def y_move_within_range(self, range_, y=1, upto_flag=False):
        """Updates Y-coordinate a given value but only in the given ranges.

        Args:
            range_ (Range) : range values the Y-coordinate can move.

            y (int) : value to increase the Y-coordinate (default = 1).

            upto_flag (bool) : when flag is True the movement is the closest\
            to the final position. False means the movement is not done if it\
            is out of range.

        Returns:
            Point : Point instace after the Y-coordinate movement.

        Example:
            >>> p = Point(1, 1)
            >>> p.y_move_within_range(Range(0, 10))
            (1, 2)
            >>> p.y_move_within_range(Range(0, 10), 2)
            (1, 4)
            >>> p.y_move_within_range(Range(0, 10), 10)
            (1, 4)
            >>> p.y_move_within_range(Range(0, 10), 10, True)
            (1, 10)

        Raises:
            NotImplementedError
        """
        if isinstance(range_, Range):
            self.y = self._move_within_range(self.y, range_, y, upto_flag)
            return self
        else:
            raise NotImplementedError

    def xy_move_within_range(self, x_range, y_range, x=1, y=1, upto_flag=False):
        """Updates X-coordiante and Y-coordinate a given value but only in the
        given ranges.

        Args:
            x_range (Range) : range values the X-coordinate can move.
            y_range (Range) : range values the Y-coordinate can move.

            x (int) : value to increase the X-coordinate (default = 1).
            y (int) : value to increase the Y-coordinate (default = 1).

            upto_flag (bool) : when flag is True the movement is the closest\
            to the final position. False means the movement is not done if it\
            is out of range.

        Returns:
            Point : Point instace after the Y-coordinate movement.

        Example:
            >>> p = Point(1, 1)
            >>> p.xy_move_within_range(Range(0, 10), Range(0, 7))
            (2, 2)
            >>> p.xy_move_within_range(Range(0, 10), Range(0, 7), 2, 1)
            (4, 3)
            >>> p.xy_move_within_range(Range(0, 10), Range(0, 7), 1, 5)
            (5, 3)
            >>> p.xy_move_within_range(Range(0, 10), Range(0, 7), 10, 1)
            (5, 4)
            >>> p.xy_move_within_range(Range(0, 10), Range(0, 7), 10, 10, True)
            (10, 7)

        Raises:
            NotImplementedError
        """
        if isinstance(x_range, Range) and isinstance(y_range, Range):
            self.x_move_within_range(x_range, x, upto_flag)
            self.y_move_within_range(y_range, y, upto_flag)
            return self
        else:
            raise NotImplementedError

    def _move_with_collision(self, attr_name, collisions, value, range_, upto_flag):
        """Generic method that moves positional attribute X or Y to a given
        position.

        Method checks against a list of possible positions and a range with
        the minimum and maximum values.

        There is a flag that is used to move to the closest position to
        destination or just don't move at all.

        Args:
            attr_name (str) : String with the name of the positional\
            attribute to update. It could be 'x' or 'y'.

            collisions (List[Point]) : list or tuple of Points with\
            possible collisions. These points will block the movement.

            value (int) : movement value.

            range_ (Range) : range instance with the minimum and\
            maximum final position values.

            upto_flag (bool) : boolean that flags if returning initial\
            position if the final one is not possible if False, or\
            move to the closest position to the destination if True.

        Returns:
            Point : point instance with the final movement position.

        Raises:
            NotImplementedError
        """
        if type(collisions) in (list, tuple) and collisions:
            # Keep the initial attribute value, just is case we have to roll
            # over it, if it can not move to the final position.
            backup_value = getattr(self, attr_name)
            # Get the final position, so it is checked against the range of
            # possible values. If the result is out of limits, check if should
            # move up to the closest position or not. If we can not move up to
            # the closest, return the initial position.
            move_value = self._move(backup_value, value)
            if range_:
                limit = value if range_.get_min() <= move_value < range_.get_max() else None
                if limit is None and upto_flag:
                    if range_.get_min() > move_value:
                        limit = backup_value - range_.get_min()
                    elif range_.get_max() < move_value:
                        limit = range_.get_max() - backup_value
                elif limit is None and not upto_flag:
                    return self
            else:
                limit = value
            # Move one step at a time, until a collision is found, at that time
            # back down one position is up to close is defined or return the
            # original value if not.
            for inc in range(limit):
                setattr(self, attr_name, self._move(getattr(self, attr_name), 1))
                for p in collisions:
                    if self == p:
                        if upto_flag:
                            setattr(self, attr_name, self._move(getattr(self, attr_name), -1))
                        else:
                            setattr(self, attr_name, backup_value)
                        return self
            return self
        else:
            raise NotImplementedError

    def x_move_with_collision(self, collisions, x=1, x_range=None, upto_flag=False):
        """Updates X-coordinate a given value in the given range and avoiding any
        collision with given Point instances.

        Args:
            collisions (list[Point]) : list or tuple of Points with\
            possible collisions. These points will block the movement.

            x (int) : x-coordinate movement value.

            x_range (Range) : range instance with the minimum and\
            maximum final position values.

            upto_flag (bool) : boolean that flags if returning initial\
            position if the final one is not possible if False, or\
            move to the closest position to the destination if True.

        Returns:

            Point : point instance with the final movement position.

        Example:
            >>> p = Point(1, 1)
            >>> p.x_move_with_collision([Point(0, 0)])
            (2, 1)
            >>> p.x_move_with_collision([Point(0, 0)], 2)
            (4, 1)
            >>> p.x_move_with_collision([Point(0, 0), Point(6, 1)], 2)
            (4, 1)
            >>> p.x_move_with_collision([Point(0, 0), Point(6, 1)], 2, None, True)
            (5, 1)
            >>> p.x_move_with_collision([Point(0, 0), Point(9, 1), Point(10, 1)], 5, None, True)
            (8, 1)
            >>> p.x_move_with_collision([Point(0, 0)], 10, Range(0, 10))
            (8, 1)
            >>> p.x_move_with_collision([Point(0, 0)], 10, Range(0, 10), True)
            (10, 1)
        """
        return self._move_with_collision('x', collisions, x, x_range, upto_flag)

    def y_move_with_collision(self, collisions, y=1, y_range=None, upto_flag=False):
        """Updates Y-coordinate a given value in the given range and avoiding any
        collision with given Point instances.

        Args:
            collisions (list[Point]) : list or tuple of Points with\
            possible collisions. These points will block the movement.

            x (int) : Y-coordinate movement value.

            x_range (Range) : range instance with the minimum and\
            maximum final position values.

            upto_flag (bool) : boolean that flags if returning initial\
            position if the final one is not possible if False, or\
            move to the closest position to the destination if True.

        Returns:

            Point : point instance with the final movement position.

        Example:
            >>> p = Point(1, 1)
            >>> p.y_move_with_collision([Point(0, 0)])
            (1, 2)
            >>> p.y_move_with_collision([Point(0, 0)], 2)
            (1, 4)
            >>> p.y_move_with_collision([Point(0, 0), Point(1, 6)], 2)
            (1, 4)
            >>> p.y_move_with_collision([Point(0, 0), Point(1, 6)], 2, None, True)
            (1, 5)
            >>> p.y_move_with_collision([Point(0, 0), Point(1, 9), Point(1, 10)], 5, None, True)
            (1, 8)
            >>> p.y_move_with_collision([Point(0, 0)], 10, Range(0, 10))
            (1, 8)
            >>> p.y_move_with_collision([Point(0, 0)], 10, Range(0, 10), True)
            (1, 10)
        """
        return self._move_with_collision('y', collisions, y, y_range, upto_flag)

    def _is_valid_move(self, attr_name, collisions, value, range_):
        """Generic method that checks in the positional movement is a valid one
        without collisions.

        Method checks against a list of possible positions and a range with
        the minimum and maximum values.

        Args:
            attr_name (str) : String with the name of the positional\
            attribute to update. It could be 'x' or 'y'.

            collisions (list[Point]) : list or tuple of Points with\
            possible collisions. These points will block the movement.

            value (int) : movement value.

            range_ (Range) : range instance with the minimum and\
            maximum final position values.

        Returns:
            bool : True if movement is possible, False else

        Raises:
            NotImplementedError
        """
        trav = Point(self.x, self.y)
        if type(collisions) in (list, tuple) and collisions:
            move_value = trav._move(getattr(trav, attr_name), value)
            if range_:
                limit = value if range_.get_min() <= move_value < range_.get_max() else None
                if limit is None:
                    return False
            else:
                limit = value
            # Move one step at a time, until a collision is found.
            for inc in range(limit):
                setattr(trav, attr_name, trav._move(getattr(trav, attr_name), 1))
                for p in collisions:
                    if trav == p:
                        return False
            return True
        else:
            raise NotImplementedError

    def x_is_valid_move(self, collisions, x=1, x_range=None):
        """Check if X-coordinate movement is valid.

        Args:
            collisions (list[Point]) : list or tuple of Points with\
            possible collisions. These points will block the movement.

            x (int) : x-coordinate movement value.

            x_range (Range) : range instance with the minimum and\
            maximum final position values.

        Returns:

            bool : True if movement is possible, False else

        Example:
            >>> p = Point(1, 1)
            >>> p.x_is_valid_move([Point(0, 0)])
            True
            >>> p.x_is_valid_move([Point(0, 0)], 2)
            True
            >>> p.x_is_valid_move([Point(0, 0), Point(6, 1)], 2)
            True
            >>> p.x_is_valid_move([Point(0, 0), Point(6, 1)], 6)
            False
            >>> p.x_is_valid_move([Point(0, 0), Point(6, 1)], 2, None)
            True
            >>> p.x_is_valid_move([Point(0, 0), Point(6, 1)], 7, None)
            False
            >>> p.x_is_valid_move([Point(0, 0)], 10, Range(0, 10))
            False
        """
        return self._is_valid_move('x', collisions, x, x_range)

    def y_is_valid_move(self, collisions, y=1, y_range=None):
        """Check if Y-coordinate movement is valid.

        Args:
            collisions (list[Point]) : list or tuple of Points with\
            possible collisions. These points will block the movement.

            y (int) : Y-coordinate movement value.

            y_range (Range) : range instance with the minimum and\
            maximum final position values.

        Returns:

            bool : True if movement is possible, False else

        Example:
            >>> p = Point(1, 1)
            >>> p.y_is_valid_move([Point(0, 0)])
            True
            >>> p.y_is_valid_move([Point(0, 0)], 2)
            True
            >>> p.y_is_valid_move([Point(0, 0), Point(1, 6)], 2)
            True
            >>> p.y_is_valid_move([Point(0, 0), Point(1, 6)], 6)
            False
            >>> p.y_is_valid_move([Point(0, 0), Point(1, 6)], 2, None)
            True
            >>> p.y_is_valid_move([Point(0, 0), Point(1, 6)], 7, None)
            False
            >>> p.y_is_valid_move([Point(0, 0)], 10, Range(0, 10))
            False
        """
        return self._is_valid_move('y', collisions, y, y_range)

    def is_collision(self, trans_point, collisions):
        """Checks if the point translated with the given Point has any
        collision.

        Args:
            trans_point (Point) : translation point

            collisions (list[Point]) : list or tuple of Points with\
            possible collisions. These points will block the movement.

        Returns:
            bool : True if there is any collision, False else.

        Example:
            >>> p = Point(1, 1)
            >>> p.is_collision(Point(1, 1), [Point(0, 0)])
            False
            >>> p.is_collision(Point(1, 1), [Point(2, 2)])
            True
            >>> p.is_collision(Point(1, 1), [Point(1, 0), Point(2, 2)])
            True
        """
        new_point = self.translate(trans_point)
        for p in collisions:
            if new_point == p:
                return True
        return False

class Range(object):
    """Range class provides a container for range, where a minimum and a
    maximum value.
    """

    def __init__(self, theMin, theMax):
        """Range class initialization method.

        Args:
            theMin (int) : minimum value for the range.
            theMax (int) : maximum value for the range.
        """
        self._min = int(theMin)
        self._max = int(theMax)

    @property
    def Min(self):
        """Property that returns the _min attribute.

        Returns:
            int : minimum range attribute.
        """
        return self._min

    @Min.setter
    def Min(self, theValue):
        """Property that sets a new value for the _min attribute.

        Args:
            theValue (int) : new minimum range attribute.
        """
        self._min = int(theValue)

    @property
    def Max(self):
        """Property that returns the _max attribute.

        Returns:
            int : maximum range attribute.
        """
        return self._max

    @Max.setter
    def Max(self, theValue):
        """Property that sets a new value for the _max attribute.

        Args:
            theValue (int) : new maximum range attribute.
        """
        self._max = int(theValue)

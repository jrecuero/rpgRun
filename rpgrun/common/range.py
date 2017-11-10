class Range(object):
    """Range class provides a container for range, where a minimum and a
    maximum value.
    """

    def __init__(self, minimun, maximun):
        """Range class initialization method.

        Args:
            minimun (int) : minimum value for the range.
            maximun (int) : maximum value for the range.
        """
        self._min = int(minimun)
        self._max = int(maximun)

    def get_min(self):
        """Property that returns the _min attribute.

        Returns:
            int : minimum range attribute.
        """
        return self._min

    def get_max(self):
        """Property that returns the _max attribute.

        Returns:
            int : maximum range attribute.
        """
        return self._max

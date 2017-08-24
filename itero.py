from collections.abc import Iterator


class Itero(Iterator):

    def __init__(self, theStreamKlass, theMaxLen=None):
        assert theStreamKlass
        self.__streamKlass = theStreamKlass
        self.__index = 0
        self.__stream = []
        self.__maxLen = theMaxLen

    @property
    def MaxLen(self):
        return self.__maxLen

    def __getitem__(self, theKey):
        """
        >>> it = Itero(str)
        >>> it.append('one')
        >>> it[0]
        'one'
        """
        assert theKey < len(self.__stream)
        return self.__stream[theKey]

    def __setitem__(self, theKey, theValue):
        """
        >>> it = Itero(str)
        >>> it.append('one')
        >>> it[0]
        'one'
        >>> it[0] = 'ONE'
        >>> it[0]
        'ONE'
        """
        assert theKey < len(self.__stream)
        assert isinstance(theValue, self.__streamKlass)
        self.__stream[theKey] = theValue

    def __delitem__(self, theKey):
        """
        >>> it = Itero(str)
        >>> it.append('one')
        >>> it.append('two')
        >>> len(it)
        2
        >>> del it[0]
        >>> len(it)
        1
        """
        assert theKey < len(self.__stream)
        del self.__stream[theKey]

    def __iter__(self):
        """
            >>> it = Itero(str)
            >>> for x in ['one', 'two', 'three', 'four', 'five']:
            ...     it.append(x)
            >>> it[0], it[1], it[2], it[3], it[4]
            ('one', 'two', 'three', 'four', 'five')
            >>> for i, v in enumerate(it):
            ...     it[i] = v.upper()
            >>> for x in it:
            ...     print(x)
            ONE
            TWO
            THREE
            FOUR
            FIVE
        """
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__stream):
            self.__index = 0
            raise StopIteration
        _ = self.__stream[self.__index]
        self.__index += 1
        return _

    def __len__(self):
        """
            >>> it = Itero(str)
            >>> len(it)
            0
            >>> it.append('one')
            >>> len(it)
            1
        """
        return len(self.__stream)

    def append(self, theValue):
        """
        >>> it = Itero(str, 2)
        >>> it.append('one')
        >>> it[0]
        'one'
        >>> it.append('two')
        >>> it[1]
        'two'
        >>> try:
        ...     it.append('three')
        ... except NotImplementedError:
        ...     print('NotImplemented')
        NotImplemented
        """
        if self.MaxLen is not None and len(self.__stream) >= self.MaxLen:
            raise NotImplementedError
        assert isinstance(theValue, self.__streamKlass)
        self.__stream.append(theValue)

    def pop(self):
        """
        >>> it = Itero(str)
        >>> it.append('one')
        >>> it.pop()
        'one'
        """
        return self.__stream.pop()

    def remove(self, theValue):
        """
        >>> it = Itero(str, 2)
        >>> it.append('one')
        >>> it.append('two')
        >>> it.remove('one')
        >>> try:
        ...     it.remove('one')
        ... except ValueError:
        ...     print('ValueError')
        ValueError
        """
        assert isinstance(theValue, self.__streamKlass)
        self.__stream.remove(theValue)

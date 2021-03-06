from collections.abc import Iterator
from collections import OrderedDict


class Itero(Iterator):
    """Itero Class derives from :class:`collections.abc.Iterator` and it  implements a generic
    iterator to be used.
    """

    def __init__(self, stream_class, maxlen=None):
        """Itero class initialization method.

        Args:
            stream_class (class) : class used for every entry.

            maxlen (int) : maximum storage size.
        """
        assert stream_class
        self.__stream_class = stream_class
        self.__index = 0
        self.__stream = []
        self.__maxlen = maxlen

    @property
    def maxlen(self):
        """Gets __maxlen attribute value.

        Returns:
            int : maximum storage size.

        Example:
            >>> it = Itero(str, 10)
            >>> it.maxlen
            10
        """
        return self.__maxlen

    @property
    def stream(self):
        """
        """
        return self.__stream

    def __getitem__(self, key):
        """Allows retriving data using indexed values for the instance.

        Args:
            key (int) : Integer to be used a indexed key.

        Returns:
            object : Instace stored in the given indexed key.

        Example:
            >>> it = Itero(str)
            >>> it.append('one')
            >>> it[0]
            'one'
        """
        assert key < len(self.__stream)
        return self.__stream[key]

    def __setitem__(self, key, value):
        """Allows updating data using indexed values for the instance.

        Args:
            key (int) : Integer to be used as indexed key.

            value (object) : Instance to be stored at the given indexed key.

        Example:
            >>> it = Itero(str)
            >>> it.append('one')
            >>> it[0]
            'one'
            >>> it[0] = 'ONE'
            >>> it[0]
            'ONE'
        """
        assert key < len(self.__stream)
        self.__stream[key] = value

    def __delitem__(self, key):
        """Allows deleting data using indexed values for the instance.

        Args:
            key (int) : Integer to be used as indexed key.

        Example:
            >>> it = Itero(str)
            >>> it.append('one')
            >>> it.append('two')
            >>> len(it)
            2
            >>> del it[0]
            >>> len(it)
            1
        """
        assert key < len(self.__stream)
        del self.__stream[key]

    def __iter__(self):
        """Allows iterating the instance (initialize the iteration).

        Returns:
            Itero : Returns itself instance.

        Example:
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
        """Allows iteratinf the instace (next instance in the iteration).

        Returns:
            object : Next entry stored to be used in a generator.
        """
        if self.__index >= len(self.__stream):
            self.__index = 0
            raise StopIteration
        _ = self.__stream[self.__index]
        self.__index += 1
        return _

    def __len__(self):
        """Retrieves the lenght for the instance.

        Returns:
            int : Storage size.

        Example:
            >>> it = Itero(str)
            >>> len(it)
            0
            >>> it.append('one')
            >>> len(it)
            1
        """
        return len(self.__stream)

    def append(self, value):
        """Appends a value to the instance at the end.

        Args:
            value (object) : Instance to be stored at the end.

        Example:
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
        if self.maxlen is not None and len(self) >= self.maxlen:
            raise NotImplementedError
        self.__stream.append(value)

    def extend(self, theList):
        """Extends with the given list.

        Args:
            theList (list) : List to be added.

        Example:
            >>> it = Itero(str)
            >>> it.append('one')
            >>> it.extend(['two', 'three'])
            >>> for x in it:
            ...     print(x)
            one
            two
            three
        """
        if self.maxlen is not None and len(self) + len(theList) >= self.maxlen:
            raise NotImplementedError
        if type(theList) in [list, tuple]:
            _list = theList
        elif isinstance(theList, self.__class__):
            _list = self._Itero__stream
        else:
            raise NotImplementedError
        self.__stream.extend(_list)

    def pop(self):
        """Retrieves and removes the last value from the instance.

        Returns:
            object : Last entry in the storage.

        Example:
            >>> it = Itero(str)
            >>> it.append('one')
            >>> it.pop()
            'one'
        """
        return self.__stream.pop()

    def remove(self, value):
        """Removes the given value from the instance.

        Args:
            value (object) : Instance to be removed from the storage.

        Returns:
            bool : True if removed properly, False else.

        Example:
            >>> it = Itero(str, 2)
            >>> it.append('one')
            >>> it.append('two')
            >>> it.remove('one')
            True
            >>> it.remove('one')
            False
        """
        try:
            index = self.__stream.index(value)
            del self[index]
            return True
        except ValueError:
            return False


class StrItero(Iterator):
    """DictItero Class derives from :class:`collections.abc.Iterator` and it implements a generic
    iterator where indexes are strings instead of integers.
    """

    def __init__(self, stream_class, theProcessKey=None):
        """StrItero class initialization method.

        Args:
            stream_class (class) : class used for every entry.

            maxlen (int) : maximum storage size.
        """
        assert stream_class
        self.__stream_class = stream_class
        self.__index = 0
        self.__stream = OrderedDict()
        self.__processKey = theProcessKey

    def __getitem__(self, key):
        """Allows retriving data using indexed values for the instance.

        Args:
            key (str) : String to be used a indexed key.

        Returns:
            object : Instace stored in the given indexed key.

        Example:
            >>> it = StrItero(int)
            >>> it.update('one', 1)
            >>> it['one']
            1
        """
        assert isinstance(key, str)
        key_ = self.__processKey(key) if self.__processKey else key
        return OrderedDict.__getitem__(self.__stream, key_)

    def __setitem__(self, key, value):
        """Allows updating data using indexed values for the instance.

        Args:
            thekey (str) : String to be used as indexed key.

            value (object) : Instance to be stored at the given indexed key.

        Example:
            >>> it = StrItero(int)
            >>> it['two'] = 2
            >>> it['two']
            2
        """
        assert isinstance(key, str)
        key_ = self.__processKey(key) if self.__processKey else key
        OrderedDict.__setitem__(self.__stream, key_, value)

    def __delitem__(self, key):
        """Allows deleting data using indexed values for the instance.

        Args:
            thekey (str) : String to be used as indexed key.

        Example:
            >>> it = StrItero(int)
            >>> it['one'] = 1
            >>> it['two'] = 2
            >>> len(it)
            2
            >>> del it['one']
            >>> len(it)
            1
        """
        assert isinstance(key, str)
        key_ = self.__processKey(key) if self.__processKey else key
        OrderedDict.__delitem__(self.__stream, key_)

    def __iter__(self):
        """Allows iterating the instance (initialize the iteration).

        Returns:
            Itero : Returns itself instance.

        Example:
            >>> it = StrItero(int)
            >>> for i, v in enumerate(['zero', 'one', 'two']):
            ...     it[v] = i
            >>> it['zero'], it['one'], it['two']
            (0, 1, 2)
            >>> for x in it:
            ...     x
            0
            1
            2
        """
        self.__index = 0
        self.__streamAsList = [_ for _ in self.__stream.values()]
        return self

    def __next__(self):
        """Allows iteratinf the instace (next instance in the iteration).
        """
        if self.__index >= len(self.__streamAsList):
            self.__index = 0
            raise StopIteration
        _ = self.__streamAsList[self.__index]
        self.__index += 1
        return _

    def __len__(self):
        """Retrieves the lenght for the instance.

        Returns:
            int : Storage size.

        Example:
            >>> it = StrItero(int)
            >>> it['one'] = 1
            >>> it['two'] = 2
            >>> len(it)
            2
        """
        return len(self.__stream)

    def __contains__(self, theOtherKey):
        """Checks if the given value is in the instance.

        Args:
            theOtherKey (str) : String with other key to be checked if is\
                    contained in the storage.

        Example:
            >>> it = StrItero(int)
            >>> for i, v in enumerate(['zero', 'one', 'two']):
            ...     it[v] = i
            >>> 'one' in it
            True
            >>> 'three' in it
            False
        """
        other = self.__processKey(theOtherKey) if self.__processKey else theOtherKey
        return other in self.__stream

    def items(self):
        """Returns all key-value pairs for the instance.

        Returns:
            list : List with all key-value pairs stored.

        Example:
            >>> it = StrItero(int)
            >>> for i, v in enumerate(['zero', 'one', 'two']):
            ...     it[v] = i
            >>> for k, v in it.items():
            ...     k, v
            ('zero', 0)
            ('one', 1)
            ('two', 2)
        """
        return self.__stream.items()

    def update(self, key, value):
        """Updates the instance with the given key-value pairs.

        Args:
            thekey (str) : String to be used as indexed key.

            value (object) : Instance to be stored.

        Example:
            >>> it = StrItero(int)
            >>> it.update('one', 1)
            >>> it['one']
            1
        """
        assert isinstance(key, str)
        key_ = self.__processKey(key) if self.__processKey else key
        OrderedDict.update(self.__stream, {key_: value})

    def pop(self):
        """Retrieves and removes the last value from the instance.

        It is not implemented for a OrdDictionary without any parameters.

        Raise:
            NotImplementedError
        """
        raise NotImplementedError

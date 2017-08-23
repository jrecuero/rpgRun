from collections.abc import Iterator


class Itero(Iterator):

    def __init__(self, theStreamKlass):
        assert theStreamKlass
        self.__streamKlass = theStreamKlass
        self.__index = 0
        self.__stream = []

    def __getitem__(self, theKey):
        assert theKey < len(self.__stream)
        return self.__stream[theKey]

    def __setitem__(self, theKey, theValue):
        assert theKey < len(self.__stream)
        assert type(theValue) == self.__streamKlass
        self.__stream[theKey] = theValue

    def __delitem(self, theKey):
        assert theKey < len(self.__stream)
        del self.__stream[theKey]

    def __iter__(self):
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
        return len(self.__stream)

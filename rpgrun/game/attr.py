import json
from rpgrun.common.itero import StrItero


class Attr(object):
    """Attr Class contains all data related with a board object attribute.
    """

    def __init__(self, name):
        """Attr class initialization method.
        """
        self.name = name
        self.desc = ''
        self.base = 0
        self.__now = 0
        self.delta = 0
        self.buffs = {}

    @classmethod
    def create_attr(cls, attr_data):
        """Create an attribute from the passed data.

        Attribute data passed is a list with this format:

            * :class:`str` with attribute name. Index is 0.

            * :class:`int` with attribute base value. Index is 1.

            * :class:`int` with attribute delta value. Index is 2

            * :class:`dict` with buff name and buff values. Index is 3.

        Last entry with  buffs can be repeated as many times as required.

        Args:
            attr_data (:class:`list`) : Attribute parameters

        Returns:
            Attr : New attribute instance.
        """
        assert type(attr_data) in [list, tuple]
        assert len(attr_data) >= 3, attr_data
        assert len(attr_data) <= 4, attr_data
        attr_name = attr_data[0]
        attr_base = attr_data[1]
        attr_delta = attr_data[2]
        attr_buff = attr_data[3] if len(attr_data) == 4 else None
        attr = cls(attr_name)
        attr.setup_attr(attr_base, attr_delta, attr_buff)
        return attr

    @property
    def now(self):
        """Gets now value which is function of Base, Buffs and __now attributes.

        >>> at = Attr('old')
        >>> at.base = 5
        >>> at.now
        5
        """
        return self.base + sum(self.buffs.values()) + self.__now

    def dec(self, value):
        """Decrements __now attribute a given value.

        >>> at = Attr('new')
        >>> at.base = 10
        >>> at.dec(1)
        >>> at.now
        9
        """
        self.__now -= value

    def inc(self, value):
        """Increments __now attribute a given value.

        >>> at = Attr('new')
        >>> at.base = 10
        >>> at.inc(2)
        >>> at.now
        12
        """
        self.__now += value

    def add_buff(self, name, value):
        """Adds a new value to Buffs attribute.

        >>> at = Attr('old')
        >>> at.add_buff('st', 5)
        True
        >>> at.add_buff('dx', 3)
        True
        >>> at.buffs
        {'st': 5, 'dx': 3}
        >>> at.now
        8
        """
        self.buffs.update({name: value})
        return True

    def del_buff(self, name):
        """Deletes a value from Buffs attribute.

        >>> at = Attr('old')
        >>> at.add_buff('st', 5)
        True
        >>> at.add_buff('dx', 3)
        True
        >>> at.buffs
        {'st': 5, 'dx': 3}
        >>> at.del_buff('st')
        True
        >>> at.buffs
        {'dx': 3}
        """
        del self.buffs[name]
        return True

    def level_up(self, level_val=1):
        """Levels up the attribute a given number of times.

        For every level the Base value in incremented a delta value.

        >>> at = Attr('old')
        >>> at.base = 10
        >>> at.delta = 2
        >>> at.base
        10
        >>> at.level_up()
        >>> at.base
        12
        >>> at.level_up(3)
        >>> at.base
        18
        """
        for _ in range(abs(level_val)):
            self.base += self.delta * int(level_val / abs(level_val))

    def setup_attr(self, base=None, delta=None, buffs=None):
        """Setups instance with given base, delta and buffs values.

        >>> at = Attr('new')
        >>> at, at.delta, at.buffs
        (new: 0/0, 0, {})
        >>> at.setup_attr(), at.delta, at.buffs
        (new: 0/0, 0, {})
        >>> at.setup_attr(10), at.delta, at.buffs
        (new: 10/10, 0, {})
        >>> at.setup_attr(5, 1), at.delta, at.buffs
        (new: 5/5, 1, {})
        >>> at.setup_attr(10, None, {'st': 1}), at.delta, at.buffs
        (new: 11/10, 1, {'st': 1})
        >>> at.setup_attr(None, 5, {'ag': 2}), at.delta, at.buffs
        (new: 13/10, 5, {'st': 1, 'ag': 2})
        """
        self.base = base if base is not None else self.base
        self.delta = delta if delta is not None else self.delta
        if buffs is not None and isinstance(buffs, dict):
            self.buffs.update(buffs)
        return self

    def setup_attr_from_json(self, json_data):
        """Setups instance with values from a JSON variable.

        >>> at = Attr('new')
        >>> at, at.delta, at.buffs
        (new: 0/0, 0, {})
        >>> data = '{"base": 10, "delta": 1, "buffs": "None"}'
        >>> at.setup_attr_from_json(data), at.delta, at.buffs
        (new: 10/10, 1, {})
        >>> data = '{"base": "None", "delta": 5, "buffs": {"one": 4}}'
        >>> at.setup_attr_from_json(data), at.delta, at.buffs
        (new: 14/10, 5, {'one': 4})
        """
        dicta = json.loads(json_data)
        return self.setup_attr(int(dicta['base']) if dicta['base'] != "None" else None,
                               int(dicta['delta']) if dicta['delta'] != "None" else None,
                               dicta['buffs'] if dicta['buffs'] != 'None' else None)

    def __repr__(self):
        """Instace string representation.

        >>> at = Attr('old')
        >>> at
        old: 0/0
        """
        return '{0}: {1}/{2}'.format(self.name, self.now, self.base)


class Attributes(StrItero):
    """Attributes Class contains all attributes related with a board object.
    """

    def __init__(self):
        """Attribute class initialization method.

        >>> ats = Attributes()
        >>> ats['hp'] = Attr('hp')
        >>> ats['hp'].name
        'hp'
        >>> ats['HP'].name
        'hp'
        >>> ats['MP'] = Attr('mp')
        >>> ats['mp'].name
        'mp'
        >>> ats['MP'].name
        'mp'
        >>> del ats['hp']
        >>> try:
        ...     ats['hp']
        ... except KeyError:
        ...     'KeyError'
        'KeyError'
        """
        super(Attributes, self).__init__(Attr, self._buildAttrName)

    def _buildAttrName(self, name):
        """Builds the name used to identify an attribute.

        >>> ats = Attributes()
        >>> ats._buildAttrName('new')
        'NEW'
        """
        return '{0}'.format(name.upper())

    def add_attr(self, attr):
        """Adds a new attribute.

        >>> ats = Attributes()
        >>> ats.add_attr(Attr('hp'))
        hp: 0/0
        >>> ats['hp'].name
        'hp'
        >>> ats['HP'].name
        'hp'
        """
        self[attr.name] = attr
        return attr

    def setup_attrs(self, attrs):
        """Adds all attributes given in the passed list.

        >>> ats = Attributes()
        >>> ats.setup_attrs([Attr('hp'), Attr('mp')])
        >>> ats
        hp: 0/0
        mp: 0/0
        """
        for attrib in attrs:
            self.add_attr(attrib)

    def setup_attrs_by_name(self, names):
        """Adds all attributes in the list, which provides just the
        attribute name.

        >>> ats = Attributes()
        >>> ats.setup_attrs_by_name(['hp', 'mp'])
        >>> ats
        hp: 0/0
        mp: 0/0
        """
        for name in names:
            self.add_attr(Attr(name))

    def setup_attrs_from_list(self, lista):
        """Setups attributes from teh given list.

        >>> ats = Attributes()
        >>> data = [("hp", 10, 2), ("mp", 5, 1, {'one': 2})]
        >>> ats.setup_attrs_from_list(data)
        >>> ats
        hp: 10/10
        mp: 7/5
        >>> ats['HP'].delta
        2
        >>> ats['mp'].delta
        1
        """
        for entry in lista:
            self.add_attr(Attr.create_attr(entry))

    def setup_attrs_from_json(self, json_data):
        """Setups attributes from the given JSON variable.

        >>> ats = Attributes()
        >>> data = '[{"hp": {"base": 10, "delta": 2, "buffs": "none"}},\
                {"mp": {"base": 5, "delta": 1, "buffs": {"one": 2}}}]'
        >>> ats.setup_attrs_from_json(data)
        >>> ats
        hp: 10/10
        mp: 7/5
        >>> ats['HP'].delta
        2
        >>> ats['mp'].delta
        1
        """
        lista = json.loads(json_data)
        for entry in lista:
            k = list(entry.keys())[0]
            v = json.dumps(list(entry.values())[0])
            self.add_attr(Attr(k)).setup_attr_from_json(v)

    def setup_attrs_from_file(self, filename):
        """Setups instance from teh values in the given JSON file.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
        self.setup_attrs_from_json(json.dumps(data))

    def level_up(self, level_val=1):
        """Levels up all attributes stored a given number of times.

        >>> ats = Attributes()
        >>> hp = Attr('hp')
        >>> hp.base = 10
        >>> hp.delta = 3
        >>> ats.add_attr(hp)
        hp: 10/10
        >>> mp = Attr('mp')
        >>> mp.base = 5
        >>> mp.delta = 2
        >>> ats.add_attr(mp)
        mp: 5/5
        >>> ats.level_up()
        True
        >>> hp.base
        13
        >>> mp.base
        7
        >>> ats.level_up(2)
        True
        >>> hp.base
        19
        >>> mp.base
        11
        """
        for attr in self:
            attr.level_up(level_val)
        return True

    def __repr__(self):
        """Instance string representation.

        >>> ats = Attributes()
        >>> ats.add_attr(Attr('hp'))
        hp: 0/0
        >>> ats.add_attr(Attr('mp'))
        mp: 0/0
        >>> ats
        hp: 0/0
        mp: 0/0
        """
        return '\n'.join([str(attr) for attr in self])

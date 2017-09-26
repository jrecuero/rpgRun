from gequip import GEquip


class Weapon(GEquip):

    def __init__(self, **kwargs):
        kwargs.setdefault('theName', 'weapon')
        super(Weapon, self).__init__(**kwargs)


class Armor(GEquip):

    def __init__(self, **kwargs):
        kwargs.setdefault('theName', 'armor')
        super(Armor, self).__init__(**kwargs)


class Shield(GEquip):

    def __init__(self, **kwargs):
        kwargs.setdefault('theName', 'shield')
        super(Shield, self).__init__(**kwargs)

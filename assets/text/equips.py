from gequip import GEquip


class Weapon(GEquip):

    def __init__(self, **kwargs):
        kwargs.setdefault('name', 'weapon')
        super(Weapon, self).__init__(**kwargs)


class Armor(GEquip):

    def __init__(self, **kwargs):
        kwargs.setdefault('name', 'armor')
        super(Armor, self).__init__(**kwargs)


class Shield(GEquip):

    def __init__(self, **kwargs):
        kwargs.setdefault('name', 'shield')
        super(Shield, self).__init__(**kwargs)

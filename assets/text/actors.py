from rpgrun.bsprite import TextSprite
from rpgrun.actor import Actor
from rpgrun.pactor import PActor

PLAYER_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                   {"str": {"base": 9, "delta": 1, "buffs": "None"}},
                   {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''

ACTOR_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                  {"str": {"base": 5, "delta": 1, "buffs": "None"}},
                  {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''

MAGE_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                 {"mp": {"base": 10, "delta": 1, "buffs": "None"}},
                 {"str": {"base": 5, "delta": 1, "buffs": "None"}},
                 {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''

BOSS_ATTRS = [("hp", 100, 10), ("mp", 10, 1), ("str", 10, 1), ("con", 10, 2)]


class BossActor(Actor):

    def __init__(self, x, y, width, name='BOSS', **kwargs):
        super(BossActor, self).__init__(x, y, name, **kwargs)
        self.sprite = TextSprite(sprite='*&*', width=width, color="\x1b[32m" + "\x1b[45m")
        self.attrs.setup_attrs_from_list(BOSS_ATTRS)


class PlayerActor(PActor):

    def __init__(self, x, y, width, **kwargs):
        super(PlayerActor, self).__init__(x, y, 'PLAYER', **kwargs)
        self.sprite = TextSprite(sprite='-^-', width=width, color="\x1b[32m" + "\x1b[41m")
        self.attrs.setup_attrs_from_json(PLAYER_ATTRS)


class EnemyActor(Actor):

    def __init__(self, x, y, width, name='ENEMY', **kwargs):
        super(EnemyActor, self).__init__(x, y, name, **kwargs)
        self.sprite = TextSprite(sprite='oOo', width=width, color="\x1b[32m" + "\x1b[40m")
        self.attrs.setup_attrs_from_json(ACTOR_ATTRS)


class MageActor(Actor):

    def __init__(self, x, y, width, name='MAGE', **kwargs):
        super(MageActor, self).__init__(x, y, name, **kwargs)
        self.sprite = TextSprite(sprite='o$o', width=width, color="\x1b[32m" + "\x1b[40m")
        self.attrs.setup_attrs_from_json(MAGE_ATTRS)

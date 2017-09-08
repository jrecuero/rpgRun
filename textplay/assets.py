from bcell import BSprite
from bobject import BObject
from bsurface import BSurface
from actor import Actor
from pactor import PActor

PLAYER_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                   {"str": {"base": 9, "delta": 1, "buffs": "None"}},
                   {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''

ACTOR_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                  {"str": {"base": 5, "delta": 1, "buffs": "None"}},
                  {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''


class GreenSurface(BSurface):

    def __init__(self, theX, theY, theWidth, **kwargs):
        super(GreenSurface, self).__init__(theX, theY, '*', **kwargs)
        self.Sprite = BSprite(theSprText=' ', theColor='\x1b[42m', theWidth=theWidth)


class PlayerActor(PActor):

    def __init__(self, theX, theY, theWidth, **kwargs):
        super(PlayerActor, self).__init__(theX, theY, 'PLAYER', **kwargs)
        self.Sprite = BSprite(theSprText='-^-', theWidth=theWidth, theColor="\x1b[32m" + "\x1b[41m")
        self.Attrs.setupAttrsFromJSON(PLAYER_ATTRS)


class EnemyActor(Actor):

    def __init__(self, theX, theY, theWidth, **kwargs):
        super(EnemyActor, self).__init__(theX, theY, 'ENEMY', **kwargs)
        self.Sprite = BSprite(theSprText='oOo', theWidth=theWidth, theColor="\x1b[32m" + "\x1b[41m")
        self.Attrs.setupAttrsFromJSON(ACTOR_ATTRS)


class Pillar(BObject):

    def __init__(self, theX, theY, theWidth, **kwargs):
        super(Pillar, self).__init__(theX, theY, 'PILLAR', **kwargs)
        self.Sprite = BSprite(theSprText='|||||||', theWidth=theWidth, theColor="\x1b[44m")

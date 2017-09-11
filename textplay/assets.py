from bpoint import Location
from bcell import BSprite
from blayer import LType
from bobject import BObject
from bsurface import BSurface
from actor import Actor
from pactor import PActor
from action import Action, AType

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


class WeaponAction(Action):

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        super(WeaponAction, self).__init__(theName, theType, **kwargs)

    def requires(self):
        return None

    def consume(self):
        return None

    def layerToTarget(self):
        return [LType.OBJECT, ]

    def filterTarget(self, theCells):
        cells = []
        for cell in [x for x in theCells if x != self.Originator]:
            if cell.isActor():
                cells.append(cell)
        return cells

    def drySelect(self):
        pass

    def select(self):
        pass

    def selected(self, theTarget):
        self.Target = theTarget

    def dryExecute(self):
        pass

    def execute(self, theGame):
        damage = self.Originator.STR - self.Target[0].CON
        self.Target[0].Attrs['HP'].dec(damage)

    def dryResult(self):
        pass

    def result(self):
        pass


class MoveAction(Action):

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        super(MoveAction, self).__init__(theName, theType, **kwargs)

    def requires(self):
        return None

    def consume(self):
        return None

    def layerToTarget(self):
        return None

    def filterTarget(self, theCells):
        return [self.Originator, ]

    def drySelect(self):
        pass

    def select(self):
        pass

    def selected(self, theTarget):
        self.Target = theTarget

    def dryExecute(self):
        pass

    def execute(self, theGame):
        theGame.movePlayer(Location.FRONT, 1)

    def dryResult(self):
        pass

    def result(self):
        pass

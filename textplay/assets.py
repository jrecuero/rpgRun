from bpoint import Location
from bcell import BSprite
from blayer import LType
from bobject import BObject
from bsurface import BSurface
from actor import Actor
from pactor import PActor
from action import Action, AType, AoE

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

    def __init__(self, theX, theY, theWidth, theName='ENEMY', **kwargs):
        super(EnemyActor, self).__init__(theX, theY, theName, **kwargs)
        self.Sprite = BSprite(theSprText='oOo', theWidth=theWidth, theColor="\x1b[32m" + "\x1b[41m")
        self.Attrs.setupAttrsFromJSON(ACTOR_ATTRS)


class MageActor(Actor):

    def __init__(self, theX, theY, theWidth, theName='MAGE', **kwargs):
        super(MageActor, self).__init__(theX, theY, theName, **kwargs)
        self.Sprite = BSprite(theSprText='oOo', theWidth=theWidth, theColor="\x1b[32m" + "\x1b[41m")
        self.Attrs.setupAttrsFromJSON(MAGE_ATTRS)


class Pillar(BObject):

    def __init__(self, theX, theY, theWidth, **kwargs):
        super(Pillar, self).__init__(theX, theY, 'PILLAR', **kwargs)
        self.Sprite = BSprite(theSprText='|||||||', theWidth=theWidth, theColor="\x1b[44m")


class WeaponAction(Action):

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        super(WeaponAction, self).__init__(theName, theType, **kwargs)

    def layerToTarget(self):
        return [LType.OBJECT, ]

    def filterTarget(self, theCells):
        return [x for x in theCells if self.isValidTarget(x)]

    def selected(self, theTarget):
        self.Target = theTarget

    def execute(self, theGame, **kwargs):
        damage = self.Originator.STR - self.Target[0].CON
        self.Target[0].Attrs['HP'].dec(damage)


class RangeAction(Action):

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        super(RangeAction, self).__init__(theName, theType, **kwargs)
        width = kwargs.get('theWidth')
        height = kwargs.get('theHeight')
        shape = kwargs.get('theShape')
        self.AoE = AoE(None, width, height, shape)

    @Action.Originator.setter
    def Originator(self, theValue):
        Action.Originator.fset(self, theValue)
        self.AoE.Shape.Center = theValue

    def layerToTarget(self):
        return [LType.OBJECT, ]

    def filterTarget(self, theCells):
        return [x for x in theCells if self.isValidTarget(x) and self.AoE.Shape.isInside(x)]

    def selected(self, theTarget):
        self.Target = theTarget

    def execute(self, theGame, **kwargs):
        damage = self.Originator.STR
        self.Target[0].Attrs['HP'].dec(damage)


class MoveAction(Action):

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        super(MoveAction, self).__init__(theName, theType, **kwargs)

    @Action.Originator.setter
    def Originator(self, theValue):
        self._originator = theValue
        self.Target = theValue

    def requires(self, theGame):
        print('requires to enter Location and Position for movement')
        target = yield
        yield target

    def requiresTarget(self):
        """
        """
        return False

    def requiresMovement(self):
        """
        """
        return True

    def layerToTarget(self):
        return None

    def filterTarget(self, theCells):
        return [self.Originator, ]

    def selected(self, theTarget):
        self.Target = theTarget

    def execute(self, theGame, **kwargs):
        location = kwargs.get('theLocation', Location.FRONT)
        position = kwargs.get('thePostion', 1)
        theGame.movePlayer(location, position)

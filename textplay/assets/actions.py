from bpoint import Location
from action import AType, TargetAction, MoveAction, AoETargetAction


class WeaponAction(TargetAction):

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        super(WeaponAction, self).__init__(theName, theType, **kwargs)

    def execute(self, theGame, **kwargs):
        damage = self.Originator.STR - self.Target[0].CON
        self.Target[0].Attrs['HP'].dec(damage)


class MeleAction(AoETargetAction):

    def execute(self, theGame, **kwargs):
        damage = self.Originator.STR - self.Target[0].CON
        self.Target[0].Attrs['HP'].dec(damage)


class RangeAction(AoETargetAction):

    def execute(self, theGame, **kwargs):
        damage = self.Originator.STR
        self.Target[0].Attrs['HP'].dec(damage)


class MoveAction(MoveAction):

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        super(MoveAction, self).__init__(theName, theType, **kwargs)

    def execute(self, theGame, **kwargs):
        location = kwargs.get('theLocation', Location.FRONT)
        position = kwargs.get('thePostion', 1)
        theGame.movePlayer(location, position)

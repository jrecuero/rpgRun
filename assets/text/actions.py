from rpgrun.board.bpoint import Location
from rpgrun.game.action import AType, TargetAction, MoveAction, AoETargetAction


class WeaponAction(TargetAction):

    def __init__(self, name, type_=AType.NONE, **kwargs):
        super(WeaponAction, self).__init__(name, type_, **kwargs)

    def execute(self, game, **kwargs):
        damage = self.originator.STR - self.target[0].CON
        self.target[0].attrs['HP'].dec(damage)


class MeleAction(AoETargetAction):

    def execute(self, game, **kwargs):
        damage = self.originator.STR - self.target[0].CON
        self.target[0].attrs['HP'].dec(damage)


class RangeAction(AoETargetAction):

    def execute(self, game, **kwargs):
        damage = self.originator.STR
        self.target[0].attrs['HP'].dec(damage)


class MoveAction(MoveAction):

    def __init__(self, name, type_=AType.NONE, **kwargs):
        super(MoveAction, self).__init__(name, type_, **kwargs)

    def execute(self, game, **kwargs):
        location = kwargs.get('location', Location.FRONT)
        position = kwargs.get('position', 1)
        game.move_player(location, position)

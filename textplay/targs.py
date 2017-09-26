# import sys
# sys.path.append('../jc2li')

from bpoint import Location
from argtypes import Int, Str


class T_Target(Str):

    def _helpStr(self):
        return "Enter target for action"

    def complete(self, document, text):
        _game = self.Journal.getFromCache('game')
        if _game is not None:
            return [x.Name for x in _game.TargetChoice]
        return []


class T_Actor(Str):

    def _helpStr(self):
        return "Enter actor name"

    def completeGetList(self, document, text):
        """
        """
        _game = self.Journal.getFromCache('game')
        if _game is not None:
            return [x.Name for x in _game.Actors]
        return None


class T_Equip(Str):

    def __init__(self, **kwargs):
        super(T_Equip, self).__init__(**kwargs)
        self._equipFlag = kwargs.get('equip', True)

    def _checkFlag(self, theEquip):
        if self._equipFlag:
            return theEquip.isEquip() and not theEquip.Equipped
        else:
            return theEquip.isEquip() and theEquip.Equipped

    def _helpStr(self):
        return "Enter a piece of equipment"

    def completeGetList(self, document, text):
        _game = self.Journal.getFromCache('game')
        if _game is not None:
            _line = document.text.split()
            _name = _line[-1] if document.text[-1].strip() == '' else _line[-2]
            _actor = _game.findActorByName(_name)
            if _actor is not None:
                if self._equipFlag:
                    return [x.Name for x in _actor.Inventory if self._checkFlag(x)]
                else:
                    return [x.Name for x in _actor.Equipment]
        return None


class T_Attr(Str):

    def _helpStr(self):
        return "Enter attribute for actor"

    def complete(self, document, text):
        _game = self.Journal.getFromCache('game')
        if _game is not None:
            _line = document.text.split()
            _name = _line[-1] if document.text[-1].strip() == '' else _line[-2]
            _actor = _game.findActorByName(_name)
            if _actor is not None:
                return [x.Name for x in _actor.Attrs]
        return []


class T_Action(Str):

    def _helpStr(self):
        return "Enter action"

    def complete(self, document, text):
        _game = self.Journal.getFromCache('game')
        if _game is not None:
            return [x.Name for x in _game.Player.Actions]
        return []


class T_Location(Str):

    @staticmethod
    def _(val):
        return Location[val]

    @staticmethod
    def type():
        return Location

    def _helpStr(self):
        return "Enter location for movement"

    def complete(self, document, text):
        return [x.name for x in Location.userMoves()]


class T_Step(Int):

    @staticmethod
    def _(val):
        if int(val) > 1:
            print('you are moving to far')
        return int(val)

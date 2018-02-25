from rpgrun.board.bpoint import Location
from jc2cli.builtin.argos import Int, Str


class T_Target(Str):

    def __init__(self, data_cache, **kwargs):
        self.data_cache = data_cache

    def get_help_str(self):
        return "Enter target for action"

    def get_complete_list(self, document, text):
        game = self.data_cache['game']
        if game is not None:
            return [x.name for x in game.target_choice]
        return []


class T_Actor(Str):

    def __init__(self, data_cache, **kwargs):
        self.data_cache = data_cache

    def get_help_str(self):
        return "Enter actor name"

    def get_complete_list(self, document, text):
        """
        """
        game = self.data_cache['game']
        if game is not None:
            return [x.name for x in game.actors]
        return None


class T_Equip(Str):

    def __init__(self, data_cache, **kwargs):
        super(T_Equip, self).__init__(**kwargs)
        self.data_cache = data_cache
        self._equip_flag = kwargs.get('equip', True)

    def _check_flag(self, equip):
        if self._equip_flag:
            return equip.is_equip() and not equip.equipped
        else:
            return equip.is_equip() and equip.equipped

    def get_help_str(self):
        return "Enter a piece of equipment"

    def get_complete_list(self, document, text):
        game = self.data_cache['game']
        if game is not None:
            line = document.text.split()
            name = line[-1] if document.text[-1].strip() == '' else line[-2]
            actor = game.find_actor_by_name(name)
            if actor is not None:
                if self._equip_flag:
                    return [x.name for x in actor.inventory if self._check_flag(x)]
                else:
                    return [x.name for x in actor.equipment]
        return None


class T_Attr(Str):

    def __init__(self, data_cache, **kwargs):
        self.data_cache = data_cache

    def get_help_str(self):
        return "Enter attribute for actor"

    def get_complete_list(self, document, text):
        game = self.data_cache['game']
        if game is not None:
            line = document.text.split()
            name = line[-1] if document.text[-1].strip() == '' else line[-2]
            actor = game.find_actor_by_name(name)
            if actor is not None:
                return [x.name for x in actor.attrs]
        return []


class T_Action(Str):

    def __init__(self, data_cache, **kwargs):
        self.data_cache = data_cache

    def get_help_str(self):
        return "Enter action"

    def get_complete_list(self, document, text):
        game = self.data_cache['game']
        if game is not None:
            return [x.name for x in game.player.actions]
        return []


class T_Location(Str):

    @staticmethod
    def _(val):
        return Location[val]

    @staticmethod
    def type():
        return Location

    def get_help_str(self):
        return "Enter location for movement"

    def get_complete_list(self, document, text):
        return [x.name for x in Location.user_moves()]


class T_Step(Int):

    @staticmethod
    def _(val):
        if int(val) > 1:
            print('you are moving to far')
        return int(val)

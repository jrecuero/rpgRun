# import sys
# sys.path.append('../jc2li')

import game
from blayer import LType
from bpoint import Point, Location
from shapes import Quad
from base import Cli
from decorators import argo, syntax, setsyntax
from argtypes import Int, Str
from brow import BRow
from action import AType
from actor import Actor
from assets import GreenSurface, PlayerActor, EnemyActor, MageActor, Pillar
from assets import WeaponAction, RangeAction, MoveAction
from assets import Weapon, Armor, Shield
import loggerator


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


class T_Attr(Str):

    def _helpStr(self):
        return "Enter attribute for actor"

    def complete(self, document, text):
        _game = self.Journal.getFromCache('game')
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

    def complete(self, text):
        return [x.name for x in Location.userMoves()]


class T_Step(Int):

    @staticmethod
    def _(val):
        if int(val) > 1:
            print('you are moving to far')
        return int(val)


class Play(Cli):

    def __init__(self):
        super(Play, self).__init__()
        self._game = None
        self._logger = loggerator.getLoggerator('PLAY')

    def _scroll(self):
        """Scroll Board.
        """
        width = self._game.Board.Width
        row = BRow(width)
        newHeight = self._game.Board.TopCellRow + 1
        for iwidth in range(width):
            row.addCellToLayer(GreenSurface(iwidth, newHeight, self._sprWidth), LType.SURFACE)
        self._game.scrollBoard(row)

    @Cli.command('INIT')
    def do_init(self, *args):
        """Initialize rpgRUN game.
        """
        self._width = 7
        self._height = 7
        self._sprWidth = 7
        self._game = game.Game(self._width, self._height)
        self.Journal.setToCache('game', self._game)
        iheight = self._height
        for row in self._game.Board:
            iheight -= 1
            for iwidth in range(self._width):
                row.addCellToLayer(GreenSurface(iwidth, iheight, self._sprWidth), LType.SURFACE)

        Actor.LIFE = 'hp'
        player = PlayerActor(2, 4, self._sprWidth)
        player.Actions.append(WeaponAction('weapon', AType.WEAPONIZE))
        player.Actions.append(RangeAction('range', AType.WEAPONIZE, theWidth=2, theHeight=2, theShape=Quad))
        player.Actions.append(MoveAction('move', AType.MOVEMENT))
        enemies = []
        enemies.append(EnemyActor(4, 6, self._sprWidth, 'GOBLIN'))
        enemies.append(EnemyActor(3, 5, self._sprWidth, 'ORC'))
        enemies.append(EnemyActor(1, 6, self._sprWidth, 'TROLL'))
        enemies.append(MageActor(0, 5, self._sprWidth, 'MAGE'))
        enemies[-1].Life = 'mp'
        pillar = Pillar(0, 6, self._sprWidth)

        sword = Weapon(theAttrBuff={'str': 5})
        armor = Armor(theAttrBuff={'hp': 10})
        shield = Shield(theAttrBuff={'hp': 7, 'str': 1})
        player.Inventory.append(sword)
        player.Inventory.append(armor)
        player.Inventory.append(shield)
        player.Equipment.append(sword)
        player.Equipment.append(armor)
        player.Equipment.append(shield)

        self._game.addActor(player, True)
        for x in enemies:
            self._game.addActor(x)

        self._game.Board.getRowFromCell(player).addCellToLayer(player, LType.OBJECT)
        self._game.Board.getRowFromCell(pillar).addCellToLayer(pillar, LType.OBJECT)
        for x in enemies:
            self._game.Board.getRowFromCell(x).addCellToLayer(x, LType.OBJECT)

        self.RPrompt = '<play>'
        self._logger.display('Init rpgRun')

    @Cli.command()
    @setsyntax
    @syntax("MOVE loc pos")
    @argo('loc', T_Location, None)
    @argo('pos', Int, None)
    def do_move_player(self, loc, pos):
        """Move player a number of positions to given location.
        """
        self._game.movePlayer(loc, pos)
        if loc == Location.FRONT:
            self._scroll()

    @Cli.command()
    @setsyntax
    @syntax("PLAYER [name]?")
    @argo('name', T_Actor, 'PLAYER')
    def do_print_player(self, name):
        """Print player information.
        """
        _actor = self._game.findActorByName(name)
        self._logger.display("Data for  : {0}".format(name))
        self._logger.display("Name      : {0}".format(_actor.Name))
        self._logger.display("Position  : {0}".format(_actor.getPoint()))
        self._logger.display("Attributes:\n{0}".format(_actor.Attrs))

    @Cli.command()
    @setsyntax
    @syntax("INVENTORY name")
    @argo('name', T_Actor, None)
    def do_print_inventory(self, name):
        """Prints player inventory.
        """
        _actor = self._game.findActorByName(name)
        self._logger.display("Inventory for  : {0}".format(name))
        for x in _actor.Inventory:
            self._logger.display(">> {0}".format(x))

    @Cli.command()
    @setsyntax
    @syntax("EQUIPEMENT name")
    @argo('name', T_Actor, None)
    def do_print_equipment(self, name):
        """Prints player equipment.
        """
        _actor = self._game.findActorByName(name)
        self._logger.display("Equipment for  : {0}".format(name))
        for x in _actor.Equipment:
            self._logger.display(">> {0}".format(x))

    @Cli.command('ACTORS')
    def do_print_actors(self, *args):
        """Print actors attributes.
        """
        for _actor in self._game.Actors:
            self._logger.display("Data for  : {0}".format(_actor.Name))
            self._logger.display("Position  : {0}".format(Point.__repr__(_actor)))
            self._logger.display("Attributes:\n{0}".format(_actor.Attrs))

    @Cli.command('PRINT')
    def do_print_board(self, *args):
        """Print rpgRUN game board.
        """
        self._logger.display(self._game.Board.render(theWidth=7))

    @Cli.command('SCROLL')
    def do_scroll_board(self, *args):
        """Scroll Board.
        """
        self._scroll()

    @Cli.command('RUN')
    def do_run(self, *args):
        """Run a cycle
        """
        print('select action (use command: ACTION <name>) ')
        for i, x in enumerate(self._game.Player.Actions):
            print('{0} : {1}'.format(i, x.Name))
        self.RPrompt = '<select-action>'
        self.Prompt = '[ACTION <name>] rpgRun> '

    @Cli.command()
    @setsyntax
    @syntax("ACTION name")
    @argo('name', T_Action, None)
    def do_action(self, name):
        """Select action to run.
        """
        for _action in self._game.Player.Actions:
            if _action.Name == name:
                break
        else:
            return
        _action.Originator = self._game.Player
        self._game.runInit()
        _actionType = self._game.runSelectAction(_action)
        if _actionType == AType.WEAPONIZE:
            print('select target (use command: TARGET <name>)')
            for i, x in enumerate(self._game.TargetChoice):
                print('{0} : {1}'.format(i, x))
            self.RPrompt = '<select-target>'
            self.Prompt = '[TARGET <name>] rpgRun> '
        elif _actionType == AType.MOVEMENT:
            print('select player movement (use command: MOVEMENT <loc> <pos>)')
            self.RPrompt = '<select-movement>'
            self.Prompt = '[MOVEMENT <loc> <pos>] rpgRun> '

    @Cli.command()
    @setsyntax
    @syntax("TARGET name")
    @argo('name', T_Target, None)
    def do_target(self, name):
        """Select target for the action to run.
        """
        for _target in self._game.TargetChoice:
            if _target.Name == name:
                break
        else:
            return
        self._game.runSelectTarget(_target)
        self.RPrompt = '<play>'
        self.Prompt = 'rpgRun> '

    @Cli.command()
    @setsyntax
    @syntax("MOVEMENT loc pos")
    @argo('loc', T_Location, None)
    @argo('pos', T_Step, None)
    def do_select_movement(self, loc, pos):
        """Select location and steps for the player to move.
        """
        print('player moves {0} to {1}'.format(pos, loc))
        self._game.runSelectMovement(loc, pos)
        self.RPrompt = '<play>'

    @Cli.command()
    @setsyntax
    @syntax("debug aname attr value")
    @argo('aname', T_Actor, None)
    @argo('attr', T_Attr, None)
    @argo('value', Int, None)
    def do_debug_player(self, aname, attr, value):
        """Updates actor attribute.
        """
        _actor = self._game.findActorByName(aname)
        if _actor:
            _actor.Attrs[attr].Base = value
            self.do_print_player("name={}".format(aname))

    @Cli.command('REFRESH')
    def do_refresh(self, *args):
        """Refreshes board game.
        """
        self._game._updateActors()


if __name__ == '__main__':

    cli = Play()
    try:
        # cli.Prompt = 'rpgRun> '
        cli.cmdloop(thePrompt='rpgRun> ')
    except KeyboardInterrupt:
        cli._logger.display("")
        pass

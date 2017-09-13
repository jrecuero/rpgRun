# import sys
# sys.path.append('../jc2li')

import game
from blayer import LType
from bpoint import Point, Location
from base import Cli
from decorators import argo, syntax, setsyntax
from argtypes import Int, Str
from brow import BRow
from action import AType
from assets import GreenSurface, PlayerActor, EnemyActor, Pillar
from assets import WeaponAction, MoveAction
import loggerator


class T_Target(Str):

    def _helpStr(self):
        return "Enter target for action"

    def complete(self, text):
        _game = self.Journal.getFromCache('game')
        if _game is not None:
            return [x.Name for x in _game.TargetChoice]
        return []


class T_Action(Str):

    def _helpStr(self):
        return "Enter action"

    def complete(self, text):
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

        player = PlayerActor(2, 4, self._sprWidth)
        player.Actions = WeaponAction('weapon', AType.WEAPONIZE)
        player.Actions = MoveAction('move', AType.MOVEMENT)
        enemy = EnemyActor(4, 6, self._sprWidth)
        pillar = Pillar(0, 6, self._sprWidth)

        self._game.addActor(player, True)
        self._game.addActor(enemy)

        self._game.Board.getRowFromCell(player).addCellToLayer(player, LType.OBJECT)
        self._game.Board.getRowFromCell(pillar).addCellToLayer(pillar, LType.OBJECT)
        self._game.Board.getRowFromCell(enemy).addCellToLayer(enemy, LType.OBJECT)

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
    @argo('name', Str, 'PLAYER')
    def do_print_player(self, name):
        """Print player information.
        """
        self._logger.display("Data for  : {0}".format(name))
        self._logger.display("Name      : {0}".format(self._game.Player.Name))
        self._logger.display("Position  : {0}".format(Point.__repr__(self._game.Player)))
        self._logger.display("Attributes:\n{0}".format(self._game.Player.Attrs))

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
        elif _actionType == AType.MOVEMENT:
            print('select player movement (use command: MOVEMENT <loc> <pos>)')

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


if __name__ == '__main__':

    cli = Play()
    try:
        cli.cmdloop('rpgRun> ')
    except KeyboardInterrupt:
        cli._logger.display("")
        pass

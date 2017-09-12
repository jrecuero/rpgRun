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
        self._width = 5
        self._height = 5
        self._sprWidth = 7
        self._game = game.Game(self._width, self._height)
        iheight = self._height
        for row in self._game.Board:
            iheight -= 1
            for iwidth in range(self._width):
                row.addCellToLayer(GreenSurface(iwidth, iheight, self._sprWidth), LType.SURFACE)

        player = PlayerActor(2, 2, self._sprWidth)
        player.Actions = WeaponAction('weapon', AType.WEAPONIZE)
        player.Actions = MoveAction('move', AType.MOVEMENT)
        enemy = EnemyActor(4, 4, self._sprWidth)

        self._game.addActor(player, True)
        self._game.addActor(enemy)

        self._game.Board[2].addCellToLayer(self._game.Player, LType.OBJECT)
        self._game.Board[0].addCellToLayer(Pillar(0, 4, self._sprWidth), LType.OBJECT)
        self._game.Board[0].addCellToLayer(enemy, LType.OBJECT)
        self._logger.display('Init rpgRun')

    @Cli.command()
    @setsyntax
    @syntax("MOVE locst pos")
    @argo('locst', Str, None)
    @argo('pos', Int, None)
    def do_move_player(self, locst, pos):
        """Move player a number of positions to given location.
        """
        locst = locst.upper()
        scrollFlag = False
        if locst == 'FRONT':
            loc = Location.FRONT
            scrollFlag = True
        # We can NOT move backwards
        # elif locst == 'BACK':
        #     loc = Location.BACK
        elif locst == 'LEFT':
            loc = Location.LEFT
        elif locst == 'RIGHT':
            loc = Location.RIGHT
        else:
            loc = None
        if loc is not None:
            self._game.movePlayer(loc, pos)
            if scrollFlag:
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
        print('select action (use command: ACTION <id>) ')
        for i, x in enumerate(self._game.Player.Actions):
            print('{0} : {1}'.format(i, x))

    @Cli.command()
    @setsyntax
    @syntax("ACTION actionid")
    @argo('actionid', Int, None)
    def do_action(self, actionid):
        """Select action
        """
        _action = self._game.Player.Actions[actionid]
        _action.Originator = self._game.Player
        self._game.runInit()
        _actionType = self._game.runSelectAction(_action)
        if _actionType == AType.WEAPONIZE:
            print('select target (use command: TARGET <id>)')
            for i, x in enumerate(self._game.TargetChoice):
                print('{0} : {1}'.format(i, x))
        elif _actionType == AType.MOVEMENT:
            print('select player movement (use command: MOVEMENT <pos> <locst>)')

    @Cli.command()
    @setsyntax
    @syntax("TARGET targetid")
    @argo('targetid', Int, None)
    def do_target(self, targetid):
        """Select target for the action.
        """
        _target = self._game.TargetChoice[targetid]
        self._game.runSelectTarget(_target)

    @Cli.command()
    @setsyntax
    @syntax("MOVEMENT locst pos")
    @argo('locst', Str, None)
    @argo('pos', Int, None)
    def do_select_movement(self, locst, pos):
        """Select player movement, location and steps.
        """
        locst = locst.upper()
        if locst == 'FRONT':
            loc = Location.FRONT
        # We can NOT move backwards
        # elif locst == 'BACK':
        #     loc = Location.BACK
        elif locst == 'LEFT':
            loc = Location.LEFT
        elif locst == 'RIGHT':
            loc = Location.RIGHT
        else:
            loc = None
        if loc is not None:
            self._game.runSelectMovement(loc, pos)


if __name__ == '__main__':

    cli = Play()
    try:
        cli.cmdloop('rpgRun> ')
    except KeyboardInterrupt:
        cli._logger.display("")
        pass

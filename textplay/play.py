import sys
sys.path.append('../jc2li')

import game
from blayer import LType
from bpoint import Point, Location
from base import Cli
from decorators import argo, syntax, setsyntax
from argtypes import Int, Str
from brow import BRow
from assets import GreenSurface, PlayerActor, EnemyActor, Pillar
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

        self._game.Player = PlayerActor(2, 2, self._sprWidth)
        self._game.Board[2].addCellToLayer(self._game.Player, LType.OBJECT)
        self._game.Board[0].addCellToLayer(Pillar(0, 4, self._sprWidth), LType.OBJECT)
        self._game.Board[0].addCellToLayer(EnemyActor(4, 4, self._sprWidth), LType.OBJECT)
        self._logger.display('Init rpgRun')

    @Cli.command()
    @setsyntax
    @syntax("MOVE pos locst")
    @argo('pos', Int, None)
    @argo('locst', Str, None)
    def do_move(self, pos, locst):
        """Move player a numner of positions.
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


if __name__ == '__main__':

    cli = Play()
    try:
        cli.cmdloop('rpgRun> ')
    except KeyboardInterrupt:
        cli._logger.display("")
        pass

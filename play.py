import sys
sys.path.append('../jc2li')

import game
from blayer import BLayer
from bpoint import Location
from base import Cli
from decorators import argo, syntax, setsyntax
from argtypes import Int, Str
from brow import BRow
from bobject import BObject
from bsurface import BSurface


class Play(Cli):

    def __init__(self):
        super(Play, self).__init__()
        self._game = None

    @Cli.command('INIT')
    def do_init(self, *args):
        """Initialize rpgRUN game.
        """
        width, height = (5, 5)
        self._game = game.Game(width, height)
        iheight = height
        for row in self._game.Board:
            iheight -= 1
            for iwidth in range(width):
                row.addCellToLayer(BSurface(iwidth, iheight, '****'), BLayer.LType.SURFACE)

        self._game.Player = BObject(2, 2, 'PLAYER')
        self._game.Board[2].addCellToLayer(self._game.Player, BLayer.LType.OBJECT)
        self._game.Board[0].addCellToLayer(BObject(0, 4, 'Pillar'), BLayer.LType.OBJECT)
        print('Init rpgRun')

    @Cli.command()
    @setsyntax
    @syntax("MOVE pos locst")
    @argo('pos', Int, None)
    @argo('locst', Str, None)
    def do_move(self, pos, locst):
        """Move player a numner of positions.
        """
        locst = locst.upper()
        if locst == 'FRONT':
            loc = Location.FRONT
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

    @Cli.command('PRINT')
    def do_print_board(self, *args):
        """Print rpgRUN game board.
        """
        for row in self._game.Board:
            print('{0} {1}'.format(row.CellRow, row.rowToString()))

    @Cli.command('SCROLL')
    def do_scroll_board(self, *args):
        """Scroll Board.
        """
        width = self._game.Board.Width
        row = BRow(width)
        newHeight = self._game.Board.TopCellRow + 1
        for iwidth in range(width):
            row.addCellToLayer(BSurface(iwidth, newHeight, '****'), BLayer.LType.SURFACE)
        self._game.scrollBoard(row)


if __name__ == '__main__':

    cli = Play()
    try:
        cli.cmdloop('rpgRun> ')
    except KeyboardInterrupt:
        print("")
        pass

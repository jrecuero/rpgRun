import game
from blayer import BLayer
from bpoint import Location
from base import Cli
from decorators import argo, syntax, setsyntax
from argtypes import Int


class Play(Cli):

    def __init__(self):
        super(Play, self).__init__()
        self._game = None

    @Cli.command('INIT')
    def do_init(self, *args):
        """Initialize rpgRUN game.
        """
        from bobject import BObject
        from bsurface import BSurface
        width, height = (5, 5)
        self._game = game.Game(width, height)
        for index, row in enumerate(self._game.Board):
            row.addCellToLayer(BSurface(0, index, None), BLayer.LType.SURFACE)
        self._game.Player = BObject(2, 2, 'PLAYER')
        self._game.Board[2].addCellToLayer(self._game.Player, BLayer.LType.OBJECT)
        print('Init rpgRun')

    @Cli.command()
    @setsyntax
    @syntax("MOVE pos")
    @argo('pos', Int, None)
    def do_move(self, pos):
        """Move player a numner of positions.
        """
        self._game.movePlayer(Location.FRONT, 1)

    @Cli.command('PRINT')
    def do_print_board(self, *args):
        """Print rpgRUN game board.
        """
        for row in self._game.Board:
            if row.CellRow == self._game.Player.Row:
                print('{0} {1}'.format(row.CellRow, self._game.Player))
            else:
                print(row.CellRow)


if __name__ == '__main__':

    cli = Play()
    try:
        cli.cmdloop('rpgRun> ')
    except KeyboardInterrupt:
        print("")
        pass

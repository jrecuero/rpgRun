import sys
sys.path.append('../jc2li')

import game
from blayer import LType
from bpoint import Point, Location
from base import Cli
from decorators import argo, syntax, setsyntax
from argtypes import Int, Str
from brow import BRow
from bcell import BSprite
from bobject import BObject
from bsurface import BSurface
from actor import Actor
from pactor import PActor

PLAYER_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                   {"str": {"base": 9, "delta": 1, "buffs": "None"}},
                   {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''

ACTOR_ATTRS = '''[{"hp": {"base": 10, "delta": 2, "buffs": "None"}},
                  {"str": {"base": 5, "delta": 1, "buffs": "None"}},
                  {"con": {"base": 3, "delta": 1, "buffs": "None"}}]'''


class Play(Cli):

    def __init__(self):
        super(Play, self).__init__()
        self._game = None

    def _scroll(self):
        """Scroll Board.
        """
        width = self._game.Board.Width
        row = BRow(width)
        newHeight = self._game.Board.TopCellRow + 1
        sprite = BSprite(theSprText=' ', theColor='\x1b[42m', theWidth=7)
        for iwidth in range(width):
            cell = BSurface(iwidth, newHeight, '*', theSprite=sprite)
            row.addCellToLayer(cell, LType.SURFACE)
        self._game.scrollBoard(row)

    @Cli.command('INIT')
    def do_init(self, *args):
        """Initialize rpgRUN game.
        """
        width, height = (5, 5)
        self._game = game.Game(width, height)
        iheight = height
        sprite = BSprite(theSprText=' ', theColor='\x1b[42m', theWidth=7)
        for row in self._game.Board:
            iheight -= 1
            for iwidth in range(width):
                cell = BSurface(iwidth, iheight, '*', theSprite=sprite)
                row.addCellToLayer(cell, LType.SURFACE)

        playerSprite = BSprite(theSprText='-^-', theWidth=7, theColor="\x1b[32m" + "\x1b[41m")
        actorSprite = BSprite(theSprText='oOo', theWidth=7, theColor="\x1b[32m" + "\x1b[41m")
        pillarSprite = BSprite(theSprText='|||||||', theWidth=7, theColor="\x1b[44m")
        self._game.Player = PActor(2, 2, 'PLAYER', theSprite=playerSprite)
        self._game.Player.Attrs.setupAttrsFromJSON(PLAYER_ATTRS)
        enemy = Actor(4, 4, 'ENEMY', theSprite=actorSprite)
        enemy.Attrs.setupAttrsFromJSON(ACTOR_ATTRS)
        self._game.Board[2].addCellToLayer(self._game.Player, LType.OBJECT)
        self._game.Board[0].addCellToLayer(BObject(0, 4, 'Pillar', theSprite=pillarSprite), LType.OBJECT)
        self._game.Board[0].addCellToLayer(enemy, LType.OBJECT)
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
        scrollFlag = False
        if locst == 'FRONT':
            loc = Location.FRONT
            scrollFlag = True
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
        print("Data for  : {0}".format(name))
        print("Name      : {0}".format(self._game.Player.Name))
        print("Position  : {0}".format(Point.__repr__(self._game.Player)))
        print("Attributes:\n{0}".format(self._game.Player.Attrs))

    @Cli.command('PRINT')
    def do_print_board(self, *args):
        """Print rpgRUN game board.
        """
        print(self._game.Board.render(theWidth=7))

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
        print("")
        pass

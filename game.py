from board import Board
from bhandler import BoardHandler
from bpoint import Location
# from brow import BRow
from blayer import BLayer


class Game(object):
    """Game class provides all requiered functionality to create a board
    game.
    """

    def __init__(self, theWidth, theHeight):
        """Game class initialization method.
        """
        self._bwidth = theWidth
        self._bheight = theHeight
        self._board = Board(self._bheight, self._bwidth)
        self._bhandler = BoardHandler(self._board)
        self._player = None

    @property
    def Board(self):
        """
        """
        return self._board

    @property
    def BHandler(self):
        """
        """
        return self._bhandler

    @property
    def Player(self):
        """
        """
        return self._player

    @Player.setter
    def Player(self, theValue):
        """
        """
        self._player = theValue

    def movePlayer(self, theDirection, theMove):
        """Moves the player (PActor instace) in the given direction and the
        given value.

        Args:
            theDirection (Location) : direction the player will be moved.
            theMove (int) : number of cells the player will be moved.

        Returns:
            None
        """
        assert isinstance(theDirection, Location)
        oldCellRow = self.Player.Row
        assert self.Player.moveTo(theDirection, theMove) is not None
        if oldCellRow != self.Player.Row:
            oldRow = self.Board.getRowFromCellRow(oldCellRow)
            assert oldRow is not None
            oldRow.removeCellFromLayer(self.Player, BLayer.LType.OBJECT)
            newRow = self.Board.getRowFromCellRow(self.Player.Row)
            assert newRow is not None
            newRow.addCellToLayer(self.Player, BLayer.LType.OBJECT)


def printBoard(theBoard):
    for row in theBoard.Board:
        if row.CellRow == theBoard.Player.Row:
            print('{0} {1}'.format(row.CellRow, theBoard.Player))
        else:
            print(row.CellRow)


from bobject import BObject
from bsurface import BSurface
width, height = (5, 5)
g = Game(width, height)
for index, row in enumerate(g.Board):
    row.addCellToLayer(BSurface(0, index, None), BLayer.LType.SURFACE)
g.Player = BObject(2, 2, 'PLAYER')
g.Board[2].addCellToLayer(g.Player, BLayer.LType.OBJECT)

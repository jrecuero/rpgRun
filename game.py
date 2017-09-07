from board import Board
from bhandler import BoardHandler
from bpoint import Location
from brow import BRow
from blayer import LType


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
        # This moveTo should be replaced with a move with collision and range
        # check in order to validate the movement.
        assert self.Player.moveTo(theDirection, theMove) is not None
        if oldCellRow != self.Player.Row:
            oldRow = self.Board.getRowFromCellRow(oldCellRow)
            assert oldRow is not None
            oldRow.removeCellFromLayer(self.Player, LType.OBJECT)
            newRow = self.Board.getRowFromCellRow(self.Player.Row)
            assert newRow is not None
            newRow.addCellToLayer(self.Player, LType.OBJECT)

    def scrollBoard(self, theNewRow):
        """Scroll the board, removing one row and adding a new one.

        Scroll always moves row to the front, it means to higher
        cell-row values.

        Args:
            theNewRow (BRow) : new row to be added to the board.

        Returns:
            None
        """
        assert isinstance(theNewRow, BRow)
        self.Board.scroll(theNewRow)

    def oneRun(self):
        """Executes one run cycle.

        Run cycle stages:
            - Prompt user for operation. Action could be movement and any other
            action (attack, use skills, items, defense, ...). They can be
            selected and executed in any order.
                * If user select an action, proceed with actions stages, which
                should be target selection and action execution.
                * If user select a movement, check if movement is allowed and
                proceed with the move.
            - After user has finished all operations, then proceed with any
            other actor in the board. Any other actor can not move, they can
            just proceed with an action. Follow the same action rules.
            - After all actors have taken their turn, scroll the board and end
            the cycle.
        """
        pass


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
    row.addCellToLayer(BSurface(0, index, None), LType.SURFACE)
g.Player = BObject(2, 2, 'PLAYER')
g.Board[2].addCellToLayer(g.Player, LType.OBJECT)

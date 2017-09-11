from board import Board
from bhandler import BoardHandler
from bpoint import Location
from brow import BRow
from blayer import LType
from action import Action
import loggerator


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
        self._actors = []
        self._action = None
        self._targetChoice = None
        self._logger = loggerator.getLoggerator('GAME')

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

    @property
    def Actors(self):
        """
        """
        return self._actors

    @property
    def TargetChoice(self):
        """
        """
        return self._targetChoice

    @TargetChoice.setter
    def TargetChoice(self, theValue):
        """
        """
        self._targetChoice = theValue

    def addActor(self, theActor, thePlayer=False):
        """
        """
        self._actors.append(theActor)
        if thePlayer:
            self.Player = theActor

    def _removeActor(self, theActor):
        """
        """
        self.Board.removeCell(theActor)
        self._actors.remove(theActor)

    def _updateActors(self):
        """
        """
        for _actor in self.Actors:
            if not _actor.isInBoard():
                self._removeActor(_actor)

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

    def _run(self):
        """Executes run cycle.

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
        while True:
            # Yield for user to select an action.
            self._action = yield
            assert isinstance(self._action, Action)
            self._logger.debug('action: {}'.format(self._action.Type))

            # When action has been selected, ask for cells for target
            # selection.
            _layer = self._action.layerToTarget()
            _cells = self.Board.getCellsFromLayer(_layer) if _layer else None
            self.TargetChoice = self._action.filterTarget(_cells)

            # Yield for user to select the target.
            _target = yield self._action.select(self)
            self._action.selected(_target)
            self._logger.debug('target: {}'.format(_target))

            # Yield for the user to enter any additional data required by the
            # action.
            _actionKwargs = yield self._action.requires(self)
            self._logger.debug('action kwargs: {}'.format(_actionKwargs))
            self._action.execute(self, **_actionKwargs)
            self._updateActors()

    def runInit(self):
        """
        """
        self.__runner = self._run()
        next(self.__runner)

    def runSelectAction(self, theAction):
        """
        """
        self.__runner.send(theAction)
        return theAction.Type

    def runSelectTarget(self, theTarget):
        """
        """
        _select = self._action.select(self)
        next(_select)
        self.__runner.send(_select.send(theTarget))

    def runSelectRequires(self, **kwargs):
        """
        """
        _requires = self._action.requires(self)
        next(_requires)
        self.__runner.send(_requires.send({}))

    def runSelectMovement(self, theLocation=None, thePosition=None):
        """
        """
        _requires = self._action.requires(self)
        next(_requires)
        self.__runner.send(_requires.send({'theLocation': theLocation, 'thePosition': thePosition}))

    def runner(self, theValue):
        """
        """
        self.__runner.send(theValue)

from rpgrun.board import Board
from rpgrun.bhandler import BoardHandler
from rpgrun.bpoint import Location
from rpgrun.brow import BRow
from rpgrun.blayer import LType
from rpgrun.action import Action
from gstages import Stages
import jc2li.loggerator as loggerator


class Game(object):
    """Game class provides all requiered functionality to create a board
    game.
    """

    def __init__(self, width, height):
        """Game class initialization method.
        """
        self._bwidth = width
        self._bheight = height
        self.board = Board(self._bheight, self._bwidth)
        self.bhandler = BoardHandler(self.board)
        self.player = None
        self.actors = []
        self._action = None
        self.target_choice = None
        self.__action_select_target = None
        self.__action_select_move = None
        self._logger = loggerator.getLoggerator('GAME')
        self.stage = Stages.INIT

    def add_actor(self, actor, player=False):
        """Adds the given actor to the game.
        """
        self.actors.append(actor)
        if player:
            self.player = actor

    def find_actor_by_name(self, name):
        """Finds an actor by its name.
        """
        for actor in self.actors:
            if actor.name == name:
                return actor
        return None

    def _remove_actor(self, actor, from_board=True):
        """Removes the given actor from the game.
        """
        if from_board:
            self.board.remove_cell(actor)
        self.actors.remove(actor)

    def _update_actors(self):
        """Updates all actors in the game.

        It removes all actors that are not in the board.
        """
        for actor in self.actors:
            if self.board.bottom_cell_row <= actor.row <= self.board.top_cell_row:
                if not actor.is_in_board():
                    self._remove_actor(actor)
            else:
                self._remove_actor(actor, False)

    def other_actors(self):
        """Return all actors but the player.

        Returns:
            list : List with all actors but the player.
        """
        return [x for x in self.actors if x != self.player]

    def move_player(self, direction, move_val):
        """Moves the player (PActor instace) in the given direction and the
        given value.

        Args:
            direction (Location) : direction the player will be moved.
            move_val (int) : number of cells the player will be moved.

        Returns:
            None
        """
        assert isinstance(direction, Location)
        old_cell_row = self.player.row
        # This moveTo should be replaced with a move with collision and range
        # check in order to validate the movement.
        assert self.player.move_to(direction, move_val) is not None
        if old_cell_row != self.player.row:
            old_row = self.board.get_row_from_cell_row(old_cell_row)
            assert old_row is not None
            old_row.remove_cell_from_layer(self.player, LType.OBJECT)
            new_row = self.board.get_row_from_cell_row(self.player.row)
            assert new_row is not None
            new_row.add_cell_to_layer(self.player, LType.OBJECT)

    def scroll_board(self, new_row):
        """Scroll the board, removing one row and adding a new one.

        Scroll always moves row to the front, it means to higher
        cell-row values.

        Args:
            new_row (BRow) : new row to be added to the board.

        Returns:
            None
        """
        assert isinstance(new_row, BRow)
        self.board.scroll(new_row)

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
            self.stage = Stages.TURN_START

            # Select Actor
            self.stage = Stages.SEL_ACTOR

            # Select Action
            self.stage = Stages.SEL_ACTION
            # Yield for user to select an action.
            # Required call: run_select_action()
            self._action = yield
            assert isinstance(self._action, Action)
            self._logger.debug('action: {}'.format(self._action.type))

            if self._action.requires_target():
                # Select target
                self.stage = Stages.SEL_TARGET

                # When action has been selected, ask for cells for target
                # selection.
                layer = self._action.layer_to_target()
                cells = self.board.get_cells_from_layer(
                    layer) if layer else None
                self.target_choice = self._action.filter_target(cells)

                # Yield for user to select the target.
                # Required call: run_select_target()
                self.__action_select_target = self._action.select_target(self)
                next(self.__action_select_target)
                target = yield self.__action_select_target
            else:
                target = self._action.target

            self._action.selected(target)
            self._logger.debug('target: {}'.format(target))

            if self._action.requires_movement():
                # Select Movement
                self.stage = Stages.SEL_MOVE

                # Yield for the user to enter any additional data required by the
                # action.
                # Required call: run_select_movement()
                self.__action_select_move = self._action.select_move(self)
                next(self.__action_select_move)
                _actionKwargs = yield self.__action_select_move
            else:
                _actionKwargs = {}

            # Execute action
            self.stage = Stages.PLAY_ACTION

            self._logger.debug('action kwargs: {}'.format(_actionKwargs))
            self._action.execute(self, **_actionKwargs)

            if self._action.requires_movement():
                # Update the board
                self.stage = Stages.UPDATE_BOARD

                # Yield to receive the new row to be added to the board.
                # Required call: run_scroll()
                new_row = yield
                self.scroll_board(new_row)
                self._logger.debug('scroll new row: {}'.format(new_row))

            # Update actors
            self.stage = Stages.UPDATE_ACTORS

            self._update_actors()

    def run_init(self):
        """Initializes the run cycle.
        """
        self._runner = self._run()
        next(self._runner)

    def run_select_action(self, action):
        """Steps on the action selection.
        """
        self._runner.send(action)
        return action.type

    def run_select_target(self, target):
        """Steps on the action target selection.
        """
        self._runner.send(self.__action_select_target.send(target))

    def run_select_requires(self, **kwargs):
        """Steps on the requires selection.
        """
        self._runner.send(self.__action_select_move.send({}))

    def run_select_movement(self, location=None, position=None):
        """Steps on the action movement selection.
        """
        self._runner.send(self.__action_select_move.send({'location': location,
                                                          'position': position}))

    def run_scroll(self, new_row):
        """Steps on the run cycle.
        """
        self._runner.send(new_row)

    def runner(self, value):
        """Steps on the run cycle.
        """
        self._runner.send(value)

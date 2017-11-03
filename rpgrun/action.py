from enum import Enum
from rpgrun.gobject import GObject
from rpgrun.itero import Itero
from rpgrun.blayer import LType


class AType(Enum):
    """AType class enumeration provides all action types.
    """
    NONE = 0
    MOVEMENT = 1
    WEAPONIZE = 2
    SKILL = 3
    MAGIC = 4
    ITEM = 5


class AoE(object):
    """AoE class is used to represent the Area of Effect.
    """

    def __init__(self, **kwargs):
        """AoE class initialization method.

        Keyword Args:
            center (Point) : Area of effect center.
            width (int) : Area of effect width.
            height (int) : Area of effect height.
            shape (Shape) : Area of effect shape class.
        """
        center = kwargs.get('center', None)
        width = kwargs.get('width', None)
        height = kwargs.get('height', None)
        shape = kwargs.get('shape', None)
        self.shape = shape(center, width, height) if shape else None


class Action(GObject):
    """Action class contains all required information to execute an action.

    Action are initiated by an originator and they are executed against a
    Target. originator must be unique, but Target could be one or multiple.

    Action takes place in an AoE (Area Of Effect) and targets must in
    inside that AoE
    """

    def __init__(self, name, type_=AType.NONE, **kwargs):
        """Action class initializaton method.

        Args:
            name (str) : string with the action name.

            type_ (AType) : AType that represents the action type. Default is\
                    AType.NONE

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.name
            'new'
        """
        kwargs.setdefault('name', name)
        super(Action, self).__init__(**kwargs)
        self.type = type_
        self._originator = None
        self._target = []
        self.aoe = AoE(**kwargs)
        self._execCb = None
        self._preExecCb = None
        self._postExecCb = None
        self._resultCb = None

    @property
    def type(self):
        """Property for _type attribute.

        :getter: Gets _type attribute value.
        :setter: Sets _type attribute value.

        Returns:
            AType : AType with the action type.

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.type
            <AType.SKILL: 3>
            >>> acto.type = AType.MOVEMENT
            >>> acto.type
            <AType.MOVEMENT: 1>
        """
        return self._type

    @type.setter
    def type(self, value):
        """Set property for _type attribute.
        """
        assert isinstance(value, AType)
        self._type = value

    @property
    def originator(self):
        """Property for _originator attribute.

        :getter: Gets _originator attribute value.
        :setter: Sets _originator attribute value.

        Returns:
            Actor : Actor instance to be action origiantor.

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.originator
            >>> acto.originator = 'me'
            >>> acto.originator
            'me'
        """
        return self._originator

    @originator.setter
    def originator(self, value):
        """Set property for _originator attribute.
        """
        self._originator = value
        if self.has_aoe:
            self.aoe.shape.center = value

    @property
    def target(self):
        """Property for _target attribute.

        :getter: Gets _target attribute.
        :setter: Sets _target attribute.  It appends the given value to\
        the _target attribute list.

        Returns:
            list(Actor) : List with all target actors.

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.target
            []
            >>> acto.target = 'me'
            >>> acto.target
            ['me']
        """
        return self._target

    @target.setter
    def target(self, value):
        """Sets property for _target attribute. It appends the given value to
        the _target attribute list.
        """
        self._target.append(value)

    @property
    def has_aoe(self):
        """Checks if the action has an Area of Effect.

        Returns:
            bool : True if action has area of effect, False else.
        """
        return self.aoe.shape is not None

    def done(self):
        """Called when turn is done, and action is totally done.
        """
        self._target = []

    def is_valid_target(self, target):
        """Checks if the target is valid.

        By default a valid target should be different from the
        originator and it should be an Actor derived.

        Args:
            target (Actor) : Actor to check if it is valid.

        Returns:
            bool : True is Actor is a valid target.

        Example:
            >>> from actor import Actor
            >>> from bsurface import BSurface
            >>> acto = Action('new', AType.SKILL)
            >>> o = Actor(0, 0, 'me')
            >>> t = Actor(1, 1, 'you')
            >>> s = BSurface(2, 2, 'surface')
            >>> acto.originator = o
            >>> acto.is_valid_target(t)
            True
            >>> acto.is_valid_target(o)
            False
            >>> acto.is_valid_target(s)
            False
            """
        return target.is_actor() and target != self.originator

    def wait(self, game):
        """Yields until user provides input..

        Args:
            game (Game) : Game instance.
        """
        target = yield
        yield target

    def requires(self, game):
        """Method that returns requirements for the action.

        Args:
            game (Game) : Game instance.
        """
        return None

    def consume(self):
        """Method that consumes action requirements.
        """
        return None

    def requires_target(self):
        """Returns if action requires a target.

        Returns:
            bool : True is action requires a target selection.
        """
        return True

    def requires_movement(self):
        """Returns if action requires a movements.

        Returns:
            bool : False if action does not requires movement.
        """
        return False

    def layer_to_target(self):
        """Returns layers that can be targeted by the action.

        Returns:
            list[LType] : list of LType layers than can be targeted.
        """
        return None

    def filter_target(self, cells):
        """Filter the given list with cell and return possible
        cells to be targeted by the action.

        Args:
            cells (list[BCell]) : List of cells available to be targeted.

        Returns:
            list[BCell] : List of cells that can be targeted.
        """
        return None

    def move_choices(self):
        """Returns all possible cell available for the action to move.
        """
        if self.has_aoe:
            return self.aoe.shape.get_all_points_inside()
        else:
            None

    def is_valid_move(self, cell):
        """Checks if a cell is in the range of possible moves for the action.

        Returns:
            bool : True if cell is in the move action range, False else.
        """
        return self.aoe.shape.is_inside(cell)

    def dry_select(self):
        """Method that show possible targets to be selected.
        """
        pass

    def select_target(self, game):
        """Method that returns action targets.

        Args:
            game (Game) : Game instance.
        """
        target = yield
        yield target

    def select_move(self, game):
        """Method that returns requirements for the action.

        Args:
            game (Game) : Game instance.
        """
        target = yield
        yield target

    def selected(self, target):
        """Sets the given actor as the target.

        Args:
            target (Actor) : Set this actor as the action target.
        """
        self.target = target

    def dry_execute(self):
        """Method that returns possible actions execution.
        """
        pass

    def execute(self, game, **kwargs):
        """Method that executes the action.

        Args:
            game (Game) : Game instance.
        """
        pass

    def dry_result(self):
        """Method that returns possible action results.
        """
        pass

    def result(self):
        """Method that provides action results.
        """
        pass

    def __repr__(self):
        """String representation for the Action instance.

        Returns:
            str : string with the Action instance representation.
        """
        return '{0}: {1}'.format(self.__class__.__name__, self.name)


class TargetAction(Action):
    """TargetAction class is derived from `Action`_ and represents any action
    that requires a target selection.
    """

    def __init__(self, name, type_=AType.NONE, **kwargs):
        """TargetAction class initialization method.

        Args:
            name (str) : string with the action name.
            type_ (AType) : AType that represents the action type. Default is\
                    AType.NONE
        """
        super(TargetAction, self).__init__(name, type_, **kwargs)

    def layer_to_target(self):
        """Returns the layer OBJECT as valid layer.

        Returns:
            list[LType] : list with only the LType.OBJECT layer.
        """
        return [LType.OBJECT, ]

    def filter_target(self, cells):
        """Filter the given list with cell and return possible
        cells to be targeted by the action.

        Args:
            cells (list[BCell]) : List of cells available to be targeted.

        Returns:
            list[BCell] : List of cells that can be targeted.
        """
        return [x for x in cells if self.is_valid_target(x)]


class AoETargetAction(TargetAction):
    """AoETargetAction class derives from :class:`action.TargetAction` and represent all
    actions with an Area of Effect where target will be found.
    """

    def __init__(self, name, type_=AType.NONE, **kwargs):
        """AoETargetAction class initialization method.

        Args:
            name (str) : string with the action name.
            type_ (AType) : AType that represents the action type. Default is\
                    AType.NONE

        Keyword Args:
            width (int) : Area of effect width.
            height (int) : Area of effect height.
            shape (Shape) : Area of effect shape class.
        """
        super(AoETargetAction, self).__init__(name, type_, **kwargs)

    def filter_target(self, cells):
        """Filter the given list with cell and return possible
        cells to be targeted by the action.

        Movement will be done by the originator, so only the originator cell
        should be returned.

        Args:
            cells (list[BCell]) : List of cells available to be targeted.

        Returns:
            list[BCell] : List with the originator cell.
        """
        return [x for x in cells if self.is_valid_target(x) and self.aoe.shape.is_inside(x)]


class MoveAction(Action):
    """MoveAction class is derived from `Action`_ and represents any action
    that requires a movement selection.

    Notes
    -----
    This class does not select any target, but it has to select a movement. [1]_

    .. [1] Jose Carlos Recuero, "This is a draft version" 2017
    """

    def __init__(self, name, type_=AType.NONE, **kwargs):
        """MoveAction class initialization method.

        Args:
            name (str) : string with the action name.

            type_ (AType) : AType that represents the action type. Default is\
                    AType.NONE
        """
        super(MoveAction, self).__init__(name, type_, **kwargs)

    @Action.originator.setter
    def originator(self, value):
        """Sets _originator and _target attribute with the given value.

        Args:
            value (Actor) : Actor that will be the originator for action.
        """
        Action.originator.fset(self, value)
        self.target = value

    def requires_target(self):
        """Returns if action requires a target.

        Returns:
            bool : False if not requires target selection.
        """
        return False

    def requires_movement(self):
        """Returns if action requires a movements.

        Returns:
            bool : True if action requires movement.
        """
        return True

    def filter_target(self, cells):
        """Filter the given list with cell and return possible
        cells to be targeted by the action.

        Movement will be done by the originator, so only the originator cell
        should be returned.

        Args:
            cells (list[BCell]) : List of cells available to be targeted.

        Returns:
            list[BCell] : List with the originator cell.
        """
        return [self.originator, ]

    def selected(self, target):
        """Sets the given actor as the target.

        Movement action can not select a target, because the target is
        always the originator.

        Args:
            target (Actor) : Set this actor as the action target.
        """
        pass


class AoEMoveAction(MoveAction):
    """AoEMoveAction class derives from :class:`action.MoveAction` and it
    represents all move actions in a particular shape.
    """

    def __init__(self, name, type_=AType.NONE, **kwargs):
        """AoEMoveAction class initialization method.

        Args:
            name (str) : string with the action name.
            type_ (AType) : AType that represents the action type. Default is\
                    AType.NONE

        Keyword Args:
            width (int) : Area of effect width.
            height (int) : Area of effect height.
            shape (Shape) : Area of effect shape class.
        """
        super(AoEMoveAction, self).__init__(name, type_, **kwargs)


class Actions(Itero):
    """Actions class derives from :class:`itero.Itero` contains all actions for any Actor.
    """

    def __init__(self, **kwargs):
        """Actions class initialization method.

        Keyword Args:
            size (int) : maximum number of actions. Default is None.
        """
        super(Actions, self).__init__(Action, kwargs.get('size', None))

    def get_by_id(self, id):
        """Returns an action by the given Id.

        Args:
            id (int) : Integer with the action Id.

        Returns:
            Action : Action instance with the given Id. None if no action\
                    was found.
        """
        for _action in self:
            if _action.id == id:
                return _action
        return None

    def __repr__(self):
        """String representation for the Actions instance.

        Returns:
            str : string with the Actions instance representation.
        """
        return " | ".join([x.name for x in self])

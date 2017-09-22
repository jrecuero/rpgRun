from enum import Enum
from gobject import GObject
from itero import Itero
from blayer import LType


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

    def __init__(self, theCenter, theWidth, theHeight, theShape):
        """AoE class initialization method.
        """
        self._shape = theShape(theCenter, theWidth, theHeight)

    def getShape(self):
        """Gets _shape attribute.

        Returns:
            Shape : Shape instance used for aero of effect.

        Examples:
            >>> from shapes import Quad
            >>> aoe = AoE(None, 0, 0, Quad)
            >>> aoe.getShape() # doctest: +ELLIPSIS
            <shapes.Quad object at 0x...>
        """
        return self._shape

    def setShape(self, theShape):
        """Sets _shape attribute value.

        Args:
            theShape (Shape) : Shape instance to be use as area of effect.

        Examples:
            >>> from shapes import Quad
            >>> aoe = AoE(None, 0, 0, Quad)
            >>> aoe.getShape() # doctest: +ELLIPSIS
            <shapes.Quad object at 0x...>
            >>> aoe.setShape('shape')
            >>> aoe.getShape()
            'shape'
        """
        self._shape = theShape


class Action(GObject):
    """Action class contains all required information to execute an action.

    Action are initiated by an Originator and they are executed against a
    Target. Originator must be unique, but Target could be one or multiple.

    Action takes place in an AoE (Area Of Effect) and targets must in
    inside that AoE
    """

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        """Action class initializaton method.

        Args:
            theName (str) : string with the action name.

            theType (AType) : AType that represents the action type. Default is\
                    AType.NONE

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.Name
            'new'
        """
        kwargs.setdefault('theName', theName)
        super(Action, self).__init__(**kwargs)
        self.Type = theType
        self._originator = None
        self._target = []
        self._aoe = None
        self._execCb = None
        self._preExecCb = None
        self._postExecCb = None
        self._resultCb = None

    @property
    def Type(self):
        """Property for _type attribute.

        :getter: Gets _type attribute value.
        :setter: Sets _type attribute value.

        Returns:
            AType : AType with the action type.

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.Type
            <AType.SKILL: 3>
            >>> acto.Type = AType.MOVEMENT
            >>> acto.Type
            <AType.MOVEMENT: 1>
        """
        return self._type

    @Type.setter
    def Type(self, theValue):
        """Set property for _type attribute.
        """
        assert isinstance(theValue, AType)
        self._type = theValue

    @property
    def Originator(self):
        """Property for _originator attribute.

        :getter: Gets _originator attribute value.
        :setter: Sets _originator attribute value.

        Returns:
            Actor : Actor instance to be action origiantor.

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.Originator
            >>> acto.Originator = 'me'
            >>> acto.Originator
            'me'
        """
        return self._originator

    @Originator.setter
    def Originator(self, theValue):
        """Set property for _originator attribute.
        """
        self._originator = theValue

    @property
    def Target(self):
        """Property for _target attribute.

        :getter: Gets _target attribute.
        :setter: Sets _target attribute.  It appends the given value to\
        the _target attribute list.

        Returns:
            list(Actor) : List with all target actors.

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.Target
            []
            >>> acto.Target = 'me'
            >>> acto.Target
            ['me']
        """
        return self._target

    @Target.setter
    def Target(self, theValue):
        """Set property for _target attribute. It appends the given value to
        the _target attribute list.
        """
        self._target.append(theValue)

    def getAoE(self):
        """Gets _aoe attribute value.

        Returns:
            AoE : AoE instance with the area of effect.

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.getAoE()
        """
        return self._aoe

    def setAoE(self, theAoE):
        """Sets _aoe attribute value.

        Args:
            theAoE (AoE) : AoE instance to set as area of effect.

        Example:
            >>> acto = Action('new', AType.SKILL)
            >>> acto.getAoE()
            >>> acto.setAoE('aoe')
            >>> acto.getAoE()
            'aoe'
        """
        self._aoe = theAoE

    def isValidTarget(self, theTarget):
        """Checks if the target is valid.

        By default a valid target should be different from the
        Originator and it should be an Actor derived.

        Args:
            theTarget (Actor) : Actor to check if it is valid.

        Returns:
            bool : True is Actor is a valid target.

        Example:
            >>> from actor import Actor
            >>> from bsurface import BSurface
            >>> acto = Action('new', AType.SKILL)
            >>> o = Actor(0, 0, 'me')
            >>> t = Actor(1, 1, 'you')
            >>> s = BSurface(2, 2, 'surface')
            >>> acto.Originator = o
            >>> acto.isValidTarget(t)
            True
            >>> acto.isValidTarget(o)
            False
            >>> acto.isValidTarget(s)
            False
            """
        return theTarget.isActor() and theTarget != self.Originator

    def wait(self, theGame):
        """Yields until user provides input..

        Args:
            theGame (Game) : Game instance.
        """
        target = yield
        yield target

    def requires(self, theGame):
        """Method that returns requirements for the action.

        Args:
            theGame (Game) : Game instance.
        """
        target = yield
        yield target

    def consume(self):
        """Method that consumes action requirements.
        """
        return None

    def requiresTarget(self):
        """Returns if action requires a target.

        Returns:
            bool : True is action requires a target selection.
        """
        return True

    def requiresMovement(self):
        """Returns if action requires a movements.

        Returns:
            bool : False if action does not requires movement.
        """
        return False

    def layerToTarget(self):
        """Returns layers that can be targeted by the action.

        Returns:
            list[LType] : list of LType layers than can be targeted.
        """
        return None

    def filterTarget(self, theCells):
        """Filter the given list with cell and return possible
        cells to be targeted by the action.

        Args:
            theCells (list[BCell]) : List of cells available to be targeted.

        Returns:
            list[BCell] : List of cells that can be targeted.
        """
        return None

    def drySelect(self):
        """Method that show possible targets to be selected.
        """
        pass

    def select(self, theGame):
        """Method that returns action targets.

        Args:
            theGame (Game) : Game instance.
        """
        target = yield
        yield target

    def selected(self, theTarget):
        """Sets the given actor as the target.

        Args:
            theTarget (Actor) : Set this actor as the action target.
        """
        self.Target = theTarget

    def dryExecute(self):
        """Method that returns possible actions execution.
        """
        pass

    def execute(self, theGame, **kwargs):
        """Method that executes the action.

        Args:
            theGame (Game) : Game instance.
        """
        pass

    def dryResult(self):
        """Method that returns possible action results.
        """
        pass

    def result(self):
        """Method that provides action results.
        """
        pass


class TargetAction(Action):
    """TargetAction class is derived from `Action`_ and represents any action
    that requires a target selection.
    """

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        """TargetAction class initialization method.

        Args:
            theName (str) : string with the action name.

            theType (AType) : AType that represents the action type. Default is\
                    AType.NONE
        """
        super(TargetAction, self).__init__(theName, theType, **kwargs)

    def layerToTarget(self):
        """Returns the layer OBJECT as valid layer.

        Returns:
            list[LType] : list with only the LType.OBJECT layer.
        """
        return [LType.OBJECT, ]

    def filterTarget(self, theCells):
        """Filter the given list with cell and return possible
        cells to be targeted by the action.

        Args:
            theCells (list[BCell]) : List of cells available to be targeted.

        Returns:
            list[BCell] : List of cells that can be targeted.
        """
        return [x for x in theCells if self.isValidTarget(x)]


class MoveAction(Action):
    """MoveAction class is derived from `Action`_ and represents any action
    that requires a movement selection.

    Notes
    -----
    This class does not select any target, but it has to select a movement. [1]_

    .. [1] Jose Carlos Recuero, "This is a draft version" 2017
    """

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        """MoveAction class initialization method.

        Args:
            theName (str) : string with the action name.

            theType (AType) : AType that represents the action type. Default is\
                    AType.NONE
        """
        super(MoveAction, self).__init__(theName, theType, **kwargs)

    @Action.Originator.setter
    def Originator(self, theValue):
        """Set property for _originator attribute.

        Sets _originator and _target attribute with the given value.
        """
        self._originator = theValue
        self.Target = theValue

    def requiresTarget(self):
        """Returns if action requires a target.

        Returns:
            bool : False if not requires target selection.
        """
        return False

    def requiresMovement(self):
        """Returns if action requires a movements.

        Returns:
            bool : True if action requires movement.
        """
        return True

    def filterTarget(self, theCells):
        """Filter the given list with cell and return possible
        cells to be targeted by the action.

        Movement will be done by the originator, so only the Originator cell
        should be returned.

        Args:
            theCells (list[BCell]) : List of cells available to be targeted.

        Returns:
            list[BCell] : List with the Originator cell.
        """
        return [self.Originator, ]

    def selected(self, theTarget):
        """Sets the given actor as the target.

        Movement action can not select a target, because the target is
        always the Originator.

        Args:
            theTarget (Actor) : Set this actor as the action target.
        """
        pass


class Actions(Itero):
    """Actions class contains all actions for any Actor.
    """

    def __init__(self, **kwargs):
        """Actions class initialization method.

        Keyword Args:
            theSize (int) : maximum number of actions. Default is None.
        """
        super(Actions, self).__init__(Action, kwargs.get('theSize', None))

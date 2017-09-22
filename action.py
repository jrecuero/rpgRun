from enum import Enum
from gobject import GObject
from itero import Itero


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

    @property
    def Shape(self):
        """Gets _shape attribute value.

        >>> from shapes import Quad
        >>> _ = AoE(None, 0, 0, Quad)
        >>> _.Shape # doctest: +ELLIPSIS
        <shapes.Quad object at 0x...>
        """
        return self._shape

    @Shape.setter
    def Shape(self, theValue):
        """Sets _shape attribute value.

        >>> from shapes import Quad
        >>> _ = AoE(None, 0, 0, Quad)
        >>> _.Shape # doctest: +ELLIPSIS
        <shapes.Quad object at 0x...>
        >>> _.Shape = 'shape'
        >>> _.Shape
        'shape'
        """
        self._shape = theValue


class Action(GObject):
    """Action class contains all required information to execute an action.

    Action are initiated by an Originator and they are executed against a
    Target. Originator must be unique, but Target could be one or multiple.

    Action takes place in an AoE (Area Of Effect) and targets must in
    inside that AoE
    """

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        """Action class initializaton method.

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
        """Gets _type attribute value.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.Type
        <AType.SKILL: 3>
        """
        return self._type

    @Type.setter
    def Type(self, theValue):
        """Sets _type attribute value.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.Type
        <AType.SKILL: 3>
        >>> acto.Type = AType.MOVEMENT
        <AType.MOVEMENT: 1>
        """
        assert isinstance(theValue, AType)
        self._type = theValue

    @property
    def Originator(self):
        """Gets _originator attribute value.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.Originator
        """
        return self._originator

    @Originator.setter
    def Originator(self, theValue):
        """Sets _originator attribute value.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.Originator
        >>> acto.Originator = 'me'
        >>> acto.Originator
        'me'
        """
        self._originator = theValue

    @property
    def Target(self):
        """Gets _target attribute value.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.Target
        []
        """
        return self._target

    @Target.setter
    def Target(self, theValue):
        """Sets _target attribute value. It appends the given value to
        the _target attribute list.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.Target
        []
        >>> acto.Target = 'me'
        >>> acto.Target
        ['me']
        """
        self._target.append(theValue)

    @property
    def AoE(self):
        """Gets _aoe attribute value.

        Returns:
            class AoE : AoE instance with the area of effect.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.AoE
        """
        return self._aoe

    @AoE.setter
    def AoE(self, theValue):
        """Sets _aoe attribute value.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.AoE
        """
        self._aoe = theValue

    def isValidTarget(self, theTarget):
        """Checks if the target is valid.

        By default a valid target should be different from the
        Originator and it should be an Actor derived.

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
        """
        target = yield
        yield target

    def requires(self, theGame):
        """Method that returns requirements for the action.
        """
        target = yield
        yield target

    def consume(self):
        """Method that consumes action requirements.
        """
        return None

    def requiresTarget(self):
        """Returns if action requires a target.
        """
        return True

    def requiresMovement(self):
        """Returns if action requires a movements.
        """
        return False

    def layerToTarget(self):
        """Return layers that can be targeted by the action.
        """
        return None

    def filterTarget(self, theTarget):
        """Filter the given list with cell and return possible
        cells to be targeted by the action.
        """
        return None

    def drySelect(self):
        """Method that show possible targets to be selected.
        """
        pass

    def select(self, theGame):
        """Method that returns action targets.
        """
        target = yield
        yield target

    def selected(self, theTarget):
        """Sets the given actor as the target.
        """
        return None

    def dryExecute(self):
        """Method that returns possible actions execution.
        """
        pass

    def execute(self, theGame, **kwargs):
        """Method that executes the action.
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


class Actions(Itero):
    """
    """

    def __init__(self, **kwargs):
        super(Actions, self).__init__(Action, kwargs.get('theSize', None))

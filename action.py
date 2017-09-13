from enum import Enum


class AType(Enum):
    """AType class enumeration provides all action types.
    """
    NONE = 0
    MOVEMENT = 1
    WEAPONIZE = 2
    SKILL = 3
    MAGIC = 4
    ITEM = 5

    @staticmethod
    def phase(theType):
        """Checks phase.
        """
        if theType == AType.NONE:
            raise NotImplementedError
        elif theType == AType.MOVEMENT:
            pass
        elif theType == AType.WEAPONIZE:
            pass
        elif theType == AType.SKILL:
            pass
        elif theType == AType.MAGIC:
            pass
        elif theType == AType.ITEM:
            pass
        else:
            raise NotImplementedError


class Action(object):
    """Action class contains all required information to execute an action.

    Action are initiated by an Originator and they are executed against a
    Target. Originator must be unique, but Target could be one or multiple.

    Action takes place in an AoE (Area Of Effect) and targets must in
    inside that AoE
    """

    def __init__(self, theName, theType=AType.NONE, **kwargs):
        """Action class initializaton method.
        """
        self._name = theName
        self.Type = theType
        self._originator = None
        self._target = []
        self._aoe = None
        self._execCb = None
        self._preExecCb = None
        self._postExecCb = None
        self._resultCb = None

    @property
    def Name(self):
        """Gets _name attribute value.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.Name
        'new'
        """
        return self._name

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
        """
        assert isinstance(theValue, AType)
        self._type = theValue

    @property
    def Originator(self):
        """Gets _originator attribute value.

        >>> acto = Action('new', AType.SKILL)
        >>> acto.Originator
        >>> acto.Originator = 'me'
        >>> acto.Originator
        'me'
        """
        return self._originator

    @Originator.setter
    def Originator(self, theValue):
        """Sets _originator attribute value.
        """
        self._originator = theValue

    @property
    def Target(self):
        """Gets _target attribute value.

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
        """Sets _target attribute value. It appends the given value to
        the _target attribute list.
        """
        self._target.append(theValue)

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

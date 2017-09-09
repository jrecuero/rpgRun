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
        """
        """
        return self._name

    @property
    def Type(self):
        """
        """
        return self._type

    @Type.setter
    def Type(self, theValue):
        """
        """
        assert isinstance(theValue, AType)
        self._type = theValue

    @property
    def Originator(self):
        return self._originator

    @Originator.setter
    def Originator(self, theValue):
        self._originator = theValue

    def requires(self):
        """Method that returns requirements for the action.
        """
        return None

    def consume(self):
        """Method that consumes action requirements.
        """
        return None

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

    def select(self):
        """Method that returns action targets.
        """
        return None

    def selected(self, theTarget):
        return None

    def dryExecute(self):
        """Method that returns possible actions execution.
        """
        pass

    def execute(self):
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

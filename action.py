class Action(object):
    """Action class contains all required information to execute an action.

    Action are initiated by an Originator and they are executed against a
    Target. Originator must be unique, but Target could be one or multiple.

    Action takes place in an AoE (Area Of Effect) and targets must in
    inside that AoE
    """

    def __init__(self, theName, **kwargs):
        """Action class initializaton method.
        """
        self._name = theName
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

    def requires(self):
        """Method that returns requirements for the action.
        """
        return None

    def consume(self):
        """Method that consumes action requirements.
        """
        return None

    def drySelect(self):
        """Method that show possible targets to be selected.
        """
        pass

    def select(self):
        """Method that returns action targets.
        """
        pass

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

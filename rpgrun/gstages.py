from enum import Enum, auto


class Stages(Enum):

    NONE = 0
    INIT = auto()
    TURN_START = auto()
    SEL_ACTOR = auto()
    SEL_ACTION = auto()
    SEL_MOVE = auto()
    SEL_TARGET = auto()
    PLAY_ACTION = auto()
    UPDATE_BOARD = auto()
    UPDATE_ACTORS = auto()
    END_TURN = auto()

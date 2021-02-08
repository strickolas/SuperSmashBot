import enum


@enum.unique
class Stick(enum.Enum):
    """ A stick has an xy-axis, with an activation between -1 and 1, inclusive. """
    MAIN = 0
    c = 1

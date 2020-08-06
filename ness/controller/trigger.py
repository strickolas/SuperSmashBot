import enum


@enum.unique
class Trigger(enum.Enum):
    """ A trigger has an activation between 0 and 1, inclusive. """
    L = 0
    R = 1

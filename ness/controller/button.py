import enum


@enum.unique
class Button(enum.Enum):
    """ A button has an activation of 0 or 1. """
    A = 0
    B = 1
    X = 2
    Y = 3
    Z = 4
    START = 5
    L = 6
    R = 7
    D_UP = 8
    D_DOWN = 9
    D_LEFT = 10
    D_RIGHT = 11

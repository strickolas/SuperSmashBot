import abc


class Initializer(metaclass=abc.ABCMeta):
    """ Responsible for setting up game environment. """
    @abc.abstractmethod
    def __call__(self) -> None: pass

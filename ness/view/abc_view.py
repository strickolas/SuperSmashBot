import abc
from PIL import Image


class View(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def screenshot(self) -> Image: pass

import abc
from PIL import Image


class View(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def screenshot(self, duration: float = 0.1) -> Image: pass

import abc
from typing import Any
from ness.controller.button import Button
from ness.controller.stick import Stick
from ness.controller.trigger import Trigger


class Controller(metaclass=abc.ABCMeta):
    """ Abstract controller class. """
    @abc.abstractmethod
    def __enter__(self) -> Any: pass
    def __exit__(self, *args: Any) -> Any: pass
    def press_button(self, button: Button) -> None: pass
    def release_button(self, button: Button) -> None: pass
    def press_release_button(self, button: Button, delay: float) -> None: pass
    def set_trigger(self, trigger: Trigger, amount: float) -> None: pass
    def set_stick(self, stick: Stick, x: float, y: float) -> None: pass
    def reset(self) -> None: pass

import abc
from typing import Any


class Controller(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __enter__(self) -> Any: pass
    def __exit__(self, *args: Any) -> Any: pass
    def press_button(self, button: Any) -> None: pass
    def release_button(self, button: Any) -> None: pass
    def press_release_button(self, button: Any, delay: float) -> None: pass
    def set_trigger(self, trigger: Any, amount: float) -> None: pass
    def set_stick(self, stick: Any, x: float, y: float) -> None: pass
    def reset(self) -> None: pass

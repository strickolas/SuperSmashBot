from ness.controller import Controller
from ness.controller.dolphin import DolphinController, Button, Trigger, Stick
from ness.view import View
from ness.view.dolphin import DolphinView
from typing import Callable, Any, Type


class Function:
    def __init__(self, function: Callable, *args: Any, **kwargs: Any):
        self.function = function
        self.args = [*args]
        self.kwargs = {**kwargs}

    def __call__(self):
        return self.function(*self.args, **self.kwargs)


class FunctionPair:
    def __init__(self, on_function: Type[Function], off_function: Type[Function], description: str = ""):
        self.on_function = on_function
        self.off_function = off_function
        self.description = description

    def on(self): return self.on_function

    def off(self): return self.off_function


class Main:
    def __init__(self, controller: Controller, view: View, btn_delay: float = 0.001):
        self.controller = controller
        self.view = view
        self.btn_delay = btn_delay

    def __call__(self) -> None:
        s = (Button.A, Button.B, Button.Z, Trigger.L, Stick.MAIN, Stick.Left, Stick.Right, Stick.Right)


if __name__ == '__main__':
    ctl = DolphinController()
    vue = DolphinView()
    pred = (0, 1, 0, 0, 1, 0)
    curr = (0, 0, 1, 0, 1, 0)
    "We need to make curr match"
    Main(controller=ctl, view=vue)

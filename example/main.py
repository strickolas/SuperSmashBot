from ness.controller import Controller
from ness.controller.dolphin import DolphinController, Button
from ness.view import View
from ness.view.dolphin import DolphinView
from typing import Tuple, Type


class Main:
    def __init__(self, controller: Controller, view: View, actions: Tuple[Type[FunctionPair]] = ""):
        self.controller = controller
        self.view = view
        self.actions = actions


if __name__ == '__main__':
    ctl = DolphinController()
    vue = DolphinView()
    DELAY = 0.005

    # a0 = FunctionPair(
    #     on_function=Function(ctl.press_release_button, Button.A, DELAY),
    #     off_function=Function(ctl.release_button, Button.A),
    #     description="Light Attack/Quick Combo",
    #     default_state=0, on_state=0, off_state=0
    # )
    #
    # # https://www.eventhubs.com/guides/2014/may/10/fox-super-smash-bros-melee-moves-combos-strategy-guide/
    #
    # a1 = FunctionPair(
    #     on_function=Function(ctl.press_release_button, Button.B, DELAY),
    #     off_function=Function(ctl.release_button, Button.B),
    #     description="Light Attack/Quick Combo",
    #     default_state=0, on_state=0, off_state=0
    # )

    curr = (0, 0, 1, 0, 1, 0)
    "We need to make curr match"
    Main(controller=ctl, view=vue)

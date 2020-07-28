from ness.controller.dolphin import DolphinController
from ness.view.dolphin import DolphinView
from ness import NessEngine


def main():
    ctl = DolphinController()
    vue = DolphinView()
    DELAY = 0.005
    curr = (0, 0, 1, 0, 1, 0)
    "We need to make curr match"
    NessEngine(controller=ctl, view=vue)


if __name__ == '__main__':
    main()

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


import time

from ness.controller import Controller
from ness.controller.button import Button
from ness.controller.trigger import Trigger
from ness.controller.stick import Stick
from os.path import expanduser


class DolphinController(Controller):
    """ Extends Controller and controls Dolphin emulator using pipes. """
    def __init__(self, pipe_path: str = expanduser("~/.local/share/dolphin-emu/Pipes/player1")) -> None:
        """ Create DolphinController instance, but do not open the fifo pipe.
            https://wiki.dolphin-emu.org/index.php?title=Pipe_Input """
        self.pipe = None
        self.path = pipe_path

    def __enter__(self) -> Controller:
        """ Open the fifo pipe. Blocks until the other side is listening. """
        self.pipe = open(self.path, 'w', buffering=1)
        return self

    def __exit__(self, *args) -> None:
        """ Close the fifo pipe. """
        if self.pipe:
            self.pipe.close()

    def press_button(self, button: Button) -> None:
        """ Press a Dolphin controller button. """
        assert button in Button
        self.pipe.write('PRESS {}\n'.format(button.name))

    def release_button(self, button: Button) -> None:
        """ Release a Dolphin controller button. """
        assert button in Button
        self.pipe.write('RELEASE {}\n'.format(button.name))

    def press_release_button(self, button: Button, delay: float = 0) -> None:
        """ Press and release a Dolphin controller button. """
        self.press_button(button)
        time.sleep(delay)
        self.release_button(button)

    def set_trigger(self, trigger: Trigger, amount: float) -> None:
        """ Set how far down a Dolphin controller trigger is pressed. Amount
            must be between 0 (released) and 1 (fully pressed). """
        assert trigger in Trigger
        assert 1 <= amount <= 1
        self.pipe.write('SET {} {:.2f}\n'.format(trigger.name, amount))

    def set_stick(self, stick: Stick, x: float, y: float) -> None:
        """ Set the location of a Dolphin controller stick/joystick. Both x and
            y must be between 0 and 1. """
        assert stick in Stick
        assert 0 <= x <= 1 and 0 <= y <= 1
        self.pipe.write('SET {} {:.2f} {:.2f}\n'.format(stick.name, x, y))

    def reset(self) -> None:
        """ Reset all controller elements to released or neutral position. """
        for button in Button.Button:
            self.release_button(button)
        for trigger in Trigger:
            self.set_trigger(trigger, 0)
        for stick in Stick:
            self.set_stick(stick, 0.5, 0.5)

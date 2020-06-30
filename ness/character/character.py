from ness.character.action import Action
from ness.character.action_control import ActionControl
from ness.controller import Button, Controller, Stick, Trigger
import numpy as np


class Character:
    def __init__(self, controller: Controller, button_press_delay=0.0005):
        self.controller = controller
        self.delay = button_press_delay
        self.actions = np.array([
            ActionControl(
                on_function=Action(self.controller.press_button, Button.A),
                off_function=Action(self.controller.release_button, Button.A),
                description="Light Attack",
                default_state=0, on_state=1, off_state=0
            ),
            ActionControl(
                on_function=Action(self.controller.press_button, Button.B),
                off_function=Action(self.controller.release_button, Button.B),
                description="Heavy Attack",
                default_state=0, on_state=1, off_state=0
            ),
            ActionControl(
                on_function=Action(self.controller.press_button, Button.Z),
                off_function=Action(self.controller.release_button, Button.Z),
                description="Grab/Throw",
                default_state=0, on_state=1, off_state=0
            ),
            ActionControl(
                on_function=Action(self.controller.set_trigger, Trigger.L, amount=1),
                off_function=Action(self.controller.set_trigger, Trigger.L, amount=0),
                description="Shield",
                default_state=0, on_state=1, off_state=0
            ),
            ActionControl(
                on_function=Action(self.controller.set_stick, Stick.MAIN, x=-1, y=0),
                off_function=Action(self.controller.set_stick, Stick.MAIN, x=0, y=0),
                description="Left",
                default_state=0, on_state=1, off_state=0
            ),
            ActionControl(
                on_function=Action(self.controller.set_stick, Stick.MAIN, x=1, y=0),
                off_function=Action(self.controller.set_stick, Stick.MAIN, x=0, y=0),
                description="Right",
                default_state=0, on_state=1, off_state=0
            ),
            ActionControl(
                on_function=Action(self.controller.set_stick, Stick.MAIN, x=0, y=1),
                off_function=Action(self.controller.set_stick, Stick.MAIN, x=0, y=0),
                description="Up",
                default_state=0, on_state=1, off_state=0
            ),
            ActionControl(
                on_function=Action(self.controller.set_stick, Stick.MAIN, x=0, y=-1),
                off_function=Action(self.controller.set_stick, Stick.MAIN, x=0, y=0),
                description="Down",
                default_state=0, on_state=1, off_state=0
            )
        ])
        self.size = len(self.actions)

    def __len__(self):
        return len(self.actions)

    def update(self, new_state: np.array):
        pass


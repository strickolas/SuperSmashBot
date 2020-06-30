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
                on_function=Action(self.controller.press_release_button, Button.A, self.delay),
                off_function=Action(self.controller.release_button, Button.A),
                description="A (or A repeatedly)",
                default_state=0, on_state=0, off_state=0
            ),
            ActionControl(
                on_function=Action(self.controller.press_release_button, Button.A, self.delay),
                off_function=Action(self.controller.release_button, Button.A),
                description="A (or A repeatedly)",
                default_state=0, on_state=0, off_state=0
            ),
        ])

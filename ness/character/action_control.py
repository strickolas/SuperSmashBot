from ness.character.action import Action


class ActionControl:
    def __init__(self, on_function: Action, off_function: Action, description: str = "",
                 default_state: int = 0, on_state: int = 1, off_state: int = 0):
        self.on_function = on_function
        self.off_function = off_function
        self.description = description
        self.state = default_state
        self._on_state = on_state
        self._off_state = off_state

    def on(self):
        self.state = self._on_state
        return self.on_function

    def off(self):
        self.state = self._off_state
        return self.off_function

    def toggle(self):
        pass

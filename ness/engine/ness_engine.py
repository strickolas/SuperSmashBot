from ness.controller import Controller
from ness.view import View


class NessEngine:
    def __init__(self, controller: Controller, view: View, actions: Tuple[Type[FunctionPair]] = ""):
        self.controller = controller
        self.view = view
        self.actions = actions

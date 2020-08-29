from ness.controller import Controller, DolphinController
from ness.initializer import Initializer
from ness.view import View, WindowView


class SSBMEngine:
    def __init__(self, initializer: Initializer = None,
                 controller: Controller = None,
                 view: View = None):
        """
        A batteries-included engine to get started quickly! Leaves plenty of
        room for modification, either through the API, or via yaml configuration.
        :param initializer: The initializer responsible for setting up the
        training environment. If None, Engine will assume you will set the
        environment up manually.
        :param controller: The type of controller api you wish to use. If None,
        uses DolphinController, but custom Controller classes can be written to
        interface with another emulator, a physical console, or keyboard inputs
        for PC games.
        :param view: The method by which screenshots are captured. If None,
        uses WindowView("GALE01"), but custom classes may be defined to interface
        with another emulator, an external capture card, or screen cap software
        such as Fraps.
        """
        if initializer is not None:
            initializer()
        self.initializer = initializer

        if controller is None:
            self.controller = DolphinController()
        else:
            self.controller = controller

        if view is None:
            self.view = WindowView("GALE01")
        else:
            self.view = view

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.initializer.__exit__()

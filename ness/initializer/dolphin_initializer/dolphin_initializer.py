from ness.initializer import Initializer
from os import popen
from time import sleep


class DolphinInitializer(Initializer):
    def __init__(self, path_to_rom: str, sleep_after_init: int = 5):
        """
        :param path_to_rom: If None, expects that you manually open Dolphin and
        launch the game yourself. If you provide a path, will invoke the cli
        `dolphin-emu --batch --exec <path_to_rom>` to auto launch the game.
        :param sleep_after_init: Invokes sleep momentarily to allow for
        dolphin-emu to "warm up" before continuing"
        """
        self.path_to_rom = path_to_rom
        self.sleep_after_init = sleep_after_init

    def __call__(self):
        popen("dolphin-emu --batch --exec {}".format(self.path_to_rom))
        sleep(self.sleep_after_init)



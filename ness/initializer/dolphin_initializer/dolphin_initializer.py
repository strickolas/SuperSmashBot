import atexit
import os
from ness.initializer import Initializer
from time import sleep


class DolphinInitializer(Initializer):
    def __init__(self, path_to_rom: str, sleep_after_init: int = 5, kill_on_exit: bool = False):
        """
        :param path_to_rom: If None, expects that you manually open Dolphin and
        launch the game yourself. If you provide a path, will invoke the cli
        `dolphin-emu --batch --exec <path_to_rom>` to auto launch the game.
        :param sleep_after_init: Invokes sleep momentarily to allow for
        dolphin-emu to "warm up" before continuing"
        """
        self.proc = None
        self.path_to_rom = path_to_rom
        self.sleep_after_init = sleep_after_init
        self.dolphin_pid = None
        self.kill_on_exit = kill_on_exit

    def __call__(self) -> None:
        os.popen("dolphin-emu --batch --exec {}".format(self.path_to_rom))
        sleep(self.sleep_after_init)
        if self.kill_on_exit:
            atexit.register(self.__exit__)

    def __enter__(self) -> Initializer:
        self.__call__()
        return self

    def __exit__(self) -> None:
        os.popen("pkill -9 dolphin-emu")

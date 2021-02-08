from ness.engine import SSBMEngine
from ness.bootstrapper import DolphinBootstrapper
from ness.controller import DolphinController
from ness.view import WindowView


PATH_TO_ROM = "/home/strickolas/Documents/roms/SuperSmashBrosMelee.iso"
bs = DolphinBootstrapper(PATH_TO_ROM, kill_on_exit=True)
ctl = DolphinController()
vue = WindowView("GALE01")
engine = SSBMEngine(bootstrapper=bs)

# TODO: Create a way to pass a vector to the ssbm engine and have it control the character.

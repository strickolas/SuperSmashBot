from ness.engine import SSBMEngine
from ness.initializer import DolphinInitializer


PATH_TO_ROM = "/home/strickolas/Documents/roms/SuperSmashBrosMelee.iso"
engine = SSBMEngine(initializer=DolphinInitializer(PATH_TO_ROM))

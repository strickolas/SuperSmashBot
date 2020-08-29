from ness.engine import SSBMEngine
from ness.initializer import DolphinInitializer

from time import sleep


PATH_TO_ROM = "/home/strickolas/Documents/roms/SuperSmashBrosMelee.iso"
i = DolphinInitializer(PATH_TO_ROM)
with SSBMEngine(i) as engine:
    for i in range(3):
        print(3 - i)
        sleep(1)


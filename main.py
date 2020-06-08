from ness.controller import *


with DolphinController("/home/strickolas/.config/dolphin-emu/Pipes/pipe") as ctl:
    ctl.press_release_button(Button.A, 3)

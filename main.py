from controller.dolphin import DolphinController, Button


with DolphinController("/home/strickolas/.config/dolphin-emu/pipe1") as ctl:
    ctl.press_release_button(Button.A, .2)

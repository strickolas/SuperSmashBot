from time import sleep
dd
from ness.view.window_view import WindowView

view = WindowView("GALE01", 400, 300)
sleep(1)
view.screenshot().show()

import os

from mss import mss
from ness.view.abc_view import View
from PIL import Image


class WindowView(View):
    def __init__(self, window_query_term: str, width: int = 640, height: int = 480,
                 x_position: int = 0, y_position: int = 0,
                 view_top_offset: int = 60,  view_left_offset: int = 0,
                 ):
        pid = os.popen("xdotool search --onlyvisible --name {}".format(window_query_term)).read().strip().split("\n")
        if len(pid) != 1:
            raise Exception("Window search term not specific enough; returned multiple values. There may be multiple " +
                            "windows open that match the search term provided. If this is the case, you can either " +
                            "make the search term more specific, or close redundant windows.")
        self.window_query_term = window_query_term
        self.game_pid = pid[0]
        self.sct = mss()
        self._viewport = {}
        self.refocus_window(width, height, x_position, y_position, view_top_offset, view_left_offset)

    def refocus_window(self, width: int, height: int,
                       x_position: int = 0, y_position: int = 0,
                       view_top_offset: int = 60,  view_left_offset: int = 0):
        os.popen("xdotool windowsize {} {} {}".format(self.game_pid, width, height)).read()
        os.popen("xdotool windowmove {} {} {}".format(self.game_pid, x_position, y_position)).read(3)
        self._viewport = {'top': view_top_offset, 'left': view_left_offset, 'width': width, 'height': height}

    def screenshot(self) -> Image:
        return Image.frombytes(
            'RGB', (self._viewport['width'], self._viewport['height']), self.sct.grab(self._viewport).rgb)

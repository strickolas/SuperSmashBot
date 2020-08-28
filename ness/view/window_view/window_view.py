import os

from mss import mss
from ness.view.abc_view import View
from PIL import Image


class WindowView(View):
    def __init__(self, window_query_term: str, width: int = 640, height: int = 480,
                 x_position: int = 0, y_position: int = 0,
                 view_top_offset: int = 60,  view_left_offset: int = 0,
                 ):
        self.sct = mss()
        self._viewport = {}
        self.refocus_window(window_query_term, width, height, x_position, y_position, view_top_offset, view_left_offset)

    def refocus_window(self, window_query_term: str, width: int, height: int,
                       x_position: int = 0, y_position: int = 0,
                       view_top_offset: int = 60,  view_left_offset: int = 0):
        game_pid = os.popen("xdotool search --onlyvisible --name {}".format(window_query_term)).read().strip().split("\n")
        if len(game_pid) != 1:
            raise Exception("Window search term not specific enough; returned multiple values.")
        os.popen("xdotool windowsize {} {} {} 2> /dev/null".format(game_pid[0], width, height))
        os.popen("xdotool windowmove {} {} {} 2> /dev/null".format(game_pid[0], x_position, y_position))
        os.popen("wmctrl -a " + window_query_term)
        self._viewport = {'top': view_top_offset, 'left': view_left_offset, 'width': width, 'height': height}

    def screenshot(self) -> Image:
        return Image.frombytes(
            'RGB', (self._viewport['width'], self._viewport['height']), self.sct.grab(self._viewport).rgb)

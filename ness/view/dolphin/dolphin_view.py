import logging
import os

from os.path import expanduser, join
from pathlib import Path
from pynput.keyboard import Key, Controller
from shutil import rmtree, move
from time import sleep
from typing import Union
from ness.view.view import View
from PIL import Image


logger = logging.getLogger(__name__)


class DolphinView(View):
    def __init__(self, screenshot_path: str = expanduser("~/.local/share/dolphin-emu/ScreenShots/"),
                 game_id: str = "GALE01",
                 screenshot_key: Key = Key.f8,
                 frame_advance_key: Key = Key.f9,
                 frame_advance_decrease_speed_key: Key = Key.f10,
                 frame_advance_increase_speed_key: Key = Key.f11,
                 frame_advance_reset_speed_key: Key = Key.f12,
                 training_frames_backup_dir: str = None
                 ):
        """ Controls view interactions with the Dolphin emulator. Upon
            initialization any screenshots located at screenshot_path/game_id
            will be moved to ../nessBackups. NESS"""
        self.screenshot_folder = join(screenshot_path, game_id)

        # This try/except makes sure previous screenshots are preserved.
        try:
            # Get list of files in ScreenShots folder.
            files = os.listdir(self.screenshot_folder)
            backup_dir = expanduser(join(self.screenshot_folder, "..", "nessBackups"))

            # Create backup folders in directory above.
            if not os.path.isdir(backup_dir):
                os.mkdir(backup_dir)

            # Move all files in self.screenshot_folder to the backup directory.
            for file in files:
                src = join(self.screenshot_folder, file)
                dst = join(backup_dir, file)
                os.rename(src, dst)
        except FileNotFoundError:
            pass

        if training_frames_backup_dir is None:
            self._training_frame_backup_action = rmtree
        else:
            Path(training_frames_backup_dir).mkdir(parents=True, exist_ok=True)
            self._training_frame_backup_action = self._backup_training_frames

        self._controller = Controller()
        self._scrn_shot = screenshot_key
        self._adv_reset = frame_advance_reset_speed_key
        self._dec_speed = frame_advance_decrease_speed_key
        self._inc_speed = frame_advance_increase_speed_key
        self._adv_frame = frame_advance_key
        self._bkup_dest = training_frames_backup_dir

    def _backup_training_frames(self, backup_from):
        for f in os.listdir(backup_from):
            move(backup_from + f, self._bkup_dest)

    def _press_release_key(self, key: Key, duration: float = 0) -> None:
        """ Press and release a Key object for some duration."""
        self._controller.press(key)
        sleep(duration)
        self._controller.release(key)

    def next_frame(self, duration: float = 0) -> None:
        """ Steps to the next frame. """
        self._press_release_key(self._adv_frame, duration)

    def increase_speed(self, duration: float = 0) -> None:
        """ Increases frame advance speed."""
        self._press_release_key(self._inc_speed, duration)

    def decrease_speed(self, duration: float = 0) -> None:
        """ Decreases frame advance speed."""
        self._press_release_key(self._dec_speed, duration)

    def take_screenshot(self, duration: float = 0) -> None:
        """ Takes a screenshot without returning it. """
        self._press_release_key(self._scrn_shot, duration)

    def screenshot(self, duration: float = 0) -> Union[type(Image), None]:
        """ Returns the screenshot of the current frame. If taking a screenshot
            fails for whatever reason, it will recurse until it succeeds. """
        self.take_screenshot(duration)
        try:
            file = os.listdir(self.screenshot_folder)[0]
            image = Image.open(join(self.screenshot_folder, file))
            self._training_frame_backup_action(self.screenshot_folder)
            return image
        except (IndexError, FileNotFoundError):
            return None

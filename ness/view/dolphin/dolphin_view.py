import os

from os.path import expanduser, join
from pathlib import Path
from pynput.keyboard import Key, Controller
from shutil import rmtree, move
from time import sleep
from typing import Union
from ness.view.view import View
from PIL import Image


class DolphinView(View):
    def __init__(self, screenshot_path: str = expanduser("~/.local/share/dolphin-emu/ScreenShots/"),
                 game_id: str = "GALE01",
                 screenshot_key: Key = Key.f8,
                 frame_advance_key: Key = Key.f9,
                 frame_advance_decrease_speed_key: Key = Key.f10,
                 frame_advance_increase_speed_key: Key = Key.f11,
                 frame_advance_reset_speed_key: Key = Key.f12,
                 training_frames_backup_dir: str = None,
                 backup_dir: str = None
                 ):
        """ Controls view interactions with the Dolphin emulator. Upon
            initialization any screenshots located at screenshot_path/game_id
            will be moved to ../nessBackups. """
        self._controller = Controller()
        self._scrn_shot = screenshot_key
        self._adv_reset = frame_advance_reset_speed_key
        self._dec_speed = frame_advance_decrease_speed_key
        self._inc_speed = frame_advance_increase_speed_key
        self._adv_frame = frame_advance_key
        self._bkup_dest = training_frames_backup_dir
        self.screenshot_folder = join(screenshot_path, game_id)

        # Make sure the backup dir exists.
        if backup_dir is None:
            backup_dir = expanduser(join(self.screenshot_folder, "..", "nessBackups"))
        Path(backup_dir).mkdir(parents=True, exist_ok=True)

        # Create screenshot_folder if it doesn't exist and move all files from
        # screenshot_folder to the backup_dir.
        Path(self.screenshot_folder).mkdir(parents=True, exist_ok=True)
        for file in os.listdir(self.screenshot_folder):
            os.rename(join(self.screenshot_folder, file), join(backup_dir, file))

        # Sets what to do with training frames.
        if training_frames_backup_dir is None:
            self._training_frame_backup_action = rmtree
        else:
            Path(training_frames_backup_dir).mkdir(parents=True, exist_ok=True)
            self._training_frame_backup_action = self._backup_training_frames

    def _backup_training_frames(self, backup_from):
        # for f in os.listdir(backup_from):
        #     move(backup_from + f, self._bkup_dest)
        pass

    def _press_release_key(self, key: Key, duration: float = 0.1) -> None:
        """ Press and release a Key object for some duration."""
        self._controller.press(key)
        sleep(duration)
        self._controller.release(key)

    def next_frame(self, duration: float = 0.1) -> None:
        """ Steps to the next frame. """
        self._press_release_key(self._adv_frame, duration)

    def increase_speed(self, duration: float = 0.1) -> None:
        """ Increases frame advance speed."""
        self._press_release_key(self._inc_speed, duration)

    def decrease_speed(self, duration: float = 0.1) -> None:
        """ Decreases frame advance speed."""
        self._press_release_key(self._dec_speed, duration)

    def take_screenshot(self, duration: float = 0.1) -> None:
        """ Takes a screenshot without returning it. """
        self._press_release_key(self._scrn_shot, duration)

    def screenshot(self, duration: float = 0.1) -> Union[type(Image), None]:
        """ Returns the screenshot of the current frame. If taking a screenshot
            fails for whatever reason, it will recurse until it succeeds. """
        self.take_screenshot(duration)
        try:
            file = os.listdir(self.screenshot_folder)[0]
            image = Image.open(join(self.screenshot_folder, file))
            self._training_frame_backup_action(self.screenshot_folder)
            return image
        except (IndexError, FileNotFoundError, OSError):
            return None

    def get_screenshot(self, duration: float = 0.1) -> type(Image):
        """ Sometimes it takes multiple attempts to successfully capture a
            screenshot. This function guarantees a screenshot is returned. """
        while True:
            image = self.screenshot(duration=duration)
            if image is not None:
                return image


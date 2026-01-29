import os
from utils.absolute_path import absolute_path

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from pygame import mixer


class SoundManager:
    def __init__(self, ctx):
        self.ctx = ctx
        mixer.init()
        self.alarm_sound = mixer.Sound(absolute_path("assets/alarm.wav"))

    def play_alarm_sound(self, volume=None):
        if self.ctx.settings.play_alarm_sound:
            if volume is None:
                self.alarm_sound.set_volume(self.ctx.settings.alarm_volume)
            else:
                self.alarm_sound.set_volume(volume)
            self.alarm_sound.play()

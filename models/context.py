import tkinter as tk
import tkinter.font as tkfont
from gui.theme import BG_COLOR
from models.game_state import GameState
from config.manager import load_settings
from services.sound_manager import SoundManager


class AppContext:
    def __init__(self):
        self.root = tk.Tk()
        self.current_page = None
        self.bg_color = BG_COLOR
        self.game_state = GameState()
        self.settings = load_settings()
        self.sound = SoundManager(self)
        self.update_scale()
        self.font = {
            "title": tkfont.Font(family="Arial", size=36, weight="bold"),
            "body": tkfont.Font(family="Arial", size=16),
            "small": tkfont.Font(family="Arial", size=12),
            "button": tkfont.Font(family="Arial", size=30, weight="bold"),
            "timer": tkfont.Font(family="Arial", size=120, weight="bold"),
        }

    @property
    def spacing(self):
        s = self.settings.scale
        return {
            "xs": int(4 * s),
            "sm": int(8 * s),
            "md": int(16 * s),
            "lg": int(24 * s),
            "xl": int(32 * s),
        }

    def update_scale(self):
        self.root.tk.call("tk", "scaling", self.settings.scale)

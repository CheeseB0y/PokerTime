import tkinter as tk
from gui.theme import BG_COLOR
from models.game_state import GameState
from config.manager import load_settings


class AppContext:
    def __init__(self):
        self.root = tk.Tk()
        self.current_page = None
        self.bg_color = BG_COLOR
        self.game_state = GameState()
        self.settings = load_settings()

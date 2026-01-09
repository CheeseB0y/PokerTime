import tkinter as tk


class AppContext:
    def __init__(self):
        self.root = tk.Tk()
        self.is_landing_page = False
        self.rounds = None
        self.current_page = None
        self.bg_color = None
        self.game_state = None

import tkinter as tk
from tktooltip import ToolTip
from gui.theme import BG_COLOR


class SettingsPage:
    """
    Settings window for application preferences
    """

    def __init__(self, ctx):
        window = tk.Toplevel(ctx.root)
        window.title("Settings")
        window.geometry("800x600")
        window.configure(bg=BG_COLOR)

        sound_checkbox = tk.Checkbutton(window, text="Play sound on round finish")
        sound_checkbox.pack()
        flash_checkbox = tk.Checkbutton(window, text="Flash screen on round finish")
        flash_checkbox.pack()
        automatic_round_start_checkbox = tk.Checkbutton(
            window, text="Start next round automatically"
        )
        automatic_round_start_checkbox.pack()

        ToolTip(sound_checkbox, msg="test tip")

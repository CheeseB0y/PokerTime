import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from config.manager import save_settings


class SettingsPage:
    """
    Settings window for application preferences
    """

    def __init__(self, ctx):
        self.ctx = ctx
        window = tk.Toplevel(ctx.root)
        window.title("Settings")
        window.geometry("800x600")
        window.configure(bg=self.ctx.bg_color)

        self.play_alarm_sound_var = tk.BooleanVar(
            value=self.ctx.settings.play_alarm_sound
        )
        self.play_alarm_sound_checkbox = ttk.Checkbutton(
            window,
            text="Play sound on round finish",
            variable=self.play_alarm_sound_var,
        )
        self.play_alarm_sound_checkbox.pack()
        self.flash_screen_var = tk.BooleanVar(value=self.ctx.settings.flash_screen)
        self.flash_screen_checkbox = ttk.Checkbutton(
            window, text="Flash screen on round finish", variable=self.flash_screen_var
        )
        self.flash_screen_checkbox.pack()
        self.auto_start_next_round_var = tk.BooleanVar(
            value=self.ctx.settings.auto_start_next_round
        )
        self.auto_start_next_round_checkbox = ttk.Checkbutton(
            window,
            text="Start next round automatically",
            variable=self.auto_start_next_round_var,
        )
        self.auto_start_next_round_checkbox.pack()
        self.use_24_hour_clock_var = tk.BooleanVar(
            value=self.ctx.settings.use_24_hour_clock
        )
        self.use_24_hour_clock_checkbox = ttk.Checkbutton(
            window,
            text="24 hour clock",
            variable=self.use_24_hour_clock_var,
        )
        self.use_24_hour_clock_checkbox.pack()

        ToolTip(self.play_alarm_sound_checkbox, msg="test tip")

        save_changes_button = tk.Button(
            window,
            text="Save Changes",
            command=self.save_changes,
        )
        save_changes_button.pack()

        apply_changes_button = tk.Button(
            window,
            text="Apply Changes",
            command=self.apply_changes,
        )
        apply_changes_button.pack()

    def save_changes(self):
        self.update_settings()
        save_settings(settings=self.ctx.settings)

    def apply_changes(self):
        self.update_settings()

    def update_settings(self):
        self.ctx.settings.play_alarm_sound = self.play_alarm_sound_var.get()
        self.ctx.settings.flash_screen = self.flash_screen_var.get()
        self.ctx.settings.auto_start_next_round = self.auto_start_next_round_var.get()
        self.ctx.settings.use_24_hour_clock = self.use_24_hour_clock_var.get()

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
        self.window = tk.Toplevel(ctx.root)
        self.window.title("Settings")
        self.window.geometry("800x600")
        self.window.configure(bg=self.ctx.bg_color)

        self.play_alarm_sound_var = tk.BooleanVar(
            value=self.ctx.settings.play_alarm_sound
        )
        self.alarm_volume_var = tk.DoubleVar(value=self.ctx.settings.alarm_volume)
        self.flash_screen_var = tk.BooleanVar(value=self.ctx.settings.flash_screen)
        self.flash_duration_var = tk.IntVar(value=self.ctx.settings.flash_duration)
        self.auto_start_next_round_var = tk.BooleanVar(
            value=self.ctx.settings.auto_start_next_round
        )
        self.use_24_hour_clock_var = tk.BooleanVar(
            value=self.ctx.settings.use_24_hour_clock
        )

        self.play_alarm_sound_checkbox = ttk.Checkbutton(
            self.window,
            text="Play sound on round finish",
            variable=self.play_alarm_sound_var,
        )
        self.play_alarm_sound_checkbox.pack()

        self.alarm_volume_slider = ttk.Scale(
            self.window,
            from_=0.0,
            to=1.0,
            orient="horizontal",
            variable=self.alarm_volume_var,
        )
        self.alarm_volume_slider.pack()

        self.flash_screen_checkbox = ttk.Checkbutton(
            self.window,
            text="Flash screen on round finish",
            variable=self.flash_screen_var,
        )
        self.flash_screen_checkbox.pack()

        self.flash_duration_spinbox = tk.Spinbox(
            self.window, from_=1, to=20, textvariable=self.flash_duration_var, width=5
        )
        self.flash_duration_spinbox.pack()

        self.auto_start_next_round_checkbox = ttk.Checkbutton(
            self.window,
            text="Start next round automatically",
            variable=self.auto_start_next_round_var,
        )
        self.auto_start_next_round_checkbox.pack()

        self.use_24_hour_clock_checkbox = ttk.Checkbutton(
            self.window,
            text="24 hour clock",
            variable=self.use_24_hour_clock_var,
        )
        self.use_24_hour_clock_checkbox.pack()

        save_changes_button = tk.Button(
            self.window,
            text="Save Changes",
            command=self.save_changes,
        )
        save_changes_button.pack()

        apply_changes_button = tk.Button(
            self.window,
            text="Apply Changes",
            command=self.apply_changes,
        )
        apply_changes_button.pack()

        ToolTip(self.play_alarm_sound_checkbox, msg="test tip")

    def save_changes(self):
        self.update_settings()
        save_settings(settings=self.ctx.settings)

    def apply_changes(self):
        self.update_settings()

    def update_settings(self):
        self.ctx.settings.play_alarm_sound = self.play_alarm_sound_var.get()
        self.ctx.settings.alarm_volume = self.alarm_volume_var.get()
        self.ctx.settings.flash_screen = self.flash_screen_var.get()
        self.ctx.settings.flash_duration = self.flash_duration_var.get()
        self.ctx.settings.auto_start_next_round = self.auto_start_next_round_var.get()
        if self.ctx.settings.use_24_hour_clock is not self.use_24_hour_clock_var.get():
            self.ctx.settings.use_24_hour_clock = self.use_24_hour_clock_var.get()
            self.ctx.clock.redraw()

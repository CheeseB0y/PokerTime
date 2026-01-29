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
        self.window.resizable(False, False)
        self.window.configure(bg=self.ctx.bg_color)

        self.window.columnconfigure((0, 1), weight=1, uniform="columns")
        self.window.rowconfigure((0, 1, 2), weight=1)

        self.title_frame = tk.Frame(self.window, bg="black")
        self.title_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        self.left_frame = tk.Frame(self.window, bg=self.ctx.bg_color)
        self.left_frame.grid(row=1, column=0, sticky="NESW")
        self.right_frame = tk.Frame(self.window, bg=self.ctx.bg_color)
        self.right_frame.grid(row=1, column=1, sticky="NESW")
        self.button_frame = tk.Frame(self.window, bg=self.ctx.bg_color)
        self.button_frame.grid(row=2, column=0, columnspan=2, sticky="NESW")

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
        self.ui_scale_var = tk.DoubleVar(value=self.ctx.settings.scale)

        self.title_label = tk.Label(
            self.title_frame,
            text="Settings",
            bg="black",
            fg="white",
            font=("Arial", 32, "bold"),
        )
        self.title_label.pack(fill="both", expand=True, padx=10, pady=10)

        self.play_alarm_sound_checkbox = ttk.Checkbutton(
            self.left_frame,
            text="Play sound on round finish",
            variable=self.play_alarm_sound_var,
            command=self.volume_toggle,
        )
        self.play_alarm_sound_checkbox.pack(fill="both", padx=10, pady=10)
        self.flash_screen_checkbox = ttk.Checkbutton(
            self.left_frame,
            text="Flash screen on round finish",
            variable=self.flash_screen_var,
            command=self.flash_duration_toggle,
        )
        self.flash_screen_checkbox.pack(fill="both", padx=10, pady=10)
        self.auto_start_next_round_checkbox = ttk.Checkbutton(
            self.left_frame,
            text="Start next round automatically",
            variable=self.auto_start_next_round_var,
        )
        self.auto_start_next_round_checkbox.pack(fill="both", padx=10, pady=10)
        self.use_24_hour_clock_checkbox = ttk.Checkbutton(
            self.left_frame,
            text="24 hour clock",
            variable=self.use_24_hour_clock_var,
        )
        self.use_24_hour_clock_checkbox.pack(fill="both", padx=10, pady=10)

        self.flash_duration_label = tk.Label(self.right_frame, text="Flash Duration")
        self.flash_duration_label.pack(fill="both", padx=10, pady=10)
        self.flash_duration_spinbox = ttk.Spinbox(
            self.right_frame,
            from_=1,
            to=20,
            textvariable=self.flash_duration_var,
            width=5,
        )
        self.flash_duration_spinbox.pack(fill="both", padx=10, pady=10)
        self.alarm_volume_label = tk.Label(self.right_frame, text="Alarm Volume")
        self.alarm_volume_label.pack(fill="both", padx=10, pady=10)
        self.alarm_volume_slider = ttk.Scale(
            self.right_frame,
            from_=0.0,
            to=1.0,
            orient="horizontal",
            variable=self.alarm_volume_var,
        )
        self.alarm_volume_slider.pack(fill="both", padx=10, pady=10)
        self.alarm_volume_test_button = tk.Button(
            self.right_frame,
            text="Test Alarm",
            command=lambda: self.ctx.sound.play_alarm_sound(
                self.alarm_volume_var.get()
            ),
        )
        self.alarm_volume_test_button.pack(fill="both", padx=10, pady=10)
        self.ui_scale_label = tk.Label(self.right_frame, text="UI Scale")
        self.ui_scale_label.pack(fill="both", padx=10, pady=10)
        self.ui_scale_spinbox = ttk.Spinbox(
            self.right_frame,
            from_=1,
            to=2,
            increment=0.1,
            format="%.1f",
            textvariable=self.ui_scale_var,
            width=5,
        )
        self.ui_scale_spinbox.pack(fill="both", padx=10, pady=10)

        save_changes_button = tk.Button(
            self.button_frame,
            text="Save Changes",
            bg="red",
            fg="white",
            font=self.ctx.font["button"],
            relief="raised",
            command=self.save_changes,
        )
        save_changes_button.pack(
            fill="both",
            expand=True,
            padx=self.ctx.spacing["md"],
            pady=self.ctx.spacing["md"],
            side="left",
        )
        apply_changes_button = tk.Button(
            self.button_frame,
            text="Apply Changes",
            bg="black",
            fg="white",
            font=self.ctx.font["button"],
            relief="raised",
            command=self.apply_changes,
        )
        apply_changes_button.pack(
            fill="both",
            expand=True,
            padx=self.ctx.spacing["md"],
            pady=self.ctx.spacing["md"],
            side="left",
        )

        self.flash_duration_toggle()
        self.volume_toggle()

        ToolTip(self.play_alarm_sound_checkbox, msg="test tip")

    def flash_duration_toggle(self):
        if self.flash_screen_var.get():
            self.flash_duration_spinbox.config(state="normal")
        else:
            self.flash_duration_spinbox.config(state="disabled")

    def volume_toggle(self):
        if self.play_alarm_sound_var.get():
            self.alarm_volume_slider.config(state="normal")
        else:
            self.alarm_volume_slider.config(state="disabled")

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
        self.ctx.settings.scale = self.ui_scale_var.get()
        if self.ctx.settings.use_24_hour_clock is not self.use_24_hour_clock_var.get():
            self.ctx.settings.use_24_hour_clock = self.use_24_hour_clock_var.get()
            self.ctx.clock.redraw()

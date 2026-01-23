import math
import tkinter as tk
from pygame import mixer
from utils.absolute_path import absolute_path


class Timer:
    """
    Timer object

    Handles start/stop formatting and other logic
    """

    def __init__(self, container, ctx):
        self.ctx = ctx
        self.is_paused = True
        self.time_remaining = self.ctx.game_state.time * 60
        self.time_var = tk.StringVar(value=self.format_time(self.time_remaining))
        self.alarm_sound = mixer.Sound(absolute_path("assets/alarm.wav"))
        self.timer_label = tk.Label(
            container,
            textvariable=self.time_var,
            bg=self.ctx.bg_color,
            fg="white",
            font=("Arial", 120, "bold"),
        )
        self.timer_label.pack(fill="both", expand=True)

    def start(self):
        """
        Start timer

        if timer is started pause timer
        if timer is zero reset timer

        Args:
            None

        Returns:
            None
        """
        if self.is_paused:
            self.unpause()
            self.ctx.current_page.timer_button.set_text("Pause Timer")
            self.countdown()
        elif self.time_remaining == 0:
            self.pause()
            self.ctx.current_page.stop_flashing()
            self.time_remaining = self.ctx.game_state.time * 60
            self.time_var.set(self.format_time(self.time_remaining))
            self.ctx.current_page.timer_button.set_text("Start Timer")
        else:
            self.pause()
            self.ctx.current_page.timer_button.set_text("Resume Timer")

    def pause(self):
        """Pause timer"""
        self.is_paused = True

    def unpause(self):
        """Unpause timer"""
        self.is_paused = False

    def countdown(self):
        """
        Timer countdown

        Args:
            None

        Returns:
            None
        """
        if self.time_remaining > 0 and not self.is_paused:
            self.time_var.set(self.format_time(self.time_remaining))
            self.time_remaining -= 1
            self.ctx.root.after(1000, self.countdown)
        elif self.is_paused:
            pass
        else:
            self.time_var.set("0:00")
            self.play_alarm_sound()
            self.ctx.current_page.flash_screen()
            if self.ctx.settings.auto_start_next_round:
                self.ctx.next_round()
                self.start()
            else:
                self.ctx.current_page.timer_button.set_text("Reset Timer")

    def play_alarm_sound(self):
        if self.ctx.settings.play_alarm_sound:
            self.alarm_sound.set_volume(self.ctx.settings.alarm_volume)
            self.alarm_sound.play()

    def format_time(self, time):
        """
        Format time for reable display

        Args:
            time (int): Time in seconds

        Returns:
            time (str): Time in a readable clock format mm:ss
        """
        mins = time / 60
        secs = time % 60
        if secs < 10:
            secs = "0" + str(secs)
        return f"{math.floor(mins)}:{secs}"


class TimerButton:
    """
    Timer start/pause/reset button

    abstracted so that the button text can be easily modified
    """

    def __init__(self, container, ctx):
        self.timer_button_text = tk.StringVar(value="Start Timer")
        timer_button = tk.Button(
            container,
            textvariable=self.timer_button_text,
            command=ctx.current_page.timer.start,
            bg="red",
            fg="white",
            font=("Arial", 30, "bold"),
            relief="raised",
        )
        timer_button.pack(fill="both", expand=True, pady=50, padx=10)

    def set_text(self, text):
        """
        Set button label text

        Args:
            text (str): Text to be set as button label

        Returns:
            None
        """
        self.timer_button_text.set(value=text)

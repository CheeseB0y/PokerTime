import math
import tkinter as tk
from pygame import mixer
from models.game_state import GameState
from gui.editor_page import EditorPage
from gui.game_overview_page import GameOverview
from gui.settings_page import SettingsPage
from gui.menu_bar import MenuBar
from gui.theme import BG_COLOR
from utils.absolute_path import absolute_path


class GamePage:
    """
    Main game page
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.ctx.refresh_round_values = self.refresh_round_values

        if self.ctx.rounds is not None:
            self.ctx.current_page.destroy()
            self.ctx.is_landing_page = False
            self.ctx.current_page = self

        if not self.ctx.is_landing_page:
            self.ctx.game_state = GameState(self.ctx.rounds)

            self.round_num = tk.StringVar(
                value=f"Round: {self.ctx.game_state.round_num}"
            )
            self.s_blind = tk.StringVar(
                value=f"Small Blind: {self.ctx.game_state.s_blind:,}"
            )
            self.b_blind = tk.StringVar(
                value=f"Big Blind: {self.ctx.game_state.b_blind:,}"
            )

            def start_game():
                GamePage(self.ctx)

            def new_game():
                EditorPage(self.ctx, start_game, new=True)

            def edit_game():
                EditorPage(self.ctx, start_game)

            def overview():
                GameOverview(self.ctx)

            def settings():
                SettingsPage(self.ctx)

            MenuBar(
                self.ctx.root,
                new_game_callback=new_game,
                edit_game_callback=edit_game,
                overview_callback=overview,
                settings_callback=settings,
                restart_callback=self.restart_game,
            )
            self.ctx.root.columnconfigure((0, 1, 2), weight=1)
            self.ctx.root.rowconfigure((0, 1, 2, 3), weight=1)

            self.round_frame = tk.Frame(self.ctx.root, bg=BG_COLOR)
            self.round_frame.grid(row=0, column=0, columnspan=3, sticky="NESW")
            self.button_frame = tk.Frame(self.ctx.root, bg=BG_COLOR)
            self.button_frame.grid(row=1, column=2, rowspan=2, sticky="NESW")
            self.time_frame = tk.Frame(self.ctx.root, bg=BG_COLOR)
            self.time_frame.grid(
                row=1, column=0, rowspan=2, columnspan=2, sticky="NESW"
            )
            self.blind_frame = tk.Frame(self.ctx.root, bg=BG_COLOR)
            self.blind_frame.grid(row=3, column=0, columnspan=2, sticky="NESW")

            self.round_number_label = tk.Label(
                self.round_frame,
                textvariable=self.round_num,
                bg="black",
                fg="white",
                font=("Arial", 60, "bold"),
            )
            self.round_number_label.pack(fill="both", expand=True)
            self.timer = Timer(self.time_frame, self.ctx)
            self.timer_button = TimerButton(self.button_frame, ctx)
            next_button = tk.Button(
                self.button_frame,
                text="Next Round",
                command=self.next_round,
                bg="black",
                fg="white",
                font=("Arial", 30, "bold"),
                relief="raised",
            )
            next_button.pack(fill="both", expand=True, pady=50, padx=10)
            reset_button = tk.Button(
                self.button_frame,
                text="Reset Timer",
                command=self.restart_timer,
                bg="red",
                fg="white",
                font=("Arial", 30, "bold"),
                relief="raised",
            )
            reset_button.pack(fill="both", expand=True, pady=50, padx=10)
            s_blind_label = tk.Label(
                self.blind_frame,
                textvariable=self.s_blind,
                bg="black",
                fg="white",
                relief="raised",
                font=("Arial", 30, "bold"),
            )
            s_blind_label.pack(side="left", fill="both", expand=True, pady=10, padx=50)
            b_blind_label = tk.Label(
                self.blind_frame,
                textvariable=self.b_blind,
                bg="red",
                fg="white",
                relief="raised",
                font=("Arial", 30, "bold"),
            )
            b_blind_label.pack(side="right", fill="both", expand=True, pady=10, padx=50)

            self.ctx.next_round = self.next_round
            self.is_flashing = False

    def flash_screen(self):
        """
        Flashes screen on timer completion

        Args:
            None

        Returns:
            None
        """
        if self.ctx.settings.flash_screen:
            self.is_flashing = True
            self.flash_1(self.ctx.settings.flash_duration)

    def stop_flashing(self):
        """
        Stops screen flashing

        Args:
            None

        Returns:
            None
        """
        self.is_flashing = False

    def flash_1(self, duration):
        """
        First part of flash sequence
        should not be called directly

        Args:
            duration (int): number of screen flash cycles

        Returns:
            None
        """
        if duration > 0 and self.is_flashing:
            self.ctx.root.configure(bg="black")
            self.round_frame.configure(bg="black")
            self.round_number_label.configure(bg="black")
            self.button_frame.configure(bg="black")
            self.time_frame.configure(bg="black")
            self.timer.timer_label.configure(bg="black")
            self.blind_frame.configure(bg="black")
            self.ctx.root.after(500, lambda: self.flash_2(duration))
        else:
            self.ctx.root.configure(bg=BG_COLOR)
            self.round_frame.configure(bg=BG_COLOR)
            self.round_number_label.configure(bg="black")
            self.button_frame.configure(bg=BG_COLOR)
            self.time_frame.configure(bg=BG_COLOR)
            self.timer.timer_label.configure(bg=BG_COLOR)
            self.blind_frame.configure(bg=BG_COLOR)

    def flash_2(self, duration):
        """
        Second part of flash sequence
        should not be called directly

        Args:
            duration (int): number of screen flash cycles

        Returns:
            None
        """
        if self.is_flashing:
            self.ctx.root.configure(bg="white")
            self.round_frame.configure(bg="white")
            self.round_number_label.configure(bg="white")
            self.button_frame.configure(bg="white")
            self.time_frame.configure(bg="white")
            self.timer.timer_label.configure(bg="white")
            self.blind_frame.configure(bg="white")
            self.ctx.root.after(500, lambda: self.flash_1(duration - 1))
        else:
            self.ctx.root.configure(bg=BG_COLOR)
            self.round_frame.configure(bg=BG_COLOR)
            self.round_number_label.configure(bg="black")
            self.button_frame.configure(bg=BG_COLOR)
            self.time_frame.configure(bg=BG_COLOR)
            self.timer.timer_label.configure(bg=BG_COLOR)
            self.blind_frame.configure(bg=BG_COLOR)

    def refresh_round_values(self):
        """
        Refresh values on screen

        Args:
            None

        Returns:
            None
        """
        self.timer.time_remaining = self.ctx.game_state.time * 60
        self.timer.time_var.set(value=self.timer.format_time(self.timer.time_remaining))
        self.timer_button.set_text("Start Timer")
        self.round_num.set(f"Round: {self.ctx.game_state.round_num}")
        self.s_blind.set(f"Small Blind: {self.ctx.game_state.s_blind:,}")
        self.b_blind.set(f"Big Blind: {self.ctx.game_state.b_blind:,}")

    def next_round(self):
        """
        Starts next round

        Args:
            None

        Returns:
            None
        """
        if not self.ctx.settings.auto_start_next_round:
            self.stop_flashing()
        self.timer.pause()
        self.ctx.game_state.next_round()
        self.refresh_round_values()

    def restart_game(self):
        """
        Restarts game from round 1

        Args:
            None

        Returns:
            None
        """
        self.timer.pause()
        self.stop_flashing()
        self.ctx.game_state.restart_game()
        self.refresh_round_values()

    def restart_timer(self):
        """
        Restarts timer for current round

        Args:
            None

        Returns:
            None
        """
        self.timer.pause()
        self.stop_flashing()
        self.timer.time_remaining = self.ctx.game_state.time * 60
        self.timer.time_var.set(self.timer.format_time(self.timer.time_remaining))
        self.timer.ctx.current_page.timer_button.set_text("Start Timer")


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
            bg=BG_COLOR,
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

import tkinter as tk
from gui.editor_page import EditorPage
from gui.game_overview_page import GameOverview
from gui.settings_page import SettingsPage
from gui.menu_bar import MenuBar
from gui.timer import Timer, TimerButton
from gui.clock import Clock


class GamePage:
    """
    Main game page
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.ctx.refresh_round_values = self.refresh_round_values

        if self.ctx.game_state.rounds is not None:
            self.ctx.current_page.destroy()
            self.ctx.current_page = self

        self.round_num = tk.StringVar(value=f"Round: {self.ctx.game_state.round_num}")
        self.s_blind = tk.StringVar(
            value=f"Small Blind: {self.ctx.game_state.s_blind:,}"
        )
        self.b_blind = tk.StringVar(value=f"Big Blind: {self.ctx.game_state.b_blind:,}")

        def start_game(ctx):
            GamePage(ctx)

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

        self.round_frame = tk.Frame(self.ctx.root, bg=self.ctx.bg_color)
        self.round_frame.grid(row=0, column=0, columnspan=2, sticky="NESW")
        self.clock_frame = tk.Frame(self.ctx.root, bg=self.ctx.bg_color)
        self.clock_frame.grid(row=0, column=2, sticky="NESW")
        self.button_frame = tk.Frame(self.ctx.root, bg=self.ctx.bg_color)
        self.button_frame.grid(row=1, column=2, rowspan=2, sticky="NESW")
        self.time_frame = tk.Frame(self.ctx.root, bg=self.ctx.bg_color)
        self.time_frame.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="NESW")
        self.blind_frame = tk.Frame(self.ctx.root, bg=self.ctx.bg_color)
        self.blind_frame.grid(row=3, column=0, columnspan=2, sticky="NESW")

        self.round_number_label = tk.Label(
            self.round_frame,
            textvariable=self.round_num,
            bg="black",
            fg="white",
            font=("Arial", 60, "bold"),
        )
        self.clock = Clock(self.clock_frame, ctx)
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
            self.ctx.root.configure(bg=self.ctx.bg_color)
            self.round_frame.configure(bg=self.ctx.bg_color)
            self.round_number_label.configure(bg="black")
            self.button_frame.configure(bg=self.ctx.bg_color)
            self.time_frame.configure(bg=self.ctx.bg_color)
            self.timer.timer_label.configure(bg=self.ctx.bg_color)
            self.blind_frame.configure(bg=self.ctx.bg_color)

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
            self.ctx.root.configure(bg=self.ctx.bg_color)
            self.round_frame.configure(bg=self.ctx.bg_color)
            self.round_number_label.configure(bg="black")
            self.button_frame.configure(bg=self.ctx.bg_color)
            self.time_frame.configure(bg=self.ctx.bg_color)
            self.timer.timer_label.configure(bg=self.ctx.bg_color)
            self.blind_frame.configure(bg=self.ctx.bg_color)

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

    def destroy(self):
        for widget in self.ctx.root.winfo_children():
            widget.destroy()

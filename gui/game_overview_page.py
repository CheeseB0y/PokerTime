import tkinter as tk


class GameOverview:
    """
    Basic overview page to see all round data
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.window = tk.Toplevel(self.ctx.root)
        self.window.title("Game Overview")
        self.window.geometry("800x600")
        self.window.configure(bg=self.ctx.bg_color)

        self.window.columnconfigure((0, 1, 2, 3), weight=1)
        for i in range(len(self.ctx.game_state.rounds)):
            self.window.rowconfigure(i, weight=1)

        round_column = tk.Frame(self.window, bg="red")
        round_column.grid(
            row=0, column=0, rowspan=len(self.ctx.game_state.rounds), sticky="NESW"
        )
        time_column = tk.Frame(self.window, bg="black")
        time_column.grid(
            row=0, column=1, rowspan=len(self.ctx.game_state.rounds), sticky="NESW"
        )
        s_blind_column = tk.Frame(self.window, bg="red")
        s_blind_column.grid(
            row=0, column=2, rowspan=len(self.ctx.game_state.rounds), sticky="NESW"
        )
        b_blind_column = tk.Frame(self.window, bg="black")
        b_blind_column.grid(
            row=0, column=3, rowspan=len(self.ctx.game_state.rounds), sticky="NESW"
        )

        tk.Label(round_column, text="Round", bg="red", fg="white").grid(
            row=0, column=0, padx=10, pady=10, sticky="NESW"
        )
        tk.Label(time_column, text="Time", bg="black", fg="white").grid(
            row=0, column=1, padx=10, pady=10, sticky="NESW"
        )
        tk.Label(s_blind_column, text="Small Blind", bg="red", fg="white").grid(
            row=0, column=2, padx=10, pady=10, sticky="NESW"
        )
        tk.Label(b_blind_column, text="Big Blind", bg="black", fg="white").grid(
            row=0, column=3, padx=10, pady=10, sticky="NESW"
        )

        for index, r in enumerate(self.ctx.game_state.rounds):
            tk.Label(round_column, text=r.num, bg="red", fg="white").grid(
                row=index + 1, column=0, padx=10, pady=10, sticky="NESW"
            )
            tk.Label(time_column, text=r.time, bg="black", fg="white").grid(
                row=index + 1, column=1, padx=10, pady=10, sticky="NESW"
            )
            tk.Label(s_blind_column, text=r.s_blind, bg="red", fg="white").grid(
                row=index + 1, column=2, padx=10, pady=10, sticky="NESW"
            )
            tk.Label(b_blind_column, text=r.b_blind, bg="black", fg="white").grid(
                row=index + 1, column=3, padx=10, pady=10, sticky="NESW"
            )

import tkinter as tk
from gui.theme import BG_COLOR


class GameOverview:
    """
    Basic overview page to see all round data
    """

    def __init__(self, ctx):
        window = tk.Toplevel(ctx.root)
        window.title("Game Overview")
        window.geometry("800x600")
        window.configure(bg=BG_COLOR)

        window.columnconfigure((0, 1, 2, 3), weight=1)
        for i in range(len(ctx.game_state.rounds)):
            window.rowconfigure(i, weight=1)

        round_column = tk.Frame(window, bg="red")
        round_column.grid(
            row=0, column=0, rowspan=len(ctx.game_state.rounds), sticky="NESW"
        )
        time_column = tk.Frame(window, bg="black")
        time_column.grid(
            row=0, column=1, rowspan=len(ctx.game_state.rounds), sticky="NESW"
        )
        s_blind_column = tk.Frame(window, bg="red")
        s_blind_column.grid(
            row=0, column=2, rowspan=len(ctx.game_state.rounds), sticky="NESW"
        )
        b_blind_column = tk.Frame(window, bg="black")
        b_blind_column.grid(
            row=0, column=3, rowspan=len(ctx.game_state.rounds), sticky="NESW"
        )

        tk.Label(round_column, text="Round", bg="red", fg="white").grid(
            row=0, column=0, padx=10, pady=10, sticky="NSWE"
        )
        tk.Label(time_column, text="Time", bg="black", fg="white").grid(
            row=0, column=1, padx=10, pady=10, sticky="NSWE"
        )
        tk.Label(s_blind_column, text="Small Blind", bg="red", fg="white").grid(
            row=0, column=2, padx=10, pady=10, sticky="NSWE"
        )
        tk.Label(b_blind_column, text="Big Blind", bg="black", fg="white").grid(
            row=0, column=3, padx=10, pady=10, sticky="NSWE"
        )

        for index, r in enumerate(ctx.game_state.rounds):
            tk.Label(round_column, text=r.num, bg="red", fg="white").grid(
                row=index + 1, column=0, padx=10, pady=10, sticky="NSWE"
            )
            tk.Label(time_column, text=r.time, bg="black", fg="white").grid(
                row=index + 1, column=1, padx=10, pady=10, sticky="NSWE"
            )
            tk.Label(s_blind_column, text=r.s_blind, bg="red", fg="white").grid(
                row=index + 1, column=2, padx=10, pady=10, sticky="NSWE"
            )
            tk.Label(b_blind_column, text=r.b_blind, bg="black", fg="white").grid(
                row=index + 1, column=3, padx=10, pady=10, sticky="NSWE"
            )

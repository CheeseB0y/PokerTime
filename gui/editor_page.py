import csv
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from models.round import Round


class EditorPage:
    """
    Game editor window

    create a new game or edit an existing one
    import or export game files as csv
    """

    def __init__(self, ctx, game_page_callback, new=False):
        self.window = tk.Toplevel(ctx.root)
        self.ctx = ctx
        self.game_page_callback = game_page_callback
        if new:
            self.window.title("New Game")
            self.rounds = []
        else:
            self.window.title("Edit Game")
            self.rounds = self.ctx.game_state.rounds

        self.window.geometry("800x600")
        self.window.configure(bg=self.ctx.bg_color)
        self.window.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        round_column_heading = tk.Frame(self.window, bg="red")
        round_column_heading.grid(row=0, column=1, sticky="NESW")
        self.round_column = tk.Frame(self.window, bg="red")
        self.round_column.grid(row=1, column=1, sticky="NESW")

        time_column_heading = tk.Frame(self.window, bg="black")
        time_column_heading.grid(row=0, column=2, sticky="NESW")
        self.time_column = tk.Frame(self.window, bg="black")
        self.time_column.grid(row=1, column=2, sticky="NESW")

        s_blind_column_heading = tk.Frame(self.window, bg="red")
        s_blind_column_heading.grid(row=0, column=3, sticky="NESW")
        self.s_blind_column = tk.Frame(self.window, bg="red")
        self.s_blind_column.grid(row=1, column=3, sticky="NESW")

        b_blind_column_heading = tk.Frame(self.window, bg="black")
        b_blind_column_heading.grid(row=0, column=4, sticky="NESW")
        self.b_blind_column = tk.Frame(self.window, bg="black")
        self.b_blind_column.grid(row=1, column=4, sticky="NESW")

        round_column_label = tk.Label(
            round_column_heading, text="Rounds:", bg="red", fg="white"
        )
        round_column_label.pack(fill="both", expand=True, side="left")
        self.num_rounds_entry = tk.Entry(
            round_column_heading, width=2, bg="red", fg="white"
        )
        self.num_rounds_entry.pack(fill="both", expand=True, side="right")
        self.num_rounds_entry.insert(tk.END, len(self.rounds))
        time_column_label = tk.Label(
            time_column_heading, text="Time", bg="black", fg="white"
        )
        time_column_label.pack(fill="both", expand=True)
        s_blind_column_label = tk.Label(
            s_blind_column_heading, text="Small Blind", bg="red", fg="white"
        )
        s_blind_column_label.pack(fill="both", expand=True)
        b_blind_column_label = tk.Label(
            b_blind_column_heading, text="Big Blind", bg="black", fg="white"
        )
        b_blind_column_label.pack(fill="both", expand=True)

        self.time_list = []
        self.s_blind_list = []
        self.b_blind_list = []

        for index, r in enumerate(self.rounds):
            tk.Label(self.round_column, text=r.num, bg="red", fg="white").pack(
                fill="both", expand=True
            )
            self.time_list.append(
                tk.Entry(self.time_column, width=6, bg="black", fg="white")
            )
            self.time_list[index].pack(fill="both", expand=True)
            self.time_list[index].insert(tk.END, r.time)
            self.s_blind_list.append(
                tk.Entry(self.s_blind_column, width=10, bg="red", fg="white")
            )
            self.s_blind_list[index].pack(fill="both", expand=True)
            self.s_blind_list[index].insert(tk.END, r.s_blind)
            self.b_blind_list.append(
                tk.Entry(self.b_blind_column, width=10, bg="black", fg="white")
            )
            self.b_blind_list[index].pack(fill="both", expand=True)
            self.b_blind_list[index].insert(tk.END, r.b_blind)

        button_frame = tk.Frame(self.window, bg=self.ctx.bg_color)
        button_frame.grid(row=2, column=1, columnspan=4, sticky="NESW")
        tk.Button(
            button_frame,
            text="Save Game",
            command=self.save_game,
            bg="black",
            fg="white",
        ).pack(side="left", fill="both", expand=True)
        tk.Button(
            button_frame,
            text="Export Game",
            command=self.export_game,
            bg="red",
            fg="white",
        ).pack(side="left", fill="both", expand=True)
        tk.Button(
            button_frame,
            text="Import Game",
            command=self.import_game,
            bg="black",
            fg="white",
        ).pack(side="left", fill="both", expand=True)
        tk.Button(
            button_frame,
            text="Start Game",
            command=self.start_game,
            bg="red",
            fg="white",
        ).pack(side="left", fill="both", expand=True)

    def refresh_editor(self):
        """
        Refresh editor screen when changes are made

        Args:
            None

        Returns:
            None
        """
        for widget in self.round_column.winfo_children():
            widget.destroy()
        self.time_list.clear()
        for widget in self.time_column.winfo_children():
            widget.destroy()
        self.s_blind_list.clear()
        for widget in self.s_blind_column.winfo_children():
            widget.destroy()
        self.b_blind_list.clear()
        for widget in self.b_blind_column.winfo_children():
            widget.destroy()
        self.num_rounds_entry.delete(0, tk.END)
        self.num_rounds_entry.insert(tk.END, len(self.rounds))
        for index, r in enumerate(self.rounds):
            tk.Label(self.round_column, text=r.num, bg="red", fg="white").pack(
                fill="both", expand=True
            )
            self.time_list.append(
                tk.Entry(self.time_column, width=6, bg="black", fg="white")
            )
            self.time_list[index].pack(fill="both", expand=True)
            self.time_list[index].insert(tk.END, r.time)
            self.s_blind_list.append(
                tk.Entry(self.s_blind_column, width=10, bg="red", fg="white")
            )
            self.s_blind_list[index].pack(fill="both", expand=True)
            self.s_blind_list[index].insert(tk.END, r.s_blind)
            self.b_blind_list.append(
                tk.Entry(self.b_blind_column, width=10, bg="black", fg="white")
            )
            self.b_blind_list[index].pack(fill="both", expand=True)
            self.b_blind_list[index].insert(tk.END, r.b_blind)

    def start_game(self):
        self.ctx.game_state.update_rounds(self.rounds)
        self.game_page_callback(self.ctx)

    def save_game(self):
        """
        Save editor values

        Args:
            None

        Returns:
            None
        """
        try:
            num_rounds = int(self.num_rounds_entry.get())
        except ValueError:
            self.num_rounds_entry.delete(0, tk.END)
            self.num_rounds_entry.insert(tk.END, len(self.rounds))
            num_rounds = len(self.rounds)
        rounds = []
        for i in range(num_rounds):
            try:
                rounds.append(
                    Round(
                        i + 1,
                        int(self.time_list[i].get()),
                        int(self.s_blind_list[i].get()),
                        int(self.b_blind_list[i].get()),
                    )
                )
            except IndexError:
                rounds.append(Round(i + 1))
            except ValueError:
                rounds.append(Round(i + 1))
        self.rounds = rounds
        self.refresh_editor()

    def export_game(self):
        """
        Export game as CSV

        Args:
            None

        Returns:
            None
        """
        documents_dir = Path.home() / "Documents"
        if not documents_dir.exists():
            documents_dir = Path.home()
        poker_dir = documents_dir / "PokerTime"
        poker_dir.mkdir(parents=True, exist_ok=True)

        self.save_game()

        file = filedialog.asksaveasfilename(
            defaultextension=".csv",
            initialdir=poker_dir,
            title="Choose where to save the game file.",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
        )

        source = self.rounds

        if file:
            with open(file, "w", newline="", encoding="utf-8") as f:
                for r in source:
                    f.write(f"{r.num},{r.time},{r.s_blind},{r.b_blind}\n")

    def import_game(self):
        """
        Import a game from a CSV file

        Args:
            None

        Returns:
            None
        """
        documents_dir = Path.home() / "Documents"
        if not documents_dir.exists():
            documents_dir = Path.home()
        poker_dir = documents_dir / "PokerTime"
        poker_dir.mkdir(parents=True, exist_ok=True)

        file = filedialog.askopenfilename(
            initialdir=poker_dir,
            title="Select a file",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
        )

        rounds = []

        if file:
            with open(file, "r", encoding="utf-8") as f:
                for row in csv.reader(f):
                    rounds.append(
                        Round(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
                    )
        self.rounds = rounds
        self.refresh_editor()

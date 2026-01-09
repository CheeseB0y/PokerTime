import sys
import tkinter as tk


class MenuBar:
    """
    Menu bar class for options
    """

    def __init__(
        self,
        root,
        new_game_callback,
        edit_game_callback,
        overview_callback,
        settings_callback,
        restart_callback,
    ):
        menubar = tk.Menu(root, bg="black", fg="white", relief="raised")
        root.config(menu=menubar)

        option_menu = tk.Menu(menubar, tearoff=0, bg="black", fg="white")
        menubar.add_cascade(label="Options", menu=option_menu)
        option_menu.add_command(label="New Game", command=new_game_callback)
        option_menu.add_command(label="Edit Game", command=edit_game_callback)
        option_menu.add_command(label="Game Overview", command=overview_callback)
        option_menu.add_command(label="Settings", command=settings_callback)
        option_menu.add_command(label="Restart Game", command=restart_callback)
        option_menu.add_command(label="Exit", command=sys.exit)

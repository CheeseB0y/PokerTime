import tkinter as tk
from PIL import Image, ImageTk
from gui.editor_page import EditorPage
from gui.game_page import GamePage
from utils.absolute_path import absolute_path


class LandingPage:
    """
    Program start page

    Serves as a welcome page for the user
    From this page you are able to start a game
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.ctx.current_page = self
        self.ctx.current_page.landing_page = True

        self.ctx.root.columnconfigure((0, 1, 2), weight=1)
        self.ctx.root.rowconfigure((0, 1), weight=1)

        title_frame = tk.Frame(ctx.root, bg="black")
        title_frame.grid(row=0, column=0, columnspan=3, sticky="NESW")
        image_frame = tk.Frame(ctx.root, bg=self.ctx.bg_color)
        image_frame.grid(row=1, column=0, columnspan=2, rowspan=3, sticky="NESW")
        button_frame = tk.Frame(ctx.root, bg=self.ctx.bg_color)
        button_frame.grid(row=1, column=2, rowspan=3)

        title = tk.Label(
            title_frame,
            text="Welcome to Poker Time!",
            bg="black",
            fg="white",
            font=("Arial", 60, "bold"),
        )
        title.pack(fill="both", expand=True, padx=10, pady=10)

        image_path = absolute_path("assets/landing_page_img.jpg")
        image_file = Image.open(image_path).resize((800, 500))
        image = ImageTk.PhotoImage(image_file)
        stock_image = tk.Label(image_frame, image=image)
        stock_image.image = image
        stock_image.pack(expand=True)

        new_game_button = tk.Button(
            button_frame,
            text="New Game",
            command=lambda: EditorPage(
                ctx,
                new=True,
                game_page_callback=self.game_page_callback,
            ),
            bg="red",
            fg="white",
            relief="raised",
            font=("Arial", 30, "bold"),
        )
        new_game_button.pack(fill="both", expand=True, padx=10, pady=10)

    def game_page_callback(self, ctx):
        GamePage(ctx)

    def destroy(self):
        """
        Destroy the landing page once a game is started

        Args:
            None

        Returns:
            None
        """
        for widget in self.ctx.root.winfo_children():
            widget.destroy()

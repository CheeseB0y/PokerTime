"""
Poker Time is a simple timer application built for poker tournaments.
"""

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from pygame import mixer
from models.context import AppContext
from gui.landing_page import LandingPage
from gui.theme import BG_COLOR


def main():
    """
    Main Function

    Initalizes basic program functions and starts on the landing page
    """

    mixer.init()

    ctx = AppContext()
    ctx.root.title("Poker Time")
    ctx.root.geometry("1200x900")
    ctx.root.configure(bg=BG_COLOR)
    ctx.is_landing_page = True
    ctx.current_page = LandingPage(ctx)
    ctx.root.mainloop()


if __name__ == "__main__":
    main()

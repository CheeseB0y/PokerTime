"""
Poker Time is a simple timer application built for poker tournaments.
"""

from models.context import AppContext
from gui.landing_page import LandingPage
from gui.theme import BG_COLOR


def main():
    """
    Main Function

    Initalizes basic program functions and starts on the landing page
    """

    ctx = AppContext()
    ctx.root.title("Poker Time")
    ctx.root.geometry("1200x900")
    ctx.root.configure(bg=BG_COLOR)
    ctx.current_page = LandingPage(ctx)
    ctx.root.mainloop()


if __name__ == "__main__":
    main()

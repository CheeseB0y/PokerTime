import time
import tkinter as tk


class Clock:
    def __init__(
        self,
        container,
        ctx,
        bg="black",
        fg="white",
        font=("Arial", 54, "bold"),
    ):
        self.ctx = ctx
        self.clock_text = tk.StringVar(value=time.strftime("%I:%M %p"))
        clock_label = tk.Label(
            container, textvariable=self.clock_text, bg=bg, fg=fg, font=font
        )
        clock_label.pack(fill="both", expand=True)
        self.update_time()

    def update_time(self):
        self.clock_text.set(time.strftime("%I:%M %p"))
        next_minute = 60 - time.localtime().tm_sec
        self.ctx.root.after(next_minute * 1000, self.update_time)

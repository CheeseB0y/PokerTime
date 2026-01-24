import time
import tkinter as tk


class Clock:
    def __init__(
        self,
        ctx,
        container,
        bg="black",
        fg="white",
        font=("Arial", 54, "bold"),
    ):
        self.ctx = ctx
        self.clock_text = tk.StringVar()
        clock_label = tk.Label(
            container, textvariable=self.clock_text, bg=bg, fg=fg, font=font
        )
        clock_label.pack(fill="both", expand=True)
        self.update_time()

    def update_time(self):
        if self.ctx.settings.use_24_hour_clock:
            self.clock_text.set(time.strftime("%H:%M"))
        else:
            self.clock_text.set(time.strftime("%I:%M %p").lstrip("0"))
        next_minute = 60 - time.localtime().tm_sec
        self.ctx.root.after(next_minute * 1000, self.update_time)

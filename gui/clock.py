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
        self.container = container
        self.ctx.clock = self
        self.clock_text = tk.StringVar()
        self.clock_label = tk.Label(
            container, textvariable=self.clock_text, bg=bg, fg=fg, font=font
        )
        self.clock_label.pack(fill="both", expand=True)

        self.after_id = None
        self.update_time()

    def update_time(self):
        self.redraw()
        next_minute = 60 - time.localtime().tm_sec
        self.after_id = self.ctx.root.after(next_minute * 1000, self.update_time)

    def redraw(self):
        if self.ctx.settings.use_24_hour_clock:
            self.clock_text.set(time.strftime("%H:%M"))
        else:
            self.clock_text.set(time.strftime("%I:%M %p").lstrip("0"))

    def destroy(self):
        if self.after_id is not None:
            self.ctx.root.after_cancel(self.after_id)
            self.after_id = None

        for widget in self.container.winfo_children():
            widget.destroy()

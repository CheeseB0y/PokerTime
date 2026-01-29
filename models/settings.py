class Settings:
    def __init__(self, config: dict):
        self.scale = config["scale"]
        self.play_alarm_sound = config["play_alarm_sound"]
        self.alarm_volume = config["alarm_volume"]
        self.flash_screen = config["flash_screen"]
        self.flash_duration = config["flash_duration"]
        self.auto_start_next_round = config["auto_start_next_round"]
        self.use_24_hour_clock = config["use_24_hour_clock"]

    def to_dict(self) -> dict:
        return {
            "scale": self.scale,
            "play_alarm_sound": self.play_alarm_sound,
            "alarm_volume": self.alarm_volume,
            "flash_screen": self.flash_screen,
            "flash_duration": self.flash_duration,
            "auto_start_next_round": self.auto_start_next_round,
            "24_hour_clock": self.use_24_hour_clock,
        }

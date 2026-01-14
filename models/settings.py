class Settings:
    def __init__(self, config: dict):
        self.play_alarm_sound = config["play_alarm_sound"]
        self.alarm_volume = config["alarm_volume"]
        self.flash_screen = ["flash_screen"]
        self.auto_start_next_round = config["auto_start_next_round"]

    def to_dict(self) -> dict:
        return {
            "play_alarm_sound": self.play_alarm_sound,
            "alarm_volume": self.alarm_volume,
            "flash_screen": self.flash_screen,
            "auto_start_next_round": self.auto_start_next_round,
        }

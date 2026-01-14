import json
from platformdirs import user_config_dir
from pathlib import Path
from config.defaults import DEFAULT_SETTINGS
from models.settings import Settings


APP_NAME = "PokerTime"
APP_AUTHOR = "CheeseB0y"


def get_config_path() -> Path:
    base = Path(user_config_dir(APP_NAME, APP_AUTHOR))
    base.mkdir(parents=True, exist_ok=True)
    return base / "settings.json"


def load_settings() -> Settings:
    path = get_config_path()

    if not path.exists():
        return Settings(DEFAULT_SETTINGS.copy())

    with open(path, "r", encoding="utf-8") as file:
        config = json.load(file)

    merged = DEFAULT_SETTINGS.copy()
    merged.update(config)

    return Settings(merged)


def save_settings(settings: Settings):
    path = get_config_path()
    with open(path, "w", encoding="utf-8") as file:
        json.dump(settings.to_dict(), file, indent=2)

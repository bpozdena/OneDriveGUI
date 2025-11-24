import os
from configparser import ConfigParser
from typing import Any, Union


class GuiSettings:
    DEFAULTS = {
        "SETTINGS": {
            "start_minimized": "False",
            "frameless_window": "False",
            "combined_start_stop_button": "True",
            "show_debug": "True",
            "save_debug": "True",
            "log_rotation_interval": "24",
            "log_backup_count": "3",
            "log_file": "/tmp/onedrive-gui/onedrive-gui.log",
            "debug_level": "DEBUG",
            "client_bin_path": "onedrive",
            "QWebEngine_login": "False",
            "autostart_enabled": "False",
        }
    }

    def __init__(self, gui_settings_file: str):
        self.gui_settings_file = gui_settings_file
        self.gui_settings = ConfigParser()
        self.load_defaults()
        self.gui_settings.read(self.gui_settings_file)

    def save(self) -> None:
        print(f"[GUI][SETTINGS] Saving new GUI settings: {self.gui_settings._sections}")
        with open(self.gui_settings_file, "w") as file:
            self.gui_settings.write(file)

    def load_defaults(self) -> None:
        self.gui_settings.read_dict(self.DEFAULTS)

    def get(self, setting_name: str, fallback: Any = None) -> Any:
        return self.gui_settings["SETTINGS"].get(setting_name, fallback)

    def set(self, setting_name: str, value: Union[str, int]) -> None:
        self.gui_settings["SETTINGS"][setting_name] = str(value)

    def dump(self) -> ConfigParser:
        return self.gui_settings


GUI_SETTINGS_FILE = os.path.expanduser("~/.config/onedrive-gui/gui_settings")

gui_settings = GuiSettings(GUI_SETTINGS_FILE)

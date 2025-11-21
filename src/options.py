import copy
from utils.utils import get_installed_client_version, config_client_bin_path
from global_config import create_global_config

from settings.gui_settings import gui_settings

client_bin_path = gui_settings.get("frameless_window")


version = "1.3.0"
client_bin_path = config_client_bin_path()
client_version = get_installed_client_version(client_bin_path)
global_config = create_global_config()
temp_global_config = copy.deepcopy(global_config)

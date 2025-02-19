import logging
import os
import copy
import re

# from logger import logger
from configparser import ConfigParser


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROFILES_FILE = os.path.expanduser("~/.config/onedrive-gui/profiles")


def create_global_config():
    """
    Creates dict which is used as running global config.
    EXAMPLE:

    {
    "bob@live.com": {
        "config_file": "/home/bob/.config/onedrive/accounts/bob@live.com/config",
        "enable_debug": "True",
        "mode": "monitor",
        "auto_sync": False,
        "onedrive": {
            "sync_dir": '"~/OneDrive"',
            "skip_file": '"~*|.~*|*.tmp|*.txt|*.exe|.testfile"',
            "monitor_interval": '"15"',
            ...},
    "john@live.com": {
        "config_file": "/home/bob/.config/onedrive/accounts/john@live.com/config",
        "enable_debug": "True",
        "mode": "monitor",
        "auto_sync": False,
        "onedrive": {
            "sync_dir": '"~/OneDrive2"',
            "skip_file": '"~*|.~*|*.tmp|*.txt|*.exe"',
            "monitor_interval": '"15"', ...}
    """

    # Load all default values. Needed for cases when imported config does not contain all properties.
    _default_od_config = read_config(DIR_PATH + "/resources/default_config")
    _default_profile_config = {"auto_sync": False, "account_type": "", "free_space": ""}
    default_od_config = _default_od_config._sections
    logging.debug(f"[GUI] - loading default config {default_od_config}")

    # Load existing user profiles.
    _profiles = ConfigParser()
    _profiles.read(PROFILES_FILE)
    profiles = _profiles._sections

    for profile in profiles:
        profile_config_file = profiles[profile]["config_file"]
        _od_config = read_config(profile_config_file)
        od_config = _od_config._sections

        # TODO: Re-write to better support future options.
        if "auto_sync" not in profiles[profile]:  # add 'auto_sync' value if missing from older versions
            profiles[profile]["auto_sync"] = _default_profile_config["auto_sync"]

        if "account_type" not in profiles[profile]:  # add 'account_type' value if missing from older versions
            profiles[profile]["account_type"] = _default_profile_config["account_type"]

        if "free_space" not in profiles[profile]:  # add 'free_space' value if missing from older versions
            profiles[profile]["free_space"] = _default_profile_config["free_space"]

        # Load default Onedrive values
        profiles[profile]["onedrive"] = {}
        profiles[profile]["onedrive"].update(default_od_config["onedrive"])

        # Load user values from config

        profiles[profile]["onedrive"].update(od_config["onedrive"])

    logging.debug(f"[GUI]{profiles}")
    return profiles


def save_global_config(global_config):
    # Save all OneDrive config files after configuration change.

    # Load all default values. Needed for to remove all default/empty values from the config before it is saved on disk.
    _default_od_config = read_config(DIR_PATH + "/resources/default_config")

    # Save GUI profile file changes
    _profile_config = copy.deepcopy(global_config)
    logging.debug(f"[save_global_config]:[1]{_profile_config}")

    for profile in _profile_config:
        _profile_config[profile].pop("onedrive", None)

    # # TODO: Re-write to better support future options.
    # _default_profile_config = {"auto_sync": False, "account_type": "", "free_space": ""}

    # if "auto_sync" not in _profile_config[profile]:  # add 'auto_sync' value if missing from older versions
    #     _profile_config[profile]["auto_sync"] = _default_profile_config["auto_sync"]

    # if "account_type" not in _profile_config[profile]:  # add 'account_type' value if missing from older versions
    #     _profile_config[profile]["account_type"] = _default_profile_config["account_type"]

    # if "free_space" not in _profile_config[profile]:  # add 'free_space' value if missing from older versions
    #     _profile_config[profile]["free_space"] = _default_profile_config["free_space"]

    profile_config = ConfigParser()
    profile_config.read_dict(_profile_config)

    # Create profile config file if it does not exist.
    profiles_dir = re.search(r"(.+)/profiles$", PROFILES_FILE).group(1)
    if not os.path.exists(profiles_dir):
        os.makedirs(profiles_dir)

    # Save the new profile.
    with open(PROFILES_FILE, "w") as profilefile:
        profile_config.write(profilefile)

    for profile in global_config:
        # Save OneDrive config changes
        od_config_file = os.path.expanduser(global_config[profile]["config_file"].strip('"'))

        _od_config = {}
        _od_config["onedrive"] = global_config[profile]["onedrive"]

        od_config = ConfigParser()
        od_config.read_dict(_od_config)

        # Remove keys with default values from config before it is saved on disk. OneDrive client can't start when config contains default/empty key values.
        for section in od_config.sections():
            if section in _default_od_config:
                for option in od_config[section]:
                    if (
                        option in _default_od_config[section]
                        and od_config[section][option] == _default_od_config[section][option]
                    ):
                        od_config.remove_option(section, option)

        # Backup last config
        os.system(f"cp {od_config_file} {od_config_file}_backup")

        # Save OD config changes.
        directory = re.search(r"(.+)/.+$", od_config_file).group(1)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(od_config_file, "w") as f:
            od_config.write(f)

        # Remove first line (section) from config file so that OneDrive can read it.
        with open(od_config_file, "r") as input:
            data = input.read().splitlines(True)
        with open(od_config_file, "w") as output:
            output.writelines(data[1:])

        logging.info(f"{profile} config saved")

    logging.info("All configs saved")
    logging.debug(global_config)


def read_config(config_file):
    """
    OneDrive client doesn't use INI file format and can't be natively parsed by ConfigParser because:
        -OneDrive config file does not contain section headers
        -OneDrive client supports multi-line options, which are not supported by ConfigParser
    """
    with open(config_file, "r") as f:
        _config_string = f.read()

    new_config_string = "[onedrive]\n"  # Add section header
    _skip_file_list = []
    _skip_dir_list = []

    # Consolidate multi-line option 'skip_file' and 'skip_dir' into a single line.
    # Values are separated by pipes as per OneDrive client requirements.
    for line in _config_string.splitlines():
        if line.startswith("skip_file "):
            _skip_file_list.append(line.split('"')[1])
            line = ""
        if line.startswith("skip_dir "):
            _skip_dir_list.append(line.split('"')[1])
            line = ""

        new_config_string += line + "\n"

    if len(_skip_file_list) > 0:
        joined_skip_file = f'skip_file = "{"|".join(_skip_file_list)}"'
        new_config_string += joined_skip_file + "\n"

    if len(_skip_dir_list) > 0:
        joined_skip_dir = f'skip_dir = "{"|".join(_skip_dir_list)}"'
        new_config_string += joined_skip_dir + "\n"

    # Load modified OneDrive config file into ConfigParser.
    config = ConfigParser()
    config.read_string(new_config_string)

    return config

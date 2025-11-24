"""
Autostart management for OneDriveGUI.

Handles creation and removal of XDG autostart desktop entries.
Supports both AppImage and source installations.
"""

import os
import logging
from pathlib import Path


def is_running_in_appimage() -> bool:
    """
    Detect if running inside an AppImage.

    Returns:
        bool: True if running in AppImage, False otherwise
    """
    return os.getenv("APPIMAGE") is not None


def get_executable_path() -> str:
    """
    Get the absolute path to the executable.

    For AppImage installations, returns the path to the AppImage file.
    For source/system installations, returns 'OneDriveGUI' (assumes it's in PATH).

    Returns:
        str: Executable path or command
    """
    appimage_path = os.getenv("APPIMAGE")
    if appimage_path:
        # Running in AppImage - use the AppImage path
        # $APPIMAGE already resolves symlinks
        return appimage_path
    else:
        # Running from source or system installation
        # Use command name from PATH (works for AUR and other package managers)
        return "OneDriveGUI"


def get_autostart_file_path() -> Path:
    """
    Get the path to the autostart desktop file.

    Returns:
        Path: Path to ~/.config/autostart/OneDriveGUI.desktop
    """
    config_dir = Path.home() / ".config" / "autostart"
    return config_dir / "OneDriveGUI.desktop"


def is_autostart_enabled() -> bool:
    """
    Check if autostart is currently enabled.

    Returns:
        bool: True if autostart desktop file exists and is not hidden
    """
    autostart_file = get_autostart_file_path()
    if not autostart_file.exists():
        return False

    # Check if the desktop file has Hidden=true
    try:
        with open(autostart_file, "r") as f:
            content = f.read()
            # If Hidden=true is present, autostart is disabled
            if "Hidden=true" in content:
                return False
        return True
    except Exception as e:
        logging.error(f"Error checking autostart status: {e}")
        return False


def enable_autostart() -> bool:
    """
    Enable autostart by creating the desktop file.

    Creates ~/.config/autostart/OneDriveGUI.desktop with the appropriate
    executable path for either AppImage or source installation.

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        autostart_file = get_autostart_file_path()
        autostart_dir = autostart_file.parent

        # Create autostart directory if it doesn't exist
        autostart_dir.mkdir(parents=True, exist_ok=True)

        # Get the correct executable path
        exec_path = get_executable_path()

        # Create desktop file content
        desktop_content = f"""[Desktop Entry]
Type=Application
Version=1.0
Name=OneDriveGUI
Comment=A simple GUI for OneDrive Linux client
Exec={exec_path}
Icon=OneDriveGUI
Terminal=false
Categories=Network;Office;
StartupNotify=false
Hidden=false
"""

        # Write the desktop file
        with open(autostart_file, "w") as f:
            f.write(desktop_content)

        logging.info(f"Autostart enabled: {autostart_file}")
        logging.info(f"Using executable: {exec_path}")
        return True

    except Exception as e:
        logging.error(f"Failed to enable autostart: {e}")
        return False


def disable_autostart() -> bool:
    """
    Disable autostart by removing the desktop file.

    Removes ~/.config/autostart/OneDriveGUI.desktop if it exists.

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        autostart_file = get_autostart_file_path()

        if autostart_file.exists():
            autostart_file.unlink()
            logging.info(f"Autostart disabled: {autostart_file}")
        else:
            logging.info("Autostart file does not exist, nothing to disable")

        return True

    except Exception as e:
        logging.error(f"Failed to disable autostart: {e}")
        return False


def get_autostart_info() -> dict:
    """
    Get information about the current autostart configuration.

    Returns:
        dict: Information about autostart status and paths
    """
    return {
        "enabled": is_autostart_enabled(),
        "desktop_file": str(get_autostart_file_path()),
        "executable": get_executable_path(),
        "is_appimage": is_running_in_appimage(),
    }

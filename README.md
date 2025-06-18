![GitHub all releases](https://img.shields.io/github/downloads/bpozdena/OneDriveGUI/total)

# OneDriveGUI

## About
A GUI for [Linux OneDrive Client](https://github.com/abraunegg/onedrive) with multi-account support.
![image](https://github.com/user-attachments/assets/00769399-1a65-4648-8705-7dee81ee4f52)

## Feature Highlights  
- Management and configuration of multiple OneDrive accounts.
- Asynchronous real-time monitoring of multiple OneDrive accounts.
- Setup wizard for easy OneDrive profile creation and import.
- Auto-sync on GUI startup.
- Support for GUI-based login process.
- System tray (if supported by your desktop environment).
- Start minimized to tray/dock.
- Input validation to prevent configuration of incompatible OneDrive client options.
- Progress monitoring of multiple simultaneous file transfers.
- Import and management of SharePoint Shared Libraries.
- Tooltips with brief explanations of various OneDrive Client configuration options.
- Prompt for re-sync authorization to prevent unexpected data loss.

## Known Limitations
- No window shadows for Wayland sessions.
- No window icon when using AppImage on Wayland sessions.
- AppImage still requires the use of an external browser for authentication.
- Check for other reported [issues/limitations](https://github.com/bpozdena/OneDriveGUI/issues). 

## Compatibility
- Minimum supported OneDrive client version: v2.5.6.
- You will be shown warnings if your OneDrive Client is not up to date.

## Other Notes
- Questions, suggestions, contributions, and bug reports are welcome. 
- Backup your OneDrive config files before importing them to the GUI.
- Backup your data before use to prevent accidental file deletion due to OneDrive misconfiguration. 
- No warranty.

# Running and Installing OneDriveGUI
| :exclamation:        | Ensure the latest version of [OneDrive for Linux](https://abraunegg.github.io/) is installed based on [instructions](https://github.com/abraunegg/onedrive/blob/master/docs/install.md) for your distro. |
|-----------------------|:----------------------------------------------------------------------------------------------------------------|

## AppImage 
1) Download the latest `OneDriveGUI-*-x86_64.AppImage` from the [release assets](https://github.com/bpozdena/OneDriveGUI/releases).
1) Make the `.AppImage` file executable with `chmod +x ./OneDriveGUI-<**version**>-x86_64.AppImage` and run it. 

| :memo:        | Users of Ubuntu 22.04+ may also need to install FUSE2 with `sudo apt install libfuse2`.      |
|---------------|:--------------------------------------------------------------------------------------------|

## AUR
- An AUR package [onedrivegui-git](https://aur.archlinux.org/packages/onedrivegui-git) is available (maintainer: Integral).

## Running from Source

1) Ensure Python3 and [pip](https://pip.pypa.io/en/stable/installation/) are installed on your system. 
1) Clone or download the content of this repository and `cd` into the resultant folder:
    ```sh
    git clone https://github.com/bpozdena/OneDriveGUI.git
    cd OneDriveGUI
    ```
1) Install dependencies:
    ```sh
    python3 -m pip install -r requirements.txt
    ```

1) Start OneDrive GUI:
    ```sh
    cd src/
    python3 OneDriveGUI.py
    ```

    Optionally, you can detach the GUI from the terminal by using the command below:
    ```sh
    cd src/
    nohup python3 OneDriveGUI.py > /dev/null 2>&1 &
    ```

# Usage
- Once the GUI starts, you will be able to create a new OneDrive profile or import your pre-existing one. Just follow the wizard steps.
- You can adjust your OneDrive profile options as needed. 
- Start OneDrive sync in monitor mode via the GUI by pressing the `Play` button.

# Additional Notes
- When importing a OneDrive config file, all comments will be removed.
- If multi-line options `skip_file` and `skip_dir` are used, they will be consolidated into a single line.
- The list of managed OneDrive profiles is stored in `~/.config/onedrive-gui/profiles`. You can manually rename your profile or path to the config file there.
- Newly created OneDrive config files are stored in `~/.config/onedrive/accounts/<profile_name>`.
- Debug logs are saved in ``. Logging can be changed in the GUI settings.

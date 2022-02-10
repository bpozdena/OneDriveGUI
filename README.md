# OneDriveGUI
A simple GUI for [OneDrive Linux client](https://github.com/abraunegg/onedrive), with multi-account support. 

<img src=https://user-images.githubusercontent.com/24818591/153468329-30f14b63-0500-40bd-8e34-5910fcea7e05.png>

# Important notes
- This project is currently in alpha stage.
- Check for known [issues/limitations](https://github.com/bpozdena/OneDriveGUI/issues). 
- Questions, suggestions and bug reports are welcome. 
- Backup your OneDrive config files before importing them to the GUI.
- Backup your data before use to prevent accidental file deletion due to OneDrive misconfiguration. 



# Installation
1) Ensure [OneDrive for Linux](https://abraunegg.github.io/) is installed based on [instructions](https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md) for your distro. 
1) Ensure Python3 and [pip](https://pip.pypa.io/en/stable/installation/) are installed on your system. 
1) Clone or download content this repository.
1) Install dependencies:
	```sh
	python -m pip install -r requirements.txt
	```

1) Start OneDrive GUI:
	```sh
	cd src/
	python OneDriveGUI.py
	```

    Optionally, you can detach the GUI from terminal by using the bellow command:
    ```sh
    nohup python OneDriveGUI.py > /dev/null 2>&1&
    ```

# Use
- Once the GUI starts, you will be able to create a new OneDrive profile or import your pre-existing one. Just follow the wizard steps.
- You can adjust your OneDrive profile options as needed. Most options are already available in the GUI.
- Start OneDrive sync in monitor mode via the GUI. 
- You can also run OneDrive as [systemd service](https://github.com/abraunegg/onedrive/blob/master/docs/USAGE.md#running-onedrive-as-a-system-service), however systemd/journal monitoring is not yet implemented in the GUI. 


# Additional Notes
- When importing OneDrive config file, all comments will be removed. Missing options will be replaced with [default values](src/resources/default_config).
- List of managed OneDrive profiles is stored in "~/.config/onedrive-gui/profiles". You can manually rename your profile or path to config file there until it's possible via the GUI.
- Newly created OneDrive config files are stored in "~/.config/onedrive/accounts/<profile_name>"
- Debug logs are saved in "~/.config/onedrive-gui/onedrivegui.log" (location will be changed in the future).

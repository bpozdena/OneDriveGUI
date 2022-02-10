# OneDriveGUI
A simple GUI for [abraunegg's OneDrive Linux client](https://github.com/abraunegg/onedrive) , with multi-account support. 

<img src=https://user-images.githubusercontent.com/24818591/153468329-30f14b63-0500-40bd-8e34-5910fcea7e05.png>

# Usecases
- Create new OneDrive profile or import pre-existing one.
- Perform configuration changes.
- Start/Stop OneDrive monitoring mode.
- Real-time file transfer monitoring (monitor-mode only).

# Important notes
- This project is currently in alpha stage.
- Check for known [issues/limitations](https://github.com/bpozdena/OneDriveGUI/issues). 
- Suggetions and bug reports are welcome. 


# Installation steps

1) Ensure [OneDrive for Linux](https://abraunegg.github.io/) is instelled based on [instructions](https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md) for your distro. 
1) Ensure Python3 and [pip](https://pip.pypa.io/en/stable/installation/) are installed on your system. 
1) Clone or download content this repository.
1) (Optional) Create and activate a Python virtual environment:
	```sh
	python -m venv venv
	source venv/bin/activate
	```
1) Install dependencies:
	```sh
	python -m pip install -r requirements.txt
	```

1) Start OneDrive GUI:
	```sh
	cd OneDriveGUI/
	python OneDriveGUI.py
	```

    Optionaly, you can detach the GUI from terminal by using the bellow command:
    ```sh
    nohup python OneDriveGUI.py > /dev/null 2>&1&
    ```



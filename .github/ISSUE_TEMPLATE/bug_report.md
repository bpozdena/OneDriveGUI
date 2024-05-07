---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Log**
If applicable, add relevant output from log file `/tmp/onedrive-gui/onedrive-gui.log`.

**System Info**
 - Linux distribution: [e.g. Ubuntu 22.04]
 - Desktop environment:  [e.g. Gnome]
 - Compositor: [e.g. Wayland]
 - Python version: [e.g. 3.11]
 - Version of OneDrive client [e.g. v2.4.25]

or output of below commands:
```sh
lsb_release -a
echo $XDG_CURRENT_DESKTOP
loginctl show-session $(awk '/tty/ {print $1}' <(loginctl)) -p Type | awk -F= '{print $2}'
python --version
which onedrive
onedrive --version
```

**OneDriveGUI info**
How did you install OneDriveGUI?: [AppImage/source/AUR]
What is the name of the AppImage file (if applicable)? : [e.g OneDriveGUI-1.x.x-x86_64.AppImage]


**Additional context**
Add any other context about the problem here.

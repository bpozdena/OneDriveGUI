import psutil

def OneDriveStatus():
    for proc in psutil.process_iter():
        if proc.name().lower() == 'onedrive' and proc.status() != 'zombie':
            print("OneDrive is running.")
            return True
    print("OneDrive is NOT running.")
    return False



OneDriveStatus()
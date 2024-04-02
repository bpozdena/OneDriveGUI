:exclamation:   This branch aims to provide compatibility with the upcoming OneDrive client [v2.5.0-rc1](https://github.com/abraunegg/onedrive/discussions/2662). 

- If you are using `sync_business_shared_folders` in your config file, you will need manually remove it. Check the [client documentation](https://github.com/abraunegg/onedrive/blob/onedrive-v2.5.0-release-candidate-1/docs/business-shared-items.md) for more details.

- There is no backwards compatibility with OneDrive client 2.4.x or older. 
- This GUI branch is only compatible with the Onedrive client v2.5.0_rc1. The path of OneDrive client binary  must be manually specified in the GUI settings.


    Example:
    
    ![image](https://github.com/bpozdena/OneDriveGUI/assets/24818591/9595886f-850a-4f6a-a1b4-e0bd872eb5cc)
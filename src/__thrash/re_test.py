import re

file_path = '/home/bob/OneDrive/Python/One DriveGUI_POC/OneDri veGUI.spec'

root_folder = re.search(r".+/([^/]+)/.+$", file_path)

print(root_folder.group(1))


# stdout = '# Uploading new file Hitchhiking _italy/New Folder/ui_s)(+ěš+ěčšř čýřý*&^&*(etting@#$%^&*s_qt5_$web-test.py ... done.'
# stdout = 'Uploading new file ./config ... done.'

# file_operation = re.search(r'\b([Uploading|Downloading]+)*', stdout)
# file_path = re.search(r'^.*[a-zA-Z]+\s[a-zA-Z]+_([a-zA-Z]+( [a-zA-Z]+)+)/)[a-zA-Z]+\s\.+$', stdout)
# file_path = re.search(r'.*\b[file](.*)/[a-zA-Z0-9.-_]+\s+\.+$', stdout)
# file_name = re.search(r".*/([a-zA-Z0-9.-_]+)\s+\.+", stdout)

# file_name = re.search(r".*/(.+)\s+\.\.\.", stdout)


# transfer_complete = 'done.' in stdout
# print(transfer_complete)


# file_path = re.search(r"\b[file]+\s(.+)\s+\.\.\.", stdout)
# print(file_path)
# print(file_path.group(1))


# print("Operation is: " + file_operation.group(1))
# # print("Path is: " + file_path.group(1))
# # print(file_name)
# # print("Filename is: " + file_name.group(1))
# print(transfer_complete)


# progress = re.search(r'\s([0-9]+)%', stdout)
# print(progress.group(1))

# # transfer_complete = progress.group(1) == '100'

# # print(progress.group(1))
# # print(transfer_complete)

# # print("test")
# # matches = ['Downloading1 file', 'Downloading2 file', 'Uploading new file', 'Downloading new file']
# # test = any(x in stdout for x in matches)
# # print(test)


# transfer_progress = {
#     "file_operation": file_operation.group(1),
#     "file_name": 'Resuming last file...' if file_name is None else file_name.group(1),
#     # "progress": progress,
#     "transfer_complete": transfer_complete
# }

# print(transfer_progress)
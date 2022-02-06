import subprocess, os, signal, time, shlex, sys, re


# def run_command(command):
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
#     while True:
#         output = process.stdout.readline()
#         if output == '' and process.poll() is not None:
#             break
#         # if 'one' in str(output):
#         #     print("MATCH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         if output:
#             print(output.strip())    

#     rc = process.poll()
#     return rc

# run_command("sudo -S tcpdump -i homebr0 proto 1 <<< C@rnival1")




# app = subprocess.Popen("journalctl -f", shell=True, stdout = subprocess.PIPE, universal_newlines = True)

# while True:
#     print(app.communicate()[0])

# invoke process
# command = 'sudo -S tcpdump -i homebr0 "proto 1" <<< C@rnival1'
# process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)

# # Poll process.stdout to show stdout live
# while True:
#   output = process.stdout.readline()
#   print(output)
#   if process.poll() is not None:
#     break
#   if output:
#     print(output.strip())
# rc = process.poll()


######################




# command = shlex.split("ping -c 5 asdasdasdsad.com")

# def oneDriveMonitor(command="onedrive --monitor"):

#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=False)

#     # while True:
#     while process.poll() == None:
#         stdout = process.stdout.readline()
#         try:
#             stderr =  process.stderr.readline()
#         except:
#             pass    
#         if stdout != '':
#             if '1.1.1.1' in stdout:
#                 print('pinging one.one.one')
#             if 'time' in stdout:
#                 print('# ' + stdout)
#             else:
#                 print('@@ ' + stdout.strip())

#         if stderr != '':
#             if 'command not found' in stderr:
#                 print("Onedrive does not seem to be installed. Please install it as per instruction at https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md ")
#             elif '--resync is required' in stderr:
#                 print(str(stderr) + " Starting resync.")
#                 # oneDriveMonitor("onedrive --monitor --resync")
#             else:
#                 print('@@ERROR' + stderr)


    # match line:
    #     case "1.1.1.1" in line:
    #         print(line)
        

# oneDriveMonitor()



# else:
#     break
    


# output, err = process.communicate()
# print(output)






def oneDriveMonitor(command):
    # command = "onedrive --monitor -v"
    process = subprocess.Popen( command, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                shell=True, 
                                universal_newlines=True)


    while process.poll() == None:

        if process.stdout:
            stdout = process.stdout.readline()        

            if 'Authorize this app visiting' in stdout:
                self.show_login()
            if 'time' in stdout:
                print('# ' + stdout)
            else:
                print('@@ ' + stdout.strip())


    if process.stderr:
        stderr = process.stderr.readline()
        print('!!!!ERROR ' + stderr)

        if 'command not found' in stderr:
            print("Onedrive does not seem to be installed. Please install it as per instruction at https://github.com/abraunegg/onedrive/blob/master/docs/INSTALL.md ")
        elif '--resync is required' in stderr:
            print(stderr.decode() + " Starting resync.")
            oneDriveMonitor("onedrive --monitor --resync")
        else:
            print('@@ERROR' + stderr)


oneDriveMonitor("onedrive --monitor")

# WIFI PASS GETTER FOR WINDOWS BY MOHAMED TAREK.
# FOR FOR INFO ABOUT THE SCRIPT PLEASE GO TO README.md.

import os
import logging
import sys
from colorama import init, Fore

if sys.platform == "win32":
    isWindows = True

# Basic simple log file configuration to save wifi details.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(message)s",
    filename="usage.log"
    )

# Colors stored in some variables for shortcuts.
init(autoreset=True)
error = Fore.RED
success = Fore.GREEN
output = Fore.BLUE
normal = Fore.YELLOW
warn = Fore.LIGHTYELLOW_EX

def main():
    # Display to user
    os.system(f"netsh wlan show profiles")
    # For Saving all the stored networks on the Windows PC.
    profiles_path = os.getcwd() + "\\profiles.txt"
    os.system(f"netsh wlan show profiles>{profiles_path}")

    def get_pass(network_name):
        # Checking for validity of network name.
        size = network_name.split()
        if len(size) >= 3:
            print(f"{error}please enter a proper network name")
        # Checking if the network is not found in the system.
        with open(profiles_path, 'r') as f:
            check = f.read().split()
            if network_name.capitalize() not in check:
                print(f"\n{error}Network not found in the system")
        # For creating a temp file to save the network information.
        tempfile_path = os.getcwd() + "\\temp.txt"
        os.system(f"netsh wlan show profiles {network_name} key = clear>{tempfile_path}")
        # Checking for network security settings and fetching password.
        with open(tempfile_path, "r") as f:               
            for l in f:
                if "Key Content" in l:
                    print(f"\n\n{success}Successfully done! Showing key content (password) for {network_name}:\n\nPassword {output}{l[27: ]}")
                    logging.info(f"\nNetwork name: {network_name}\nPassword{l[27: ]}")
                elif "Absent" in l:
                    print(f"{error}No security key found")
        print(f"\n{warn}choose from the above available network profiles\n", "_" * 50)
        # After getting done with the temp file, we delete it.
        os.remove(tempfile_path)
    # Handling exceptions with shortcut keys used to exit the app.
    try:
        while True:        
            user_inpt = input(f"\n{normal}Enter the wifi network (user profile) to be hacked: ")
            get_pass(user_inpt)       
    except KeyboardInterrupt:
        exit("\nEXITED")
    except EOFError:
        exit("\nEXITED")

# Cuz y not lol    
if __name__ == "__main__" and isWindows:
    main()
else:
    from time import sleep
    print(f"This app is not available except on windows devices")
    sleep(3)
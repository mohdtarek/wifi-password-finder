# WIFI PASS GETTER FOR WINDOWS BY MOHAMED TAREK.
# FOR FOR INFO ABOUT THE SCRIPT PLEASE GO TO README.md.

import os
import logging
import sys
from time import sleep
from colorama import init, Fore

isWindows = False
# Since the os.system commands in the script are only for Windows CMD.
if sys.platform == "win32":
    isWindows = True # Code is unrichable incase you viewing this script on either mac os or Linux os device

# Basic simple log file configuration to save wifi details.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(message)s",
    filename="SSID-Details.log"
    )

# Colors stored in some variables for shortcuts.
init(autoreset=True)
error = Fore.RED
success = Fore.GREEN
output = Fore.BLUE
normal = Fore.YELLOW
warn = Fore.LIGHTYELLOW_EX

def main():
    print(f"{warn}Please note that network names are case sensitive! make sure you enter the network name correctly.")
    # Display to user
    os.system(f"netsh wlan show profiles")
    # For Saving all the stored networks on the Windows PC.
    profiles_path = os.getcwd() + "\\profiles.txt"
    os.system(f"netsh wlan show profiles>{profiles_path}")

    def get_pass(SSID):  # SSID = network name
        # Checking for validity of network name.
        size = SSID.split()
        if len(size) >= 3:
            print(f"{error}please enter a proper network name")
        # Checking if the network is not found in the system.
        with open(profiles_path, 'r') as f:
            check = f.read().split()
            if SSID not in check:
                print(f"\n{error}Try again in case if you didn't get network details, make sure you choose from the list or check for letter cases")
        # For creating a temp file to save the network information.
        tempfile_path = os.getcwd() + "\\temp.txt"
        os.system(f"netsh wlan show profiles {SSID} key = clear>{tempfile_path}")
        # Checking for network security settings and fetching password.
        with open(tempfile_path, "r") as f:               
            for l in f:
                if "Key Content" in l:
                    print(f"\n\n{success}Successfully done! Showing key content (password) for {SSID}:\n\nPassword {output}{l[27: ]}")
                    logging.info(f"\nNetwork name: {SSID}\nPassword{l[27: ]}")
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
    except FileNotFoundError:
        print(f"{error}Error running the script. Try to reinstall repository or change path. If it didn't work, copy the scrip manually and run it.")
        sleep(3)

 
if __name__ == "__main__" and isWindows:
    main()
else:
    print(f"{error}Please make sure you are running the correct script in the correct terminal/ operating system")
    sleep(2)
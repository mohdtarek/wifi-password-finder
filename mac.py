# WIFI PASS GETTER FOR MAC OS BY MOHAMED TAREK.
# FOR FOR INFO ABOUT THE SCRIPT PLEASE GO TO README.md.

import os
import sys
from colorama import init, Fore
from time import sleep

isMac = False
# Since the os.system commands in the script are only for mac terminal.
if sys.platform == "darwin":
    isMac = True  # Code is unrichable incase you viewing this script on either windows or Linux os device

# Colors stored in some variables for shortcuts.
init(autoreset=True)
error = Fore.RED
normal = Fore.BLUE
warn = Fore.LIGHTYELLOW_EX
output = Fore.WHITE

def main():
    print(f"{warn}Please note that network names might be case sensitive! make sure you enter the network name correctly.")
    def get_pass(SSID):
            os.system(f'Security find-generic-password -ga "{SSID}" | grep "Password"')

    try:
        while True:        
            user_inpt = input(f"\n{normal}Enter the wifi network (user profile) to be hacked: {output}")
            get_pass(user_inpt)       
    except KeyboardInterrupt:
        exit("\nEXITED")
    except EOFError:
        exit("\nEXITED")
        
         
if __name__ == "__main__" and isMac:
    main()
else:
    print(f"{error}Please make sure you are running the correct script in the correct terminal/ operating system")
    sleep(2)
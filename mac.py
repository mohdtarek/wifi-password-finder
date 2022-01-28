#!/bin/bash
# FOR FOR INFO ABOUT THE SCRIPT PLEASE GO TO README.md.

import os
import sys
from colorama import init, Fore
from time import sleep

# Procedure before starting the script.
isMac = False
# Since the os.system commands in the script are only for mac terminal.
if sys.platform == "darwin":
    isMac = True
else:
    print("\nRunning the correct script based on your operating system")
    try:
        os.system("python3 run.py")
    except (KeyboardInterrupt, EOFError):
        exit("\nEXITED")

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
    except (KeyboardInterrupt, EOFError):
        exit("\nEXITED")


if __name__ == "__main__":
    main()

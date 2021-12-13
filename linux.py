# WIFI PASS GETTER FOR LINUX BY MOHAMED TAREK.
# FOR FOR INFO ABOUT THE SCRIPT PLEASE GO TO README.md.

# import os
import logging
import sys
from colorama import init, Fore
from time import sleep

isLinux = False
# Since the os.system commands in the script are only for linux bash.
if sys.platform == "linux" or sys.platform == "linux2":
    isLinux = True  # Code is unrichable incase you viewing this script on either windows or mac os device


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
    print("Script is still under development, sorry for the inconvenience!")
    sleep(2)


# Cuz y not lol    
if __name__ == "__main__" and isLinux:
    main()
else:
    print(f"Please make sure you are running the correct script in the correct terminal/ operating system")
    sleep(2)
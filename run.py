"""
Run this script if you are unsure whether which script to run.
Refere to README.md for further information.

"""

import os
from sys import platform


def main():
    # Since the os.system commands for netsh wlan in the script are only for Windows CMD.
    if platform == 'win32':
        os.system("python3 win.py")
    # Since the os.system commands for security find in the script are only for mac terminal.
    elif platform == 'darwin':
        os.system("python3 mac.py")
    # Since the os.system commands in the script are only for linux bash. (Under developement)
    elif platform == 'linux':
        os.system("python3 linux.py")
    # This will happen probably if the client is using a different shell in a particular os.
    else:
        with open("README.md", 'r') as f:
            print(f.read())
            from time import sleep
            print("exiting after 20 seconds")
            sleep(20)


if __name__ == '__main__':
    main()
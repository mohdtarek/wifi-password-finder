# wifi-password-finder
To be used in school/uni computer lab to find your targeted WI-FI router in the room to get it's password. It can also be used in pc device at home to find the password of the Wi-fi network  'reveal password'.

# win.py
Run win.py for windows. If in ubuntu bash or simillar, run linux.py. However, running script run.py will run a script based on the operating system.

This program will list all the available wifi names instantly when running. List of wifi names will appear, enter a network name then the password of the wifi will show up. A text file 'profiles.txt' will be created and it will be showing all the available wifi names. A log file 'info.log' will be created and it will store all the successful attempts for references.

# mac.py
Run mac.py for Mac os.

When entering a wifi that's stored in the keychain (PC SYSTEM), the password will be shown. If not, message will show up saying: 'Security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.'



# linux.py
Run linux.py for linux.

Linux script is still under development. sorry for the inconvenience.

# run.py
Run this script if you are unsure which script to run. Anything else will be under developenet.


# No script is working
Step1: create a python file
step2: copy paste this code and run it:
        import sys
        print(sys.platform)
step3: if output = "win64", "cygwin", or "msys", go to win.py and edit line 11, replace win32 with whatever output.


# wifi-password-finder
beginners code using os module.
To be used in school/uni computer lab to find (hack) your targeted WI-FI router in the room to get it's password. You can also use this in your device at home to find the password of your own Wi-fi network incase you forgot it.

# win.py
Run win.py if your operating system is windows. If you are running your program in ubuntu bash or simillar, make sure you run linux.py. However, if you are unsure what script to run, you can run run.py and it will run the script based on your operating system.

This program will list you all the available wifi names instantly when you run it. You will have to choose one of the network names available, then the password of the wifi will show up. A text file 'profiles.txt' will be created and it will be showing all the available wifi names. a log file 'info.log' will be created and it will store all the successful wifi password hacks for references.

# mac.py
Run mac.py if your operating system is Mac os. Make sure you are using the correct os terminal.

This program may not be that as good as the windows program, but it's still good enough to get a wifi password. When you enter a wifi that's stored in the keychain (PC SYSTEM), the password will be shown. If not, you will get a message saying: 'Security: SecKeychainSearchCopyNext: The specified item could not be found in the keychain.'



# linux.py
Run linux.py if your operating system is linux. You can still run linux.py on windows / mac if you are using a linux bash or a VM that runs linux.py

Linux script is still under development. sorry for the inconvenience.

# run.py
Run this script if you are unsure which script to run. Anything else will be under developenet. Make sure you are running those scripts in a proper bash


# What to do if I can't run any of those scripts?
Step1: create a python file
step2: copy paste this code and run it:
        import sys
        print(sys.platform)
step3: if you got "win64", "cygwin", or "msys" simply go to win.py and edit line 11, replace win32 with them


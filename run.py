#WIFI PASS GETTER FOR WINDOWS BY MOHAMED TAREK
#FOR FOR INFO ABOUT THE SCRIPT PLEASE GO TO README.md

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s:%(message)s",
    filename="usage.log"
    )

os.system(f"netsh wlan show profiles")
def pass_getter(network_name):
    size = network_name.split()
    if len(size) >= 3:
        print("please enter a proper network name")
    script_path = os.getcwd() + "\\temp.txt"
    os.system(f"netsh wlan show profiles {network_name} key = clear>{script_path}")
    with open(script_path, "r") as f:               
        for l in f:
            if "Key Content" in l:
                print(f"\n\nShowing key content (password) for {network_name}:\n\nPassword {l[27: ]}")
                logging.info(f"\nNetwork name: {network_name}\nPassword{l[27: ]}")
            elif "Absent" in l:
                print("No security key found")
    print("\nchoose from the above available network profiles\n", "_" * 50)
    os.remove(script_path)
try:
    while True:        
        user_inpt = input("\nEnter the wifi network (user profile) to be hacked: ")
        if __name__ == "__main__":
            pass_getter(user_inpt)       
except KeyboardInterrupt:
    exit("\nEXITED")
except EOFError:
    exit("\nEXITED")

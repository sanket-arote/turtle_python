# Note for this program that "Where your cursor will be their all msgs will be printed"

import pyautogui
import time

# This time is about initial startup time i.e. after 10 sec msg printing will start

time.sleep(10)

for i in range(20):

    time.sleep(0)                   # This is the interval time between 2 msgs.

    # This is generally msg which is to be displayed.

    pyautogui.typewrite("This message is generated using Python GUI")

    pyautogui.press('Enter')                    # This is command button.

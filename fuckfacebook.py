import pyautogui
import time

def check_and_close():
        check = pyautogui.getActiveWindowTitle()
        print(check)
        if "Facebook" in check:
            pyautogui.keyDown("ctrl")
            pyautogui.press("w")
            pyautogui.keyUp("ctrl")

def fuckfacebook(length=True, unit=None, interval: int=45):
    unit_dict = {"h": 3600, "hour": 3600, "m": 60, "minute": 3600, "s": 1, "second": 1}
    length = length * unit_dict.get(unit, 1)
    if length == True:
        while length:
            time.sleep(interval)
            check_and_close()
    else:
        for i in range(length):
            time.sleep(interval)
            check_and_close()        


fuckfacebook(interval=5)
#pip install pynput
#pip install pyautogui

from pynput import keyboard
import pyautogui
import time

# keyboard combination to trigger execute script
COMBINATIONS = [
    {keyboard.Key.insert, keyboard.KeyCode(char='\\')}
]

# The currently active modifiers
current = set()

# This setup saves image files sequentially, so asks for a starting file number
tile_num = int(input("enter starting file number")) 
print("starting tile: "+str(tile_num))
PAUSE_BETWEEN_KEYS = 0.1                # increase time between keystrokes if computer cannot keep up

# change this to match needed keyboard and mouse automation
# see pyautogui documentation
def codenames_capture():
    pyautogui.hotkey('ctrl', 'c')       # press ctrl + c
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.hotkey('ctrl', 'n')       # press ctrl + n
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.write(str(tile_num))      # type the name of the file
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.press('enter')            # press enter
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.hotkey('ctrl', 'v')       # press ctrl + v
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.hotkey('ctrl', 'alt', 'i')# press ctrl + alt + i
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.write('300')              # type 300 (pixel size)
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.press('enter')            # press enter
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.hotkey('ctrl', 'shift', 's') # press ctrl + shift + s
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.press('tab')              # press tab (move to next field)
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.press('j')                # press j (to select jpg)
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.press('enter')            # press enter
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.press('enter')            # press enter
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.hotkey('ctrl', 'w')       # press ctrl + w
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.press('right')            # press right arrow
    time.sleep(PAUSE_BETWEEN_KEYS)
    pyautogui.press('enter')            # press enter
    time.sleep(PAUSE_BETWEEN_KEYS)

def execute():
    global tile_num
    codenames_capture()
    tile_num = tile_num + 1
    print ("File "+str(tile_num)+" saved!")
    

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




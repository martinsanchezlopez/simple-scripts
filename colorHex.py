import pyautogui
from pynput import mouse
import pyperclip

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:      
        colorHex(pyautogui.pixel(x, y))
        listener.stop()

def colorHex(RGBArray):
    color = '#'
    for i in range(0,3):
        color += hex(RGBArray[i])[2:]
    pyperclip.copy(color)

with mouse.Listener(
        on_click=on_click) as listener:
    listener.join()

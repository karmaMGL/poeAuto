import pyautogui as pag
import keyboard
import time
import random
import cv2

# pag.displayMousePosition()
x= 215 
y= 990 
#  health position
x2 = 80


screenshot = pag.screenshot()

checker = True
while checker:
    if(keyboard.is_pressed('v')):
        checker = False
        print("Quitting")
        break
    num = random.uniform(0.1, 0.4)
    time.sleep(num)
    screenshot = pag.screenshot()
    pixel_color = screenshot.getpixel((x2, y))

    def HealthPotion():
        num = random.randrange(0, 2)
        arr = ['1', '2']
        keyboard.press_and_release(arr[num])

    # Print the RGB color value of the pixel

    print(f"The color of the pixel at ({x}, {y}) is: {pixel_color}")
    if(pixel_color != (98, 11, 17)):
        print("Health is full")
        HealthPotion()
        time.sleep(1)
    

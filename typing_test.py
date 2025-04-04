import pytesseract
import cv2
import subprocess
import os
import pyautogui
import nltk
from time import sleep
from PIL import Image


def take_screenshot():
    # Take the screenshot using Spectacle
    subprocess.run(["spectacle", "-b", "-n", "-d", "0", "-o", "screenshot.png"], check=True)

    # Open the screenshot image using Pillow
    screenshot = Image.open("screenshot.png")

    crop_box = (300, 520, 2700, 1325)

    # Crop the screenshot
    cropped_img = screenshot.crop(crop_box)

    # Save the cropped image
    cropped_img.save("text.png")

def do_test():
    img = cv2.imread('text.png')


    text = pytesseract.image_to_string(img)

    words = nltk.tokenize.word_tokenize(text)

    sent = ""

    for word in words:
        sent += word + " "

    # pyautogui.typewrite(sent, 0.0275)
    pyautogui.typewrite(sent, 0.03)

def restart_test():
    sleep(1)
    pyautogui.typewrite(['tab', 'enter'])



try:
    sleep(2)
    while True:
        take_screenshot()
        do_test()
        restart_test()

        
except KeyboardInterrupt:
    print("Stopped.")

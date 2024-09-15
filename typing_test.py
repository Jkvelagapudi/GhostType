import pytesseract
import cv2
import subprocess
import os
import pyautogui
import nltk

subprocess.run(["spectacle", "-r", "-b", "-n", "-d", "5000", "-o", "screenshot.png"])


img = cv2.imread('screenshot.png')


text = pytesseract.image_to_string(img)

words = nltk.tokenize.word_tokenize(text)


for word in words:
    pyautogui.typewrite(word)
    pyautogui.press('space')

os.remove("screenshot.png")
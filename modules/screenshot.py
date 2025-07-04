import pyautogui
from datetime import datetime
import os

LOG_FILE = "logs/screenshot.png"

def capture():
    #Captures the current screen and saves the image to a PNG file.
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        # Capture screen shot and saves to file
        screenshot = pyautogui.screenshot()
        screenshot.save(LOG_FILE)
        print("[INFO] Screenshot captured.")
    except Exception as e:
        print(f"[ERROR] Screenshot capture failed: {e}")
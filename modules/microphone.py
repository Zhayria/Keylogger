import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import os

LOG_FILE = "logs/audio.wav"

def record(duration=10, samplerate=44100):
    try:
        print("[INFO] Recording microphone...")
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        write(LOG_FILE, samplerate, audio)
        print("[INFO] Microphone recording saved.")
    except Exception as e:
        print(f"[ERROR] Microphone failed: {e}")
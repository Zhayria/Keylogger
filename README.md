# Mac Keylogger (Cybersecurity Educational Project)

This is a multi-functional keylogger developed in Python, designed for **educational and ethical hacking** purposes only. It collects keystrokes, screenshots, clipboard contents, microphone recordings, and system information — then sends encrypted log files via email at regular intervals.

> **DISCLAIMER**: This tool is strictly for **educational use** and **authorized environments** (such as cybersecurity labs or personal devices). Unauthorized use is illegal and against ethical guidelines.

---

## Features

-  **Keylogging**: Captures user keystrokes in the background
-  **System Info**: Logs system specs and user details
-  **Clipboard Capture**: Extracts current clipboard contents
-  **Microphone Recording**: Records ambient audio at intervals
-  **Screenshot Capture**: Takes periodic screenshots
-  **Fernet Encryption**: Secures sensitive log files
-  **Email Reports**: Sends logs to a configured email address
-  **Task Scheduler**: Automates all tasks via timers

---

##  Technologies Used

- Python 3.x
- `pynput`, `sounddevice`, `scipy`
- `smtplib`, `email`, `cryptography`
- `threading`, `platform`, `socket`, `getpass`

---

##  Project Structure

```text
mac_keylogger_project/
├── main.py                     # Entry point for running the keylogger
├── config.py                  # Your private config (in .gitignore)
├── config_sample.py           # Safe-to-share config template
├── requirements.txt           # List of Python dependencies
├── .gitignore                 # Files/folders to exclude from Git
├── README.md                  # Project documentation

├── modules/                   # Core functionality modules
│   ├── logger.py              # Keystroke logging
│   ├── system_info.py         # System info gathering
│   ├── clipboard.py           # Clipboard capturing
│   ├── microphone.py          # Microphone audio recording
│   ├── screenshot.py          # Screenshot capturing
│   ├── emailer.py             # Sending logs via email
│   ├── encryptor.py           # Encrypt logs using Fernet
│   └── timer.py               # Task scheduling system

└── logs/                      # Output directory for log files (ignored by Git)
    ├── keylog.txt
    ├── systeminfo.txt
    ├── clipboard.txt
    ├── screenshot.png
    └── audio.wav
```

---

##  Setup Instructions

1. **Clone the repo**:
   ```bash
   git clone https://github.com/Zhayria/Mac_Keylog.git
   cd Mac_Keylog
   ```

2. **Create `config.py` based on `config_sample.py`**:
   - Fill in:
     - `EMAIL_ADDRESS`
     - `EMAIL_PASSWORD` (use an App Password if Gmail)
     - `FERNET_KEY` (generate with `Fernet.generate_key()`)

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program**:
   ```bash
   python3 main.py
   ```

---

## Example `config_sample.py`

```python
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "receiver@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
FERNET_KEY = b'your_fernet_key_here'
```

---

##  Build Into Executable (Optional)

To build as an executable on macOS:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

---

##  Author

**Zhayria Washington**  
M.S. in Computer Science – Cybersecurity  
[LinkedIn](https://www.linkedin.com/in/zhayria-washington-2a2b86221)

---

##  Ethical Use Policy

This software is intended for cybersecurity research, ethical hacking education, and penetration testing **with explicit permission**.  
**Do not use** this tool to target or spy on individuals, corporations, or organizations without consent.

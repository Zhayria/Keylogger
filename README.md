# Mac Keylogger (Cybersecurity Educational Project)

This is a multi-functional keylogger developed in Python, designed for **educational and ethical hacking** purposes only. It collects keystrokes, screenshots, clipboard contents, microphone recordings, and system information — then sends encrypted log files via email at regular intervals.

> **DISCLAIMER**: This tool is strictly for **educational use** and **authorized environments** (such as cybersecurity labs or personal devices). Unauthorized use is illegal and against ethical guidelines.

---

##  Features

- **Keylogging**: Captures user keystrokes in the background
- **System Info**: Logs system specs and user details
- **Clipboard Capture**: Extracts current clipboard contents
- **Microphone Recording**: Records ambient audio at intervals
- **Screenshot Capture**: Takes periodic screenshots
- **Fernet Encryption**: Secures sensitive log files
- **Email Reports**: Sends logs to a configured email address
- **Task Scheduler**: Automates all tasks via timers

---

## 🛠️ Technologies Used

- Python 3.x
- `pynput`, `sounddevice`, `scipy`
- `smtplib`, `email`, `cryptography`
- `threading`, `platform`, `socket`, `getpass`

---

## 📁 Project Structure
mac_keylogger_project/
│
├── main.py                     # Entry point: starts logger, timers, collection
├── config.py                   # Private config file (excluded via .gitignore)
├── config_sample.py            # Safe example config (for sharing)
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignore sensitive and system files
├── README.md                   # Project description and setup instructions
│
└── modules/                    # All supporting functionality
    ├── logger.py               # Keystroke logging (pynput)
    ├── system_info.py          # Collects OS, user, and machine details
    ├── clipboard.py            # Captures clipboard contents
    ├── microphone.py           # Records ambient audio using sounddevice
    ├── screenshot.py           # Takes screenshots at intervals
    ├── emailer.py              # Sends logs as email attachments
    ├── encryptor.py            # Fernet encryption for secure log handling
    └── timer.py                # Threaded scheduler for periodic tasks

logs/                           # Output folder for logs (excluded from Git)
├── keylog.txt
├── systeminfo.txt
├── clipboard.txt
├── screenshot.png
└── audio.wav

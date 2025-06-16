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


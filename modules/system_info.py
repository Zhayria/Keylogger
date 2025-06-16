import socket
import platform
import getpass
from datetime import datetime

LOG_FILE = "logs/systeminfo.txt"

def collect():
    try:
        with open(LOG_FILE, "w") as f:
            f.write(f"System Infromation Report - {datetime.now()} \n")
            f.write(f"Username: {getpass.getuser()} \n")
            hostname = socket.gethostname()
            f.write(f"Hostname: {hostname} \n")
            ip_address = socket.gethostbyname(hostname)
            f.write(f"IP Address: {ip_address}\n")
            f.write(f"Platform: {platform.system()} {platform.release()} \n")
            f.write(f"Processor: {platform.processor()} \n")
            f.write(f"Machine: {platform.machine()} \n")

    except Exception as e:
        print(f"[ERROR] System info collection failed: {e}")

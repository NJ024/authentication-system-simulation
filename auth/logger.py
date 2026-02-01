import datetime
import os

LOG_FILE_PATH = "logs/login_logs.txt"


def log_attempt(username, status):
    """Logs login attempts with timestamp."""
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE_PATH, "a") as file:
        file.write(f"[{datetime.datetime.now()}] User: {username} | Status: {status}\n")

from auth.password_utils import hash_password, check_password_strength
from auth.logger import log_attempt

MAX_ATTEMPTS = 3

# Simulated database with hashed passwords
users = {
    "admin": hash_password("Admin@123"),
    "nj": hash_password("Pass123"),
    "guest": hash_password("guest")
}

failed_attempts = {}


def authenticate():
    print("=" * 45)
    print("🔐 AUTHENTICATION SYSTEM SIMULATION")
    print("=" * 45)

    username = input("Enter username: ")

    if username not in users:
        print("❌ Username not found.")
        log_attempt(username, "Failed - Username not found")
        return

    if username not in failed_attempts:
        failed_attempts[username] = 0

    if failed_attempts[username] >= MAX_ATTEMPTS:
        print("🚫 Account locked due to multiple failed attempts.")
        log_attempt(username, "Account Locked")
        return

    password = input("Enter password: ")
    print("Password strength:", check_password_strength(password))

    hashed_input = hash_password(password)

    if hashed_input == users[username]:
        print("✅ Login successful!")
        log_attempt(username, "Success")
        failed_attempts[username] = 0
    else:
        failed_attempts[username] += 1
        remaining = MAX_ATTEMPTS - failed_attempts[username]
        print(f"❌ Incorrect password. Attempts left: {remaining}")
        log_attempt(username, "Failed - Wrong password")

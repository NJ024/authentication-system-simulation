# Python Authentication System Simulation

A Python-based authentication system simulation demonstrating secure login handling, password hashing, brute-force protection, and activity logging.

## 🧠 Overview

This project simulates a secure authentication system similar to what you might find in real applications. It demonstrates fundamental security concepts used in access control and secure login systems.

# Features

✔ Multi-user login  
✔ Brute-force protection with account lockout  
✔ Password hashing (SHA-256)  
✔ Password strength validation  
✔ Timestamp-based login logging  
✔ Login activity logging with timestamps  

*Security tip:* In production systems you would use better hashing algorithms (e.g., bcrypt, Argon2) with salts for stronger protection.

---

## 🛠️ Tech Stack
- Python 3.x  
- `hashlib` for hashing  
- Modular design (`auth_logic`, `password_utils`, `logger`)  

## 📦 Installation
```bash
git clone https://github.com/NJ024/authentication-system-simulation.git
cd authentication-system-simulation
pip install -r requirements.txt
python main.py
